# -*- coding: utf-8 -*-

from player import Player
from PyQt5 import QtGui
import os

__author__ = "Sacha HIRSCH"

class Bar(list):
    """Classe définissant une barre de joueur. On fait hériter la classe Bar de list, pour pouvoir itérer sur une barre
    aisément. Les élements de Bar seront des objets de type Player, et correspondront aux joueurs sur cette barre. Une
    barre a comme paramètres d'entrée son abcisse (pos), son numéro (number), son nombre de joueurs (nbr_players) et
    l'équipe de ses joueurs (team)"""

    image = QtGui.QImage(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'Assets/Images/barV3.png'))  # Définition de l'image associée aux barres

    def __init__(self, pos, number, nbr_players, team):

        super().__init__()

        f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameters.cfg"), 'r')  # On ouvre le fichier
        # parameters contenant les paramètres de jeu (modifié en amont pour moduler la difficulté)
        param = f.readlines()
        f.close()

        self.ref_speed = float(param[2].split('\t')[2])  # Vitesse de référence de l'ensemble des barres (m/s)
        self.width = float(param[1].split('\t')[2])  # Largeur du terrain (m)
        self.length = float(param[0].split('\t')[2])  # longueur du terrain (m)
        self.player_width = float(param[3].split('\t')[2])  # Largeur d'un joueur (m)
        self.player_length = float(param[4].split('\t')[2])
        self.bar_gap = self.length / 8  # Espace entre deux barres (m)
        self.pos = pos  # abscisse de la barre (m)
        self.number = number  # Numéro de la barre
        self.nbr_players = nbr_players  # Nombre de joueurs sur la barre
        self.team = team  # Equipe des joueurs de la barre
        self.speed = self.ref_speed / (self.nbr_players + 1)  # Vitesse de la barre (dépend de la barre) (m/s)
        self.time_step = float(param[5].split('\t')[2])  # Pas de temps
        self.center_pos = self.width / 2  # ordonnée du centre de la barre (initialisée à la moitié de la largeur)
        self.player_gap = self.width / (
                self.nbr_players + 1)  # écartement des joueurs (calculé à partir de la largeur du terrain et du
        # nombre de joueur sur la barre)

        # On ajoute les joueurs sur la barre

        for k in range(self.nbr_players):
            self.append(Player(self.team, self, (k + 1) * self.player_gap, self.pos))

    def bar_move(self, coef, coords):
        """Fonction modifiant la position de la barre et de ses joueurs, et calculant et renvoyant de paramètres de
        collision si collision il y a

        :param coef: coefficient pouvant prendre comme valeurs 0, 1 ou -1 selon la direction de déplacement voulue par
        l'utilisateur
        :type coef: float
        :param coords: coordonées de la balle
        :type coords: array numpy


        :returns kick_direction: Peut prendre les valeurs "high", "low" ou "None" selon si une collision est détectée lors du
        mouvement ou non
        :returns newcoords: Nouvelles coordonées de la balle après collision. S'il n'y a pas collision, vaut None.
         """
        kick_direction_final = None # Sens de l'éventuelle collision entre un joueur de la barre et la balle
        newcoords_final = None  # Nouvelles coordonnées de la balle après cette collision

        delta_motion = self.speed * self.time_step * coef  # Calcul du déplacement de la barre (et de ses joueurs)
        # entre t et t+dt. Coef vaut -1, 0 ou 1, selon le sens de déplacement voulu de la barre
        if not ((
                        coef > 0 and self.center_pos + delta_motion + self.player_length / 2 >= self.player_gap +
                        self.width / 1.8) or (
                        coef < 0 and self.center_pos - delta_motion - self.player_length / 2 <= -self.player_gap +
                        self.width / 2)):  # si on est pas aux limites du mouvement de la barre
            for player in self:  # On parcours les joueurs de la barre
                kick_direction, newcoords = player.player_move(delta_motion, coords)  # On fait bouger chaque joueur. On
                # récupère les coordonées de la balle après collision (la plupart du temps None) et la direction de la
                # collision
                if kick_direction is not None:  # Si un joueur a frappé la balle dans son déplacement...
                    kick_direction_final = kick_direction  # ...on sauvegarde les paramètres de sa frappe, pour plus
                    # tard les renvoyer
                    newcoords_final = newcoords

            self.center_pos += delta_motion  # On bouge le centre de la barre

        return kick_direction_final, self.speed * coef, newcoords_final

    def dessinImage(self, qp, qpoint, length, x):
        """Méthode dessinant l'image de la barre à l'aide de QImage. Celle ci ne bougera pas de la partie"""
        xcoord = int(self.pos / self.length * length + x - 25)
        ycoord = 0
        qpoint.setX(xcoord)
        qpoint.setY(ycoord)
        qp.drawImage(qpoint, Bar.image)
