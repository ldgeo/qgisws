# -*- coding:utf-8 -*-
"""
Exercice :

Remplir les fonctions déclarées dans ce module :

- *count_lines* qui renvoie le nombre de lignes d'un fichier texte
- *count_words* qui compte le nombre d'occurences d'un mot dans une colonne d'un fichier csv
- *reproject* qui reprojette un point d'un SRID à un autre (en utilisant le module pyproj)
- *transform_csv* qui lit un fichier csv, le réécrit en ayant reprojeté les champs
  de coordonnées (les 2 derniers)

Une fois ces fonctions écrites, les tester (dans ipython ou dans le main
du module) pour analyser, transformer et réécrire le fichier ban-75.csv.
Les coordonnées long/lat (srid=4326) seront reprojetés en google mercator (srid=3857)

"""
from pyproj import Proj, transform


def count_lines(filename):
    """
    :param filename: nom du fichier à ouvrir
    """
    pass


def count_words(filename, column, word, separator=','):
    """
    :param filename: nom du fichier à ouvrir
    :param column: numéro de la colonne où compter les mots
    :param word: mot à compter
    :param separator: caractère qui sépare les champs de texte
    """
    pass


def reproject(x, y, source_srid, dest_srid):
    """
    :param x: coordonnée X
    :param y: coordonnée Y
    :param source_srid: système de réf spatial source (code EPSG)
    :param dest_srid: système de réf spatial destination (code EPSG)
    """
    pass


def transform_csv(filename, separator=','):
    """
    le nom du fichier de sortie sera composé du nom du fichier source suivi
    de '.transfo.csv'

    :param filename: nom du fichier à lire
    :param separator: séparateur de colonne
    """
    pass


if __name__ == '__main__':
    pass
