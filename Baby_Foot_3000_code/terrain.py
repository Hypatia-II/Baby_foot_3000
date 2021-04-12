# -*- coding: utf-8 -*-

__author__ = "Inès BENITO"

import numpy as np
from bar import Bar
from PyQt5 import QtGui
import os


class Terrain:
    """Classe définissant un objet ) partir duquel il est possible d'accéder l'ensemble des surfaces. Il contient les
    du terrain, les lignes de buts mais aussi une fonction surfaces qui va parcourir l'ensemble des barres et renvoyer
    les surfaces des joueurs contenus dans celles-ci."""

    image = QtGui.QImage(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain.png"))
    # Définition de l'image associé au terrain

    def __init__(self):

        f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameters.cfg"), 'r')  # On ouvre le
        # fichier parameters contenant les paramètres de jeu (modifié en amont pour moduler la difficulté)
        param = f.readlines()
        f.close()

        self.length = float(param[0].split('\t')[2])  # Longueur du terrain (m)
        self.width = float(param[1].split('\t')[2])  # Largeur du terrain (m)
        self.goal_up_limit = float(param[12].split('\t')[2])
        self.goal_down_limit = float(param[13].split('\t')[2])

        e = 10 ** (-12)  # Definition d'un epsilon pour ne pas créer des parois parfaitement verticales

        # Création des huit barres du terrain

        b1 = Bar(self.length / 7 * 0 + self.length / 25, 1, 1, 'blue')
        b2 = Bar(self.length / 7 * 1, 2, 2, 'blue')
        b3 = Bar(self.length / 7 * 2, 3, 3, 'red')
        b4 = Bar(self.length / 7 * 3, 4, 5, 'blue')
        b5 = Bar(self.length / 7 * 4, 5, 5, 'red')
        b6 = Bar(self.length / 7 * 5, 6, 3, 'blue')
        b7 = Bar(self.length / 7 * 6, 7, 2, 'red')
        b8 = Bar(self.length / 7 * 7 - self.length / 25, 8, 1, 'red')
        self.bars = (b1, b2, b3, b4, b5, b6, b7, b8)
        self.team_blue_bars = (b1, b2, b4, b6)
        self.team_red_bars = (b3, b5, b7, b8)

        # Définition des buts

        self.goal_blue = np.array([[0, self.goal_down_limit],
                                   [0 + e, self.goal_up_limit],
                                   [0, 0]])
        self.goal_red = np.array([[self.length + e, self.goal_down_limit],
                                  [self.length + e, self.goal_up_limit], [0, 0]])

        # Définition des limites du terrain

        self.limit_up = np.array([[0, self.width + e],
                                  [self.length + e, self.width], [1, 1]])
        self.limit_down = np.array([[0 + e, 0 - e],
                                    [self.length, 0], [1, 1]])
        self.limit_right_up = np.array([[self.length + e, self.width],
                                        [self.length - e, self.goal_up_limit], [1, 1]])
        self.limit_right_down = np.array([[self.length + e, self.goal_down_limit],
                                          [self.length - e, 0 - e], [1, 1]])
        self.limit_left_up = np.array([[0, self.goal_up_limit],
                                       [0 + e, self.width], [1, 1]])
        self.limit_left_down = np.array([[0 - e, 0],
                                         [0, self.goal_down_limit], [1, 1]])
        self.limits = (self.limit_down, self.limit_up, self.limit_left_down, self.limit_left_up, self.limit_right_down,
                       self.limit_right_up)  # liste d'arrays

    def surfaces(self, ball):
        """Fonction renvoyant la liste des surfaces pouvant entrer en collision avec la balle. Renvoie les
        limites du terrain et les limites des joueurs se situant sur des barres dont l'abscisse est comprise dans un
        cercle de rayon ball.col_radius et de centre balle

        :param ball: La balle
        :type ball: Ball
        :return: Liste des surfaces atteignables par la balle
        :rtype: liste d'arrays numpys"""

        list_surf = list(self.limits)  # ajout des limites du terrain

        for bar in self.bars:  # ajout des limites des "player" à portée
            if ball.coords[0] + ball.col_radius + bar.player_width > bar.pos > ball.coords[0] - ball.col_radius \
                    - bar.player_width:
                for player in bar:
                    for k in range(4):
                        list_surf.append(player.boundaries[k])
        return list_surf

    def goals(self):
        """Fonction retournant les deux buts
        :return: Liste d'arrays numpy"""
        return [self.goal_blue, self.goal_red]

    def dessinImage(self, qp, qpoint, x, y):
        """Méthode dessinant l'image du terrain à l'aide de QImage"""
        qpoint.setX(x + 13)  # Recalage de l'image du terrain (dimension : pixel)
        qpoint.setY(y + 5)
        qp.drawImage(qpoint, Terrain.image)
