#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division


# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
# standard
import os

# pyqt
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QDialogButtonBox
from PyQt4.QtGui import QFileDialog
from PyQt4.QtCore import QDir
from PyQt4.QtCore import pyqtSignal

# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Browser(QDialog, ban_ui.Ui_Browser):

    # -------------------------------------------------------------------------
    # public methods
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # init attributes
        # TODO

        # custom settings for widgets
        # TODO

        # connect
        # TODO

    # -------------------------------------------------------------------------
    @property
    def filename(self):
        # TODO
        pass

    # -------------------------------------------------------------------------
    @filename.setter
    def filename(self, filename):
        # TODO
        pass

    # -------------------------------------------------------------------------
    # private methods
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __in_progress(self, line):
        # TODO
        pass

    # -------------------------------------------------------------------------
    def __compute_done(self):
        # TODO
        pass

    # -------------------------------------------------------------------------
    def __ok(self):
        # TODO
        pass

    # -------------------------------------------------------------------------
    def __browse(self):
        # TODO
        pass
