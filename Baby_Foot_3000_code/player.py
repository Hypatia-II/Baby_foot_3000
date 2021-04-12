# -*- coding: utf-8 -*-

__author__ = "Sacha HIRSCH"

import numpy as np
from physics_engine import Sym
from PyQt5 import QtGui
import os


class Player: #Author : Sacha HIRSCH
    """Classe définissant un joueur, caractérisé par son équipe, sa position et sa barre. Chaque joueur contient quatre
    surfaces, qui délimitent un rectangle définissant sa "hitbox". Ce sont ces surfaces qui vont être déplacées par
    l'utilisateur. Ce déplacement est réalisé par la fonction player_move; cependant ce n'est pas sa seule utilité :
    puisque se déplacent à la fois la balle et les joueurs, il faut aussi effectuer une detection de
    collision lorsque les joueurs se déplacent, en plus de la détection de collision classique physics_engine.collision
    Ce rôle revient donc à la fonction player_move, qui réalise une détection de collision simplifiée entre une surface
    horizontale en mouvement (le haut ou le bas du joueur) et un point (la balle). En cas de collision, une nouvelle
    position et vitesse est calculée par cette même fonction.
    """
    image_team_blue = QtGui.QImage(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                'Assets/Images/player_b.png'))
    # Définition de l'image associée aux joueurs (team bleue)
    image_team_red = QtGui.QImage(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                               'Assets/Images/player_r.png'))
    # Définition de l'image associée aux joueurs (team rouge )

    def __init__(self, team, bar, pos_player, pos_bar):
        f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameters.cfg"), 'r')
        # On ouvre le fichier parameters contenant les paramètres de jeu (modifié en
        # amont pour moduler la difficulté)
        param = f.readlines()
        f.close()

        self.team = team  # Equipe du joueur
        self.bar = bar  # Barre du joueur
        self.pos_player = pos_player  # Ordonnée du joueur
        self.pos_bar = pos_bar  # Abscisse du joueur

        player_width = float(param[3].split('\t')[2])  # Largeur du joueur (m)
        player_length = float(param[4].split('\t')[2])  # Longueur du joueur (m)

        self.up_boundary = np.array([[-player_length / 2 + pos_bar, player_width / 2 + pos_player],  # Limite haute
                                     [player_length / 2 + pos_bar, player_width / 2 + pos_player], [3, 3]])  # du joueur
        self.right_boundary = np.array([[player_length / 2 + pos_bar, player_width / 2 + pos_player],  # Limite droite
                                        [player_length / 2 + pos_bar, -player_width / 2 + pos_player], [2, 2]])
        self.down_boundary = np.array([[player_length / 2 + pos_bar, -player_width / 2 + pos_player],  # Limite basse
                                       [-player_length / 2 + pos_bar, -player_width / 2 + pos_player], [3, 3]])
        self.left_boundary = np.array([[-player_length / 2 + pos_bar, -player_width / 2 + pos_player],  # Limite gauche
                                       [-player_length / 2 + pos_bar, player_width / 2 + pos_player], [2, 2]])

        self.boundaries = (self.up_boundary, self.right_boundary, self.down_boundary, self.left_boundary)  # Liste des
        # limites
        self.time_step = float(param[5].split('\t')[2])  # Pas temporel

    def player_move(self, delta_motion, coords):
        """Fonction modifiant l'ordonnée des surfaces définissant le joueur ainsi que son ordonnée pos_player suivant
        les mouvements imposés par sa barre. Detecte au passage une éventuelle collision avec la balle. Calcule en
        conséquence les nouvelles coordonnées de celle-ci.

        :param delta_motion: déplacement de la barre
        :type delta_motion : float
        :param coords: coordonnées de la balle (utile pour la détection de collision)
        :type coords : array numpy

        :returns kick_direction: Peut prendre les valeurs "high", "low" ou "None" selon si une collision est détectée lors du
        mouvement ou non.
        :returns newcoords: Nouvelles coordonées de la balle après collision. S'il n'y a pas collision, vaut None."""

        kick_side = None
        newcoords = None
        self.pos_player += delta_motion  # Mise à jour de l'ordonnée du joueur
        for boundary in self.boundaries:  # Mise à jour de l'ordonnée de ses surfaces limites
            boundary[0, 1] += delta_motion
            boundary[1, 1] += delta_motion

        if self.up_boundary[0, 0] < coords[0] < self.up_boundary[1, 0]:  # La balle est-elle à l'abscisse de la barre?

            if (self.up_boundary[0, 1] > coords[1] > self.up_boundary[0, 1] - delta_motion) or (  # Il y a-til collision
                    # avec le haut du joueur?
                    self.up_boundary[0, 1] < coords[1] < self.up_boundary[0, 1] - delta_motion):

                kick_side = "high"  # Définition du sens de la frappe
                newcoords = Sym(self.boundaries[0][0], self.boundaries[0][1],
                                coords)  # Calcul des nouvelles coordonées de la balle

                # Si la balle est coincée entre le joueur et le bord, on la téléporte à côté du joueur
                if newcoords[1] > self.bar.width - delta_motion:
                    if self.bar.team == 'red':
                        newcoords[0] += -self.bar.player_length
                    else:
                        newcoords[0] += self.bar.player_length
                    newcoords[1] = self.pos_player

            if (self.down_boundary[0, 1] > coords[1] > self.down_boundary[0, 1] - delta_motion) or (  # Idem si frappe
                    # vers le bas
                    self.down_boundary[0, 1] < coords[1] < self.down_boundary[0, 1] - delta_motion):

                kick_side = "low"
                newcoords = Sym(self.boundaries[2][0], self.boundaries[2][1], coords)

                if newcoords[1] < delta_motion:
                    if self.bar.team == 'red':
                        newcoords[0] += -self.bar.player_length
                    else:
                        newcoords[0] += self.bar.player_length
                    newcoords[1] = self.pos_player

        return kick_side, newcoords

    def dessinImage(self, qp, qpoint, width, length, x, y):
        """Méthode dessinant l'image du joueur à l'aide de QImage. L'image change selon l'équipe du joueur"""
        xcoord = int(self.bar.pos / self.bar.length * length + x)
        ycoord = int(self.pos_player / self.bar.width * width + y)
        qpoint.setX(xcoord)
        qpoint.setY(ycoord)
        if self.team == 'blue':
            qp.drawImage(qpoint, Player.image_team_blue)
        else:
            qp.drawImage(qpoint, Player.image_team_red)
