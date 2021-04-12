# -*- coding: utf-8 -*-

__author__ = 'Inès BENITO'

class Stat:
    """Classe définissant un objet créé au même moment qu'une Ball, sauvegardant les données de la partie en cours.
    Orginellement prévue pour sauvegarder de très nombreux paramètres, par manque de temps elle ne sauvegarde que ceux
    essentiels au jeu (les scores des équipes) et incrémente les scores en cas de but"""

    def __init__(self):
        self.score_left = 0
        self.left_just_scored = False
        self.score_right = 0
        self.right_just_scored = False
        self.score_max = 0

    def score(self, side):
        """Incrémentation des scores en cas de but
        :param side: Côté ayant marqué un but
        :type side: str"""
        if side == "left":
            self.score_left += 1
        if side == "right":
            self.score_right += 1
        self.score_max = max(self.score_left, self.score_right)  # Mise à jour du plus haut score entre les deux équipes

    def reset(self):
        """Remise à zéro des données"""
        self.score_left = 0
        self.score_right = 0

