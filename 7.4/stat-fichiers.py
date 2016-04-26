#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3 ready
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import os

# '~' est un raccourci pour désigner le répertoire utilisateur.
home_directory = os.path.expanduser('~')
file_list = os.listdir(home_directory)

count_dir = 0
count_file = 0
count_hidden = 0
count_others = 0
count = 0

for node in file_list:
    count = count + 1
    if node[0] == '.':
        count_hidden = count_hidden + 1
    if os.path.isfile(os.path.join(home_directory, node)):
        count_file = count_file + 1
    elif os.path.isdir(os.path.join(home_directory, node)):
        count_dir = count_dir + 1
    else:
        count_others = count_others + 1

print('Le répertoire utilisateur contient :')
print('    - {} fichiers réguliers'.format(count_file))
print('    - {} répertoires'.format(count_dir))
print('    - {} autres fichiers'.format(count_others))
print('Notez que {:2.0f}% des fichiers sont masqués'.format(count_hidden / float(count) * 100))
