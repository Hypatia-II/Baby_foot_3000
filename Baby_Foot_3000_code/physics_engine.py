# -*- coding: utf-8 -*-

"""physics_engine.py : Ensemble de fonctions utiles au calcul du mouvement de la balle et des collisions"""
__author__ = "Sacha HIRSCH"

import numpy as np
from random import choice


def norme(u):
    """norme d'un vecteur
    vecteur unitaire
    :param u: Vecteur quelconque
    :type u: array numpy
    :return: La norme de ce vecteur
    :rtype: float"""
    return np.sqrt(u[0] * u[0] + u[1] * u[1])


def det(u, v):
    """déterminant
    param u: Vecteur
    :type u: array numpy
    :param v: Vecteur
    :type v: array numpy
    :return: le déterminant deux vecteurs
    :rtype: float"""
    return u[0] * v[1] - u[1] * v[0]


def produit(u, v):
    """produit scalaire
    :param u: Vecteur
    :type u: array numpy
    :param v: Vecteur
    :type v: array numpy
    :return: le produit scalaire des deux vecteurs
    :rtype: float"""

    return u[0] * v[0] + u[1] * v[1]


def unitaire(u):
    """vecteur unitaire
    :param u: Vecteur quelconque
    :type u: array numpy
    :return: Le vecteur unitaire correspondant
    :rtype: array numpy"""
    return u[0] / norme(u), u[1] / norme(u)


def Sym(A, B, P):
    """Calcul du symétrique du point P par rapport à la droite (AB), perpendiculaire à la surface atteinte en I
    :param A: Premier point de l'axe de symétrie
    :type: array numpy
    :param B: Second point de l'axe de symétrie
    :type B: array numpy
    :return: Le symétrique
    :rtype: array numpy
    """
    V = (B[0] - A[0], B[1] - A[1])
    U = (P[0] - A[0], P[1] - A[1])
    u = unitaire(U)
    v = unitaire(V)
    cost = produit(u, v)
    sint = det(u, v)
    cos2t = cost * cost - sint * sint  # trigo
    sin2t = 2 * sint * cost  # trigo
    return np.array([cos2t * U[0] - sin2t * U[1] + A[0], sin2t * U[0] + cos2t * U[1] + A[1]])


def distance(A, B):
    """Calcul de la distance entre deux points"""
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** (1 / 2)


def geom_compute(surf, coords, simulated):
    """Fonction réalisant différents calculs géométriques. Les valeurs retournées seront utilisées par la fonction
    collision
    :param surf: surface à tester
    :type surf: array numpy
    :param coords: coordonnées et vitesses actuelles de la balle
    :type coords: array numpy
    :param simulated: coordonnées et vitesses prédites de la balle
    :type simulated: array numpy
    :return: Valeurs calculées (cf. la fonction collision)
    :rtype: tuple
    """
    if surf[0, 0] == surf[1, 0]:
        surf[1, 0] += 10 ** -12
    if coords[0] == simulated[0]:
        simulated[0] += 10 ** -12
    a1 = (surf[0, 1] - surf[1, 1]) / (surf[0, 0] - surf[1, 0])  # calcul du coef directeur de la surface
    a2 = (coords[1] - simulated[1]) / (coords[0] - simulated[0])  # calcul du coef directeur de la trajectoire
    b1 = surf[1, 1] - a1 * surf[1, 0]  # ordonnée à l'orgine de la surface
    b2 = simulated[1] - a2 * simulated[0]  # ordonnée à l'origine de la trajectoire

    if a2 == a1:
        a1 += 10 ** -12
    xi = -(b2 - b1) / (
            a2 - a1)  # calcul du point d'intersection des deux droites (on cherche (xi, yi) tq a1*xi + b1 = a2*xi + b2 et yi = a1*xi+b1)
    yi = a1 * xi + b1

    d1 = distance(simulated, coords)  # d1 : distance entre deux points consecutifs
    d2 = distance((xi, yi), coords)  # d2 : distance entre le point k-1 et le point d'intersection

    return a1, a2, b1, b2, xi, yi, d1, d2


def euler(ball):
    """"Fonction calculant les nouvelles positions et vitesses cartésiennes de la balle en ignorant toute
    potentielle collision
    :param ball: la balle
    :type ball: Ball
    :return: Les valeurs calculées
    :rtype: tuple"""
    newvx = ball.velocity[0] * ball.drag
    newvy = ball.velocity[1] * ball.drag  # La nouvelle vitesse est légèrement inférieure à la vitesse précédente
    # pour prendre en compte les frottements
    newxp = ball.coords[0] + newvx * ball.time_step
    newyp = ball.coords[1] + newvy * ball.time_step  # La nouvelle position est calculée grâce à une méthode d'Euler
    # (correspondant exactement à la réalité physique dans notre cas)

    return newxp, newyp, newvx, newvy


def collision(ball, current_pos, simulated, time_step, just_detected):
    """Fonction récursive renvoyant les nouvelles positions et vitesses cartésiennes de la balle en prenant en
    compte les collisions. La récursion se fait sur les surfaces collisionnées à la suite dans un seul pas de temps.
    La condition d'arrêt est l'absence de surfaces sur la trajectoire de la balle.

    :param ball: la balle
    :type ball: Ball
    :param current_pos: est la position actuelle de la balle (inialisées avec les valeurs du pas en cours)
    :type current_pos: array numpy
    :param simulated: est la position et vitesse de la balle prédite (initialisées avec la fonction Euler)
    :type simulated: array numpy
    :param time_step: est le temps restant avant la fin du pas de temps (initialisé à la durée nominale d'un pas de temps)
    :type time_step: float
    :param just_detected: est la surface venant d'être collisionnée (initalisée à une surface "nulle")
    :type just_detected: array numpy
    :return: Nouvelle position et vitesse de la balle (à la fin de la récursion)
    :rtype: simulated
    """

    surfaces_intersected = []  # On initialise la liste des surfaces avec lesquelles il y a collision

    for surface in ball.terrain.surfaces(ball):  # A chaque profondeur de récursion, on parcourt la liste des
        # surfaces renvoyées par terrain.surfaces

        values = geom_compute(surface, current_pos, simulated)  # Calcul de différentes valeurs géométriques utiles
        # pour la détection de collision et le calcul du rebond. Les valeurs sont les suivantes :
        # values[0] : a1 coef directeur de la surface
        # values[1] : a2 coef directeur de la trajectoire
        # values[2] : b1 ordonnée à l'orgine de la surface
        # values[3] : b2 ordonnée à l'origine de la trajectoire
        # values[4] : xi abscisse de l'intersection des droites portées par la trajectoire et la surface
        # values[5] : yi ordonnée de l'intersection des droites portées par la trajectoire et la surface
        # values[6] : d1 distance entre deux positions consecutives de la balle
        # values[7] : d2 distance entre l'ancienne position de la balle et l'intersection des droites trajectoire et
        # surface

        # On teste ensuite s'il y a effectivement collision

        # On veut tout d'abord d2<d1
        if values[7] < values[6] and (
                # On teste ensuite si le point d'intersection se situe sur la surface
                surface[0, 0] <= values[4] <= surface[1, 0] or surface[0, 0] >= values[4] >= surface[1, 0]) and (
                surface[0, 1] <= values[5] <= surface[1, 1] or surface[0, 1] >= values[5] >= surface[1, 1]) and not (
                # On teste ensuite si le point de collision ne trouve pas dans le sens inverse du celui de la
                # trajectoire de la balle
                (simulated[0] >= current_pos[0] >= values[4] or simulated[0] <= current_pos[0] <= values[4]) and
                (simulated[1] >= current_pos[1] >= values[5] or simulated[1] <= current_pos[1] <= values[5])) and not (
                # Et enfin on ne veut pas détecter une collision avec la surface colisionnée à la profondeur de
                # récursion précédente. En effet, à ce stade la balle est situeé sur cette surface, il y donc risque
                # de la détecter à nouveau
                np.array_equal(surface, just_detected)):

            # On calcule le symétrique de la position de la balle simulée par Euler par rapport à la surface
            # collisionée
            coordsym = Sym([surface[0, 0], surface[0, 1]], [surface[1, 0], surface[1, 1]], [simulated[0],
                                                                                            simulated[1]])

            # On calcule le temps restant à la balle pour se déplacer dans le pas de temps actuel
            dt = time_step * (values[6] - values[7]) / values[6]

            surface_boost = 1
            div = 0
            if surface[2, 0] == 2:  # Si la surface est une surface latérale de joueur, le rebond est quasi-parfait
                surface_boost = 0.9

            if surface[2, 0] == 1:  # Si la surface est un bord de terrain, il y a dissipation d'énergie, la vitesse
                # en sortie est divisée par 2
                surface_boost = 0.5

            if surface[2, 0] == 3:  # Si la surface est une surface costale du joueur, il y a dissipation d'énergie,
                # la vitesse en sortie est divisée par 4 et une vitesse latérale aléatoire est donnée pour évacuer
                # la balle
                div = choice((-ball.player_length / 500,
                              ball.player_length / 500)) / dt * ball.velocity[1]  # On ajoute une légère vitesse
                # horizontale pour éviter que la balle rebondisse indéfniment entre
                # deux joueurs côte à côte
                surface_boost = 0.25

            # Calcul final des nouvelles vitesses. bounce_bonus sert à moduler globalement la puissance du rebond
            newvx = (ball.bounce_bonus * surface_boost * (coordsym[0] - values[4])) / dt + div
            newvy = (ball.bounce_bonus * surface_boost * (coordsym[1] - values[5])) / dt

            # On ajoute la surface collisionnée à la liste des surface avec lesquelles il y a collision, ainsi
            # ainsi que les paramètres calculés s'y attachant
            surfaces_intersected.append(
                (values[7], (values[4], values[5]), (coordsym[0], coordsym[1], newvx, newvy), dt, surface))

    # On vérifie ensuite si un but a été marqué, par une détection de collision similaire à celle effectuée plus
    # tôt, cette fois ci avec les surfaces correspondant aux buts. S'il y a collision avec l'une des deux cages, on
    # met immédiatement fin à la récursion et on renvoie une valeur spéciale "goal_blue" ou "goal_red"

    for goal in ball.terrain.goals():
        values_goal = geom_compute(goal, ball.coords, simulated)
        if values_goal[7] < values_goal[6] and (
                goal[0, 0] <= values_goal[4] <= goal[1, 0] or goal[0, 0] >= values_goal[4] >= goal[1, 0]) and (
                goal[0, 1] <= values_goal[5] <= goal[1, 1] or goal[0, 1] >= values_goal[5] >= goal[1, 1]):
            if np.array_equal(goal, ball.terrain.goal_blue):
                return 'goal_blue'
            else:
                return 'goal_red'

    if len(surfaces_intersected) != 0:  # Si la liste des surfaces collisionnées n'est pas vide,
        # on sélectionne la surface la plus proche de la position actuelle de la balle de toutes les surfaces
        # collisionnées. Pour cela, on les trie suivant la distance d2

        surfaces_intersected.sort()

        # On descend ensuite d'un cran dans la récursion, avec comme nouveaux paramètres d'entrée :
        # - Le point d'intersection comme position actuelle de la balle
        # - La position après rebond comme position simulée
        # - le temps dt restant
        # - la surface venant d'être collisionée
        print()
        return collision(ball, surfaces_intersected[0][1], surfaces_intersected[0][2], surfaces_intersected[0][3],
                         surfaces_intersected[0][4])

    # Si la liste des surfaces collisionnées est vide, on renvoie les positions et vitesses prédites sans collision

    return simulated
