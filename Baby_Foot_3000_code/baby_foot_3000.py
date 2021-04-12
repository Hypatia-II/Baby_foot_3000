# -*- coding: utf-8 -*-

"""baby_foot_3000.py : Fichier à executer pour lancer le jeu regroupant l'ensemble des classes gérant l'IHM. """
__author__ = "Inès BENITO (FirstWindow, WindowSettingsUI, WindowCreditsUI, WindowHelpUI) & Sacha HIRSCH (WindowGameUI)"

import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from interface_baby_welcome import Ui_Principale_ihm
import interface_baby_settings
import interface_baby_credits
import interface_baby_help
import interface_game
from terrain import Terrain
from shutil import copyfile
from ball import Ball
from time import time
from random import randint
import os
import ctypes


class FirstWindow(QtWidgets.QMainWindow):
    """ Classe qui permet d'afficher et d'avoir toutes les fonctionnalités de la page d'accueil du jeu """

    def __init__(self):

        super().__init__()  # La classe hérite de QtWidgets
        # Configuration de l'interface utilisateur.
        self.ui = Ui_Principale_ihm()  # Instanciation de la fenêtre principale
        self.ui.setupUi(self)

        myappid = u'enstab.projetinfo.babyfoot.beta'  # Code trouvé sur internet permettant d'afficher l'icône dans la
        # barre des tâches
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.setWindowTitle("Baby-Foot 3000")
        self.setFixedSize(self.size())

        self.playlist = QtMultimedia.QMediaPlaylist()  # Création d'une playlist
        music1 = QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Musics/Coup.mp3")))
        music2 = QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Musics/VEGEDREAM.mp3")))
        music3 = QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Musics/olive.mp3")))
        music4 = QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Musics/waka.mp3")))
        music5 = QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Musics/frog.mp3")))
        music6 = QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Musics/tiger.mp3")))

        musics = [music1, music2, music3, music4, music5, music6]

        for k in range(6):  # Randomisation de l'ordre d'ajout des musiques, pour contourner les problèmes de shuffle()
            music_to_add_index = randint(0, 6-k-1)
            self.playlist.addMedia(musics[music_to_add_index])
            musics.pop(music_to_add_index)

        self.player = QtMultimedia.QMediaPlayer()  # Création d'un lecteur de musique

        self.player_shootings = QtMultimedia.QMediaPlayer()  # Création d'un lecteur pour le bruit de fond de
        # stade de foot lors de la partie de baby-foot

        self.player_shootings.setMedia(QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Sounds/shootings.mp3"))))  # Création
        # d'un lecteur de musique pour le son lorsqu'un but est marqué
        self.player_goal = QtMultimedia.QMediaPlayer()
        self.player_goal.setMedia(QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Sounds/goal.mp3"))))

        self.player.setPlaylist(self.playlist)  # Association de la playlist créée au lecteur de musique
        self.player.setVolume(70)  # Gestion du volume de la musique
        self.player.play()  # La musique est jouée à l'allumage de la fenêtre

        self.ui.NewGameButton.clicked.connect(self.new_game)  # Création d'un lien entre le boutton "New game" et le
        # démarrage d'une partie
        self.ui.SettingsButton.clicked.connect(self.settings)  # Création d'un lien entre le boutton "Settings" et la
        # page des paramètres
        self.ui.CreditsButton.clicked.connect(self.credits)
        self.ui.HelpButton.clicked.connect(self.helpbut)
        self.ui.actionStart_new_game.triggered.connect(self.new_game)  # Création d'un lien entre l'action "New Game" du
        # menu déroulant et le démarrage d'une partie
        self.ui.actionSettings.triggered.connect(self.settings)
        self.ui.actionCredits.triggered.connect(self.credits)
        self.ui.actionHelp.triggered.connect(self.helpbut)
        self.level = 0  # Variable qui mémorise le niveau de difficulté entré par l'utilisateur
        copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Parameters/parameters_easy.cfg"),
                 os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameters.cfg"))
        copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain_easy.png"),
                 os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain.png"))
        Terrain.image = QtGui.QImage(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain.png"))
        self.dialog_settings = WindowSettingsUI(self) # Instanciation de la page de paramètres
        #Initialisation des paramètres de difficulté

    def new_game(self):
        """Méthode qui ouvre la page du jeu et met en route le bruit de fond de stade de foot"""
        self.dialog_game = WindowGameUI(self)  # Instanciation de la page de jeu
        self.dialog_game.show()  # Affichage de la page de jeu
        self.music_state_changed()
        self.sound_state_changed()
        self.player_shootings.setVolume(60)  # Gestion du volume du bruit de stade de foot
        self.player_goal.setVolume(100)

    def new_game_from_settings(self):
        """Méthode qui ouvre la page de jeu lorsque l'on clique sur "New Game" à partir de la page de paramètres.
        Elle ferme la page de paramètres et met en route le son de stade de foot"""

        self.dialog_game = WindowGameUI(self)  # Instanciation de la page de jeu
        self.dialog_settings.close()  # Fermeture de la page de paramètres
        self.dialog_game.show()  # Affichage de la page de jeu
        self.player_shootings.setVolume(60)
        self.player_goal.setVolume(100)
        self.music_state_changed()
        self.sound_state_changed()

    def settings(self):
        """Méthode qui ouvre la la page des paramètres et permet de modifier la difficulté du jeu ainsi que de couper
        ou d'allumer la musique et les effets sonores """
        self.dialog_settings.setWindowTitle("Baby-Foot 3000 - Settings")  # Nommage de la page
        self.dialog_settings.show()  # Affichage de la page de paramètres
        self.dialog_settings.ui.MusicCheckBox.stateChanged.connect(self.music_state_changed)  # Création d'un lien entre
        # la case "Music On" à cocher et la lecture de la playlist
        self.dialog_settings.ui.SoundsCheckBox.stateChanged.connect(
            self.sound_state_changed)  # Création d'un lien entre
        # la case "Sounds On" à cocher et la lecture de la bande sonore de stade foot et du son lorsqu'un but est marqué
        self.dialog_settings.ui.DifficultyComboBox.currentIndexChanged.connect(
            self.difficulty)  # Création d'un lien entre
        # les cases de niveaux de difficulté et la difficulté du jeu

    def music_state_changed(self):
        """Méthode permettant d'allumer ou d'éteindre la musique lorsque la case est cochée ou décochée dans la page
        des paramètres """

        if self.dialog_settings.ui.MusicCheckBox.isChecked():  # Si la case "Music On" est cochée, on lit les musiques
            # de la playlist, sinon on éteint la musique
            self.player.play()
        else:
            self.player.pause()

    def sound_state_changed(self):
        """Méthode permettant d'allumer ou d'éteindre les effets sonores lorsque la case est cochée ou décochée dans la
        page des paramètres """

        if self.dialog_settings.ui.SoundsCheckBox.isChecked():  # Si la case "Sounds On" est cochée, on joue le bruit de
            # fond de stade de foot et on met le bruit de but, sinon on les éteint
            self.player_shootings.play()
            self.player_goal.setMuted(False)
        else:
            self.player_shootings.pause()
            self.player_goal.setMuted(True)

    def difficulty(self):
        """Méthode permettant de modifier la difficulté du jeu"""
        if self.dialog_settings.ui.DifficultyComboBox.currentIndex() == 0:
            # on importe le fichier "parameters_easy.cfg" que l'on copie dans le fichier "parameters.cfg"
            copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Parameters/parameters_easy.cfg"),
                     os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameters.cfg"))
            # on importe le fichier "terrain_easy.png" que l'on copie dans le fichier "terrain.png"
            copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain_easy.png"),
                     os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain.png"))
            self.level = 0 # On met à jour la variable du niveau de difficulté

        elif self.dialog_settings.ui.DifficultyComboBox.currentIndex() == 1:  # Si l'utilisateur choisi le niveau
            # "Medium",
            copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Parameters/parameters_medium.cfg"),
                     os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameters.cfg"))
            copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain_medium.png"),
                     os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain.png"))
            self.level = 1

        else:  # Si l'utilisateur choisi le niveau "Hard",
            copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Parameters/parameters_hard.cfg"),
                     os.path.join(os.path.dirname(os.path.abspath(__file__)), "parameters.cfg"))
            copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain_hard.png"),
                     os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain.png"))
            self.level = 2

        Terrain.image = QtGui.QImage(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets/Images/terrain.png"))

    def credits(self):
        """Méthode affichant la page des crédits """

        self.dialog_credits = WindowCreditsUI(self)  # On instancie la page des crédits
        self.dialog_credits.setWindowTitle("Baby-Foot 3000 - Credits")  # Nommage de la page
        self.dialog_credits.show()  # On affiche la fenêtre des crédits

    def helpbut(self):
        """Méthode affichant la page d'aide """

        self.dialog_help = WindowHelpUI(self)  # On instancie la page d'aide
        self.dialog_help.show()  # On affiche la page d'aide

    def end_game(self):
        """Méthode fermant la page de jeu et éteignant les bruits de fond de stade de foot """

        self.dialog_game.close()  # Fermeture de la page de jeu
        self.player_shootings.pause()  # On éteint le fond sonore de stade de foot


class WindowSettingsUI(QtWidgets.QMainWindow):
    """Classe qui permet d'afficher et d'avoir accès à toutes les fonctionnalités de la page des paramètres. Elle prend
    en paramètre la page d'accueil"""

    def __init__(self, welcomeWindow):  # La page d'accueil est un paramètre de cette classe
        super().__init__()
        self.ui = interface_baby_settings.Ui_Principale_ihm()  # On instancie la page des paramètres
        self.ui.setupUi(self)

        self.setWindowTitle("Baby-Foot 3000 - Settings")  # Nommage de la page
        self.setFixedSize(self.size())  # Taille fixée

        if welcomeWindow.level == 0:  # Si le niveau de difficulté entré par l'utilisateur est "Easy", on met le menu
            # déroulant sur la case "Easy"
            self.ui.DifficultyComboBox.setCurrentIndex(0)
        elif welcomeWindow.level == 1:  # Si le niveau de difficulté entré par l'utilisateur est "Medium", on met le
            # menu déroulant sur la case "Medium"
            self.ui.DifficultyComboBox.setCurrentIndex(1)
        else:  # Si le niveau de difficulté entré par l'utilisateur est "Hard", on met le menu
            # déroulant sur la case "Hard"
            self.ui.DifficultyComboBox.setCurrentIndex(2)

        self.ui.actionCredits.triggered.connect(welcomeWindow.credits)  # Création du lien entre l'action "Credits" et
        # l'affichade de la page des crédits
        self.ui.actionHelp.triggered.connect(welcomeWindow.helpbut)  # Création du lien entre l'action "Help" et
        # l'affichage de la page d'aide
        self.ui.actionStart_new_game.triggered.connect(welcomeWindow.new_game_from_settings)  # Création du lien entre
        # l'action "New game" de la page "Settings" et l'affichage de la page de jeu
        self.ui.NewGameButton.clicked.connect(welcomeWindow.new_game_from_settings)  # Création du lien entre
        # le boutton "New game" de la page "Settings" et l'affichage de la page de jeu


class WindowCreditsUI(QtWidgets.QMainWindow):
    """Classe qui permet d'afficher et d'avoir accès à toutes les fonctionnalités de la page des crédits. Elle prend
        en paramètre la page d'accueil"""

    def __init__(self, welcomeWindow):
        super().__init__()

        self.ui = interface_baby_credits.Ui_Principale_ihm()  # On instancie la page des crédits
        self.ui.setupUi(self)

        self.setFixedSize(self.size()) #Taille Fixée
        self.setWindowTitle("Baby-Foot 3000 - Credits")  # Nommage de la page

        self.ui.actionSettings.triggered.connect(
            welcomeWindow.settings)  # Création du lien entre l'action "Settings" et
        # l'affichage de la page des paramètres
        self.ui.actionHelp.triggered.connect(welcomeWindow.helpbut)  # Création du lien entre l'action "Help" et
        # l'affichage de la page d'aide
        self.ui.actionStart_new_game.triggered.connect(welcomeWindow.new_game)  # Création du lien entre l'action
        # "New Game" l'affichage de la page de jeu


class WindowHelpUI(QtWidgets.QMainWindow):
    """Classe qui permet d'afficher et d'avoir accès à toutes les fonctionnalités de la page des crédits. Elle prend
          en paramètre la page d'accueil"""

    def __init__(self, welcomeWindow):
        super().__init__()

        self.ui = interface_baby_help.Ui_Principale_ihm()  # On instancie la page d'aide
        self.ui.setupUi(self)
        self.setFixedSize(self.size()) #Taille Fixée
        self.setWindowTitle("Baby-Foot 3000 - Help")  # Nommage de la page
        self.ui.actionSettings.triggered.connect(
            welcomeWindow.settings)  # Création du lien entre l'action "Settings" et
        # l'affichage de la page des paramètres
        self.ui.actionCredits.triggered.connect(welcomeWindow.credits)  # Création du lien entre l'action "Credits" et
        # l'affichade de la page des crédits
        self.ui.actionStart_new_game.triggered.connect(welcomeWindow.new_game)  # Création du lien entre l'action
        # "New Game" l'affichage de la page de jeu


class WindowGameUI(QtWidgets.QMainWindow):
    """Fenêtre affichant le jeu en lui-même"""

    def __init__(self, welcomeWindow):
        super().__init__()

        self.ui = interface_game.Ui_Principale_ihm()
        self.ui.setupUi(self)
        self.setFixedSize(self.size()) #Taille Fixée
        self.setWindowTitle("Baby-Foot 3000")  # Nommage de la page

        self.ui.actionSettings.triggered.connect(welcomeWindow.settings)  # Bouton Settings
        self.ui.actionCredits.triggered.connect(welcomeWindow.credits)  # Bouton Credits
        self.ui.actionHelp.triggered.connect(welcomeWindow.helpbut)  # Bouton Help
        self.ui.actionStart_new_game.triggered.connect(self.start_game)  # Bonton NewGame
        self.ball = Ball()  # Création d'une instance de Ball
        self.timer = QtCore.QTimer()  # Création du Timer appelant le pas suivant du moteur physique toutes les 1/60 s
        self.timer.timeout.connect(self.one_step)  # Connection du timer au moteur physique
        self.delay = 1  # Temps après lequel un utilisateur peut attraper la balle après l'avoir frappée
        self.last_catch_try_blue = 0  # Date de la dernière tentative d'attrapage de la balle (équipe bleue)
        self.last_catch_try_red = 0  # Idem équipe rouge
        self.welcomeWindow = welcomeWindow  # Fenêtre principale
        self.setChildrenFocusPolicy(QtCore.Qt.NoFocus)  # cf. setChildrenFocusPolicy
        self.countdown_timer = QtCore.QTimer  # Timer pour le compteur 3..2..1..0 avant le début du match/après un but
        self.countdown_state = 3  # Etat du compteur (3, 2,1 ou 0)
        self.reset_type = None  # Type de relance du jeu (après un but ou pour une nouvelle partie)
        self.countdown_ongoing = False  # Etat du compteur (entrain d'être déroulé ou non)

        self.start_game()  # Lancement d'une partie à la fin de l'initialisation

    def closeEvent(self, event):
        """Surcharge de la fonction closeEvent de QWidget. Arrête l'ambiance sonore à la fermeture de l'instance de la
        WindowsGameUI"""
        self.welcomeWindow.player_shootings.pause()

    def keyPressEvent(self, event):
        """Surcharge de la fonction keyPressEvent de QWidget. Elle est automatiquement appelée lorsque l'utilisateur
        appuie sur une touche de clavier. Selon la touche pressée, certaines variables d'état de l'objet ball sont
        modifiées. Ces variables seront lues par les fonctions de l'objet ball, qui modifieront leur comportement en
        conséquence"""

        if event.type() == QtCore.QEvent.KeyPress:
            current_time = time()
            if event.key() == QtCore.Qt.Key_Z:  # Joueurs vers le haut
                self.ball.team_blue_state = -1
            if event.key() == QtCore.Qt.Key_S:  # Joueurs vers le bas
                self.ball.team_blue_state = 1
            if event.key() == QtCore.Qt.Key_A and current_time - self.last_catch_try_blue > self.delay:
                self.ball.player_catch_detection('blue')  # L'utilisateur tente d'attrapper la balle
            if event.key() == QtCore.Qt.Key_Space and self.ball.is_caught and self.ball.possessing_player.team == 'blue':
                self.last_catch_try_blue = current_time
                self.ball.forward_kick = True  # L'utilisateur frappe la balle

            if event.key() == QtCore.Qt.Key_Up:
                self.ball.team_red_state = -1
            if event.key() == QtCore.Qt.Key_Down:
                self.ball.team_red_state = 1
            if event.key() == QtCore.Qt.Key_Shift and current_time - self.last_catch_try_red > self.delay:
                self.ball.player_catch_detection('red')
            if event.key() == QtCore.Qt.Key_Return and self.ball.is_caught and self.ball.possessing_player.team == 'red':
                self.last_catch_try_red = current_time
                self.ball.forward_kick = True

            if event.key() == QtCore.Qt.Key_R:
                self.ball.reset_ball()

    def keyReleaseEvent(self, event):
        """Surcharge de la fonction keyReleaseEvent de QWidget. Elle est automatiquement appelée lorsque l'utilisateur
        relâche une touche de clavier. Selon la touche pressée, certaines variables d'état de l'objet ball sont
        modifiées. Ces variables seront lues par les fonctions de l'objet ball, qui modifieront leur comportement en
        conséquence"""
        if event.type() == QtCore.QEvent.KeyRelease:
            if event.key() == QtCore.Qt.Key_Up:  # Les joueurs arrêtent de bouger
                self.ball.team_red_state = 0
            if event.key() == QtCore.Qt.Key_Down:
                self.ball.team_red_state = 0
            if event.key() == QtCore.Qt.Key_Z:
                self.ball.team_blue_state = 0
            if event.key() == QtCore.Qt.Key_S:
                self.ball.team_blue_state = 0
            if event.key() == QtCore.Qt.Key_A and self.ball.is_caught and self.ball.possessing_player.team == 'blue':
                self.ball.released = True  # La balle est relachée
            if event.key() == QtCore.Qt.Key_Shift and self.ball.is_caught and self.ball.possessing_player.team == 'red':
                self.ball.released = True

    def paintEvent(self, event):
        """Surcharge de la fonction paintEvent de QWidget. Appelée par QWidget.repaint() ou Qwidget.update(), elle
        appelle la fonction draw de l'objet ball, qui va dessiner l'ensemble des images : joueurs, barres, terrain et
        balle à l'aide de l'objet QPainter initialisé au début de paintEvent."""
        self.ui.display.painter = QtGui.QPainter()
        self.ui.display.painter.begin(self)

        self.ball.draw(self.ui.display.painter, self.ui.display.height(), self.ui.display.width(),
                       self.ui.display.pos().x(), self.ui.display.pos().y())
        self.ui.display.painter.end()

    def one_step(self):
        """Méthode ayant pour principale utilité d'appeler la fonction next_step de l'objet ball. A aussi pour rôle
        d'activer certaines fonctions lors d'un but (audio, statistiques, et compte à rebours)"""
        if not self.countdown_ongoing:  # On execute le moteur physique si et seulement si le compteur n'est pas activé
            # (cf. countdown)
            self.ball.next_step()  # Execution d'un pas du motur
            self.ui.Conteneur.update()  # Mise à jour du widget (appelle paintEvent)
            if self.ball.stat.left_just_scored:
                self.ball.stat.left_just_scored = False
                self.welcomeWindow.player_goal.play()
                self.ui.lcdNumber_3.display(self.ball.stat.score_left)  # Mise à jour des scores affichés
                self.ui.lcdNumber_3.repaint()
                if self.ball.stat.score_max == 10:  # Arrêt du jeu
                    self.end_game()
                self.reset_type = 'goal'
                self.countdown()  # Lancement du compte à rebours

            if self.ball.stat.right_just_scored:
                self.ball.stat.right_just_scored = False
                self.welcomeWindow.player_goal.play()
                self.ui.lcdNumber.display(self.ball.stat.score_right)
                self.ui.lcdNumber.repaint()
                if self.ball.stat.score_max == 10:
                    self.end_game()
                self.reset_type = 'goal'
                self.countdown()

    def countdown(self):
        """Méthode affichant un compte à rebours et relançant la balle (ou une nouvelle partie) une fois terminée.
        Elle a un comportement récursif, s'appelant elle-même après une seconde, la condition d'arrêt étant le compteur
        atteignant 0. L'IHM continue de s'exécuter pendant la seconde d'attente, mais la variable d'état booléenne
        countdown_ongoing indique à la fonction one_step de ne pas mettre à jour les positions des joueurs et de la
        balle pendant ce temps """
        self.ui.lcdNumber_2.display(self.countdown_state)  # Changement du numéro
        self.ui.lcdNumber.repaint()  # Mise à jour de l'affichage du compteur
        self.ui.lcdNumber_2.setHidden(False)  # On arrête de cacher le compteur
        self.countdown_ongoing = True  # Par cette variable d'état on indique aux autres fonctions que le compte à
        # rebours tourne
        self.countdown_state -= 1  # Décrémentation du chiffre du compteur
        if self.countdown_state != -2:  # Si la valeur affichée n'est pas zéro (on a un effet de bord, d'où la valeur -2)

            self.countdown_timer.singleShot(1000, self.countdown)  # On appellera de nouveau cette fonction dans une
            # seconde

        else:  # Sinon, il faut arrêter le compte à rebours
            self.countdown_state = 3  # On remet le chiffre à sa valeur initiale
            self.countdown_ongoing = False  # On change la variable d'état pour indiquer que le compte à rebours ne
            # tourne plus
            self.ui.lcdNumber_2.setHidden(True)  # On cache le compteur
            if self.reset_type == 'new_game':
                self.ball.reset_ball()  # On remet à zéro la position de la balle
                self.timer.start(int((1 / 60) * 1000))  # Si on commence une nouvelle partie, on initialise le timer
                print("game started")
            else:
                self.ball.reset_ball()  # Si on a juste eu un but, on réinitialise simplement la position de la balle

    def start_game(self):
        """Fonction lançant une partie"""
        # Game start
        self.ball.stat.reset()  # Remise à zéro des statistiques
        self.reset_type = 'new_game'
        self.countdown()  # Lancement du compte à rebours

    def end_game(self):
        """Fonction arrêtant une partie"""
        self.timer.stop()  # Arrêt du timer rythmant les appels de one_step
        self.ball.end_game()  # Appel de la fonction end_game de la balle
        self.welcomeWindow.end_game()  # Appel de la fonction end_game de la fenêtre principale

    def setChildrenFocusPolicy(self, policy):
        """Activation des flèches du clavier. Code trouvé sur internet"""

        def recursiveSetChildFocusPolicy(parentQWidget):
            for childQWidget in parentQWidget.findChildren(QtWidgets.QWidget):
                childQWidget.setFocusPolicy(policy)
                recursiveSetChildFocusPolicy(childQWidget)

        recursiveSetChildFocusPolicy(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = FirstWindow()
    window.show()
    app.exec_()
