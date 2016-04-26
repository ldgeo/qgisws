#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal

from pyproj import Proj, transform
import os

# -----------------------------------------------------------------------------
# functions
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def count_lines(filename):
    # TODO
    pass

# -----------------------------------------------------------------------------
def reproject(x, y, source_srid, dest_srid):

    sp = Proj("+init=EPSG:{}".format(source_srid))
    dp = Proj("+init=EPSG:{}".format(dest_srid))

    # TODO

# -----------------------------------------------------------------------------
def transform_csv(filename, separator=','):
    # TODO
    pass

# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Projector(QThread):
    """
    TODO : declare signals
    """
    def __init__(self):
        super(Projector, self).__init__()
        self.filename = ""

    def filename(self, filename):
        self.filename = filename

    def run(self):
        # TODO
        pass
