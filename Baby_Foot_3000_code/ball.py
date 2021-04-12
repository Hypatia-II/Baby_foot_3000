# -*- coding: utf-8 -*-

__author__ = "Sacha HIRSCH"

from physics_engine import *
from random import choice, gauss
from terrain import Terrain
from game_stats import Stat
from PyQt5 import QtGui, QtCore
import os


class Ball:
    """Classe instanciant une balle, et contenant les fonctions de gestion de la partie"""

    image = QtGui.QImage(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'Assets/Images/ballV2.png'))  # Définition de l'image associée à la balle

    def __init__(self, terrain=Terrain()):  # On crée un terrain à la création de la balle si aucun terrain n'est
        # spécifié.

        f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameters.cfg"),
                 'r')  # On ouvre le fichier parameters contenant les paramètres de jeu (modifié en
        # amont pour moduler la difficulté)

        param = f.readlines()  # On récupère les paramètres définis dans le fichier parameters
        f.close()

        self.time_step = float(param[5].split('\t')[2])  # s
        self.drag = float(param[6].split('\t')[2])
        self.bounce_bonus = float(param[7].split('\t')[2])
        self.player_length = float(param[4].split('\t')[2])  # m
        self.player_width = float(param[3].split('\t')[2])  # m
        self.forward_kick_speed = float(param[9].split('\t')[2])  # m/s
        self.catch_radius = float(param[10].split('\t')[2])  # sans unité
        self.initial_speed = float(param[11].split('\t')[2])  # m/s

        self.terrain = terrain
        self.stat = Stat()  # On crée une instance de la classe Stat, qui sera liée à la balle
        self.radius = 0.01  # Rayon de la balle
        self.coords = np.array([self.terrain.width / 2, self.terrain.length / 2])  # m
        self.velocity = np.array([0, 0])  # m/s
        self.collision_detected = False
        self.step = 0
        self.col_radius = self.terrain.length
        self.default_coords = np.array([self.terrain.length / 2, self.terrain.width / 2])
        self.team_blue_state = 0
        self.team_red_state = 0
        self.is_caught = False
        self.just_caught = True
        self.forward_kick = False
        self.released = False
        self.possessing_player = None

        self.qpoint = QtCore.QPoint()

    def next_step(self):
        """Méthode faisant avancer les joueurs et la balle d'un pas. Tout d'abord, on fait avancer les joueurs en
        détectant au passage une éventuelle collision. Si il y a collision à ce stade, on passe au pas suivant.
        Sinon, pour faire avancer la balle, on distingue deux cas selon si un joueur est en possession de la balle ou
        non.

        - Dans le cas où aucun joueur n'a la balle, on calcule sa position suivante avec la méthode d'Euler.
        On fait ensuite appel à la fonction collision qui va détecter une éventuelle collision, puis déterminer les
        vraies nouvelles coordonées et vitesses de la balle. Dans le cas où il n'y a pas de collision, celles-ci seront
        égales celles calculées par la méthode d'Euler.

        - Si un joueur est en possession de la balle, celle-ci le suit dans son mouvement. Si le joueur vient juste
        d'attrapper la balle, celle-ci est replacée devant lui. Si l'utilisateur relâche simplement la balle, on lui
        donne une faible impulsion. Si l'utilisateur frappe la balle, on lui donn une forte impulsion.
        """

        self.stat.left_just_scored = False
        self.stat.right_just_scored = False
        self.step += 1
        kicked = False

        # On bouge les joueurs et on teste dans le même temps si une frappe est réalisée

        for bar in self.terrain.bars:  # On parcourt toutes les barres du terrain

            if bar in self.terrain.team_red_bars:  # Si la barre appartient à l'équipe rouge, on la bouge selon la
                # commande clavier du joueur rouge
                kick, speed, newcoords = bar.bar_move(self.team_red_state, self.coords)
            else:  # De même pour l'équipe bleue
                kick, speed, newcoords = bar.bar_move(self.team_blue_state, self.coords)

            if kick is not None:  # Si un joueur a percuté la balle durant son mouvement
                self.coords = newcoords  # Les nouvelles coordonnées de la balles sont celles calculées lors de cette
                # collision

                # On doit à présent donner une nouvelle vitesse à la balle. Ici, on va abandonner les lois de Descartes
                # pour donner une sensation plus proche du baby-foot en offrant à l'utilisateur plus de contrôle sur la
                # balle. Ainsi, la nouvelle vitesse est configurée de telle facçon que le joueur donne de légères
                # poussées à la balle au fur et à mesure qu'il avance.

                if self.velocity[1] * speed > 0:
                    # Si la balle et le joueur allaient dans le même sens , on soustrait la vitesse du joueur à celle de
                    # la balle

                    self.velocity[1] += -speed

                else:  # Sinon, on inverse la vitesse du joueur
                    self.velocity[1] = -self.velocity[1] + speed

                # On ajoute efin une légère vitesse horizontale pour éviter que la balle rebondisse indéfniment entre
                # deux joueurs côte à côte

                self.velocity[0] += choice((-self.player_width / 150, self.player_width / 150)) / self.time_step * \
                    self.velocity[1]

                kicked = True

        if not self.is_caught:  # Si la balle n'est pas attrapée par un joueur
            if not kicked:  # On applique la detection de collision si la balle n'a pas été touchée par un joueur

                newvalues = euler(self)  # On calcule d'abord naïvement (sans se préoccuper d'une éventuelle collision)
                # les nouvelles position et vitesse de la balle à l'aide de la fonction euler. Ces valeurs seront utiles
                # pour la détection de collision

                newvalues = collision(self, self.coords, newvalues, self.time_step, np.zeros((3, 2)))  # On appelle
                # ensuite la fonction collision qui donne les vraies nouvelles valeurs de vitesse et position de
                # la balle, après de détection de collision. Le paramètre np.zeros((2,2)) permet d'initialiser la
                # récursion (cf. la fonction collision)

                if newvalues == 'goal_blue':  # Si l'équipe bleue marque, on appelle la fonction goal avec comme
                    # paramètre l'équipe bleue
                    self.goal(self.terrain.goal_blue)
                elif newvalues == 'goal_red':  # Idem pour rouge
                    self.goal(self.terrain.goal_red)
                else:  # Si il n'y a pas de but, on met à jour les coordonées et la vitesse de la balle à l'aide des
                    # valeurs calculées par la fonction collision
                    self.coords = np.array(newvalues[0:2])
                    self.velocity = np.array(newvalues[2:4])

            self.col_radius = (self.velocity[0] ** 2 + self.velocity[1] ** 2) ** (
                    1 / 2) * self.time_step  # On met à jour le rayon de détection de collision

        elif self.just_caught:  # Si un joueur vient juste d'attrapper la balle, on replace la balle devant celui-ci,
            # en direction des cages de l'adversaire
            if self.possessing_player.team == 'red':
                self.coords = np.array(
                    [self.possessing_player.pos_bar - self.player_length / 1.99, self.possessing_player.pos_player])
                # Le coefficient 1.99 sert à placer la balle juste devant joueur (en dehors de celui-ci)
            elif self.possessing_player.team == "blue":
                self.coords = np.array(
                    [self.possessing_player.pos_bar + self.player_length / 1.99, self.possessing_player.pos_player])
            self.velocity = np.array([0, self.possessing_player.bar.speed])  # On définit la vitesse de la balle sur la
            # vitesse de la barre du joueur la possédant

            self.just_caught = False

        elif self.released:  # Si le joueur relâche la balle, on donne à la balle une impulsion faible vers l'avant du
            # joueur. La balle conserve la vitesse acquise par le déplacement du joueur
            if self.possessing_player.team == 'red':
                self.coords = np.array(
                    [self.possessing_player.pos_bar - self.player_length / 1.99, self.possessing_player.pos_player])
                self.velocity[0] = -0.15 * self.forward_kick_speed  # On donne une vitesse à la balle égale à 15% de
                # celle de la vitesse donnée lors d'une frappe
            elif self.possessing_player.team == "blue":
                self.coords = np.array(
                    [self.possessing_player.pos_bar + self.player_length / 1.99, self.possessing_player.pos_player])
                self.velocity[0] = 0.15 * self.forward_kick_speed

            self.is_caught = False
            self.released = False
            self.possessing_player = None

        elif self.forward_kick:  # Si l'utilisateur frappe dans la balle, on relâche la balle avec une forte impulsion
            # vers  l'avant du joueur. La balle conserve la vitesse acquise par le déplacement du joueur
            if self.possessing_player.team == 'red':
                self.velocity[0] = -self.forward_kick_speed
            elif self.possessing_player.team == "blue":
                self.velocity[0] = self.forward_kick_speed

            self.is_caught = False
            self.forward_kick = False
            self.possessing_player = None

        else:  # Dans le cas où un joueur est en possession de la balle et que l'utilisateur ne la relâche pas d'une
            # faço ou d'une autre, la balle suit le joueur. Sa vitesse est de même calquée sur celle du joueur
            if self.possessing_player.team == 'red':
                self.coords = np.array(
                    [self.possessing_player.pos_bar - self.player_length / 1.99, self.possessing_player.pos_player])
                self.velocity = np.array([0, self.possessing_player.bar.speed * self.team_red_state])
            else:
                self.coords = np.array(
                    [self.possessing_player.pos_bar + self.player_length / 1.99, self.possessing_player.pos_player])
                self.velocity = np.array([0, self.possessing_player.bar.speed * self.team_blue_state])

    def player_catch_detection(self, team):
        """ Cette méthode est appelée au moment où l'utlisateur essaye d'attraper la balle à l'aide de Shift ou Tab.
        Elle valide ou non la tentative de récupération de balle. Si il y a validation, l'état des variables just_caught
        , is_caught et possessing_player est mis à jour """

        if team == 'red':  # On définit la liste des barres à vérifier selon la couleur de l'utilisateur tentant
            # d'attrapper la balle
            bars = self.terrain.team_red_bars
        else:
            bars = self.terrain.team_blue_bars

        for bar in bars:  # On parcourt les quatres barres de l'équipe
            for player in bar:  # Pour chaque joueur d'une barre, on vérifie si la balle se situe à une distance du
                # joueur inférieure à la largeur du joueur multipliée par un coefficient catch_radius. Plus ce
                # coefficient est élevé, plus il est facile d'attrapper la balle
                if distance(self.coords, (player.pos_bar, player.pos_player)) < 1 / self.catch_radius * self.player_length:
                    self.is_caught = True
                    self.is_caught = True
                    self.just_caught = True
                    self.possessing_player = player

    def goal(self, goal):
        """Méthode appelée en cas de but modifiant quelques variables d'état et appelant reset_ball pour remettre la
        balle au point central

        :param goal: une surface correspondant à un des deux buts
        :type goal: array numpy"""

        if goal[0, 0] == 0:  # Si on se trouve sur le but de gauche...
            self.stat.score("right")  # Modification du score de droite
            self.stat.right_just_scored = True
        else:
            self.stat.score("left")
            self.stat.left_just_scored = True

    # On remet la balle au centre

    def reset_ball(self):
        """Méthode remettant en jeu la balle en la faisant partir du milieu de terrain dans une direction aléatoire
        La valeur aléatoire pour chacune des vitesses est un choix aléatoire entre une valeur alétoire gaussienne
        centrée en 1 et une valeur alétoire gaussienne centrée en -1
        """
        self.coords = self.default_coords
        self.velocity = self.initial_speed * np.array(
            [choice((gauss(1, 1), -gauss(1, 1))), choice((gauss(1, 1), -gauss(1, 1)))])
        print("Mise en jeu")

    def end_game(self):
        """Met fin au jeu"""
        print("Fin du jeu")
        self.stat.reset()

    def dessinImage(self, qp, qpoint, width, length, x, y):
        """Méthode dessinant l'image de la balle à l'aide de QImage"""
        xcoord = int(self.coords[0] / self.terrain.length * length + x)  # Calcul de l'abcisse de l'objet sur la
        # fenêtre. On multiplie la coordonée par le rapport entre la longeur du terrain et la largeur du widget de
        # l'IHM. On translate ensuite le résultat pour que les deux soient bien alignés.
        ycoord = int(self.coords[1] / self.terrain.width * width + y)  # Idem pour l'ordonnée
        qpoint.setX(xcoord)
        qpoint.setY(ycoord)
        qp.drawImage(qpoint, Ball.image)

    def draw(self, qp, width, length, x, y):
        """Méthode faisant appel à l'ensemble des méthodes dessinImage définies dans chacune des instances de Player,
        Bar, Ball et Terrain pour dessiner leurs images respectives."""
        self.terrain.dessinImage(qp, self.qpoint, x, y)
        self.dessinImage(qp, self.qpoint, width, length, x, y)
        for bar in self.terrain.bars:
            bar.dessinImage(qp, self.qpoint, length, x)
            for player in bar:
                player.dessinImage(qp, self.qpoint, width, length, x, y)
