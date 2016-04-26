#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division

# import des modules Qt
from PyQt4 import QtGui
import sys


if __name__ == '__main__':

    # creation de l'application
    app = QtGui.QApplication(sys.argv)

    # creation d'une fenetre principale
    window = QtGui.QWidget()

    # changeons le titre de la fenetre
    window.setWindowTitle("Signal")

    # ajout d'un bouton dans la fenetre
    # Le bouton sera enfant de la fenetre
    button = QtGui.QPushButton("Cliquer ici", window)

    # redimensionnons le bouton
    button.resize(150, 50)

    # connectons le signal de clic au slot quit() de l'application
    # deprecated : button.connect(button, QtCore.SIGNAL("clicked()"),\
    #    app, QtCore.SLOT("quit()"))
    button.clicked.connect(app.quit)

    # affichons la fenetre
    window.show()
    # lancons la boucle evenementielle
    app.exec_()
