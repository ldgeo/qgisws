#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division

import sys
# import des modules PyQt necessaires
from PyQt4.QtGui import QApplication, QPushButton
# on ne lance les commandes suivantes que si on est dans un script

if __name__ == '__main__':
    # Tous les programmes Qt ont besoin d'une
    # instance de QApplication
    # On passe les arguments de la ligne de commande car Qt
    # sait en interpreter certain
    app = QApplication(sys.argv)
    # On cree un bouton avec un texte dessus
    button = QPushButton("Hello World !")
    # on doit explicitement demander l'affichage du bouton
    button.show()
    # On lance la boucle evenementielle
    sys.exit(app.exec_())
