# -*- coding: utf-8 -*-
import time

begin = time.time()

import os
import shutil
from lxml import etree

try:
    os.mkdir("OUT_DATAS/ESLO_transcriptions")
except FileExistsError:
    print('Folder ESL0_transcriptions already exists')

compteur = 1

for f in os.listdir('IN_DATAS/ESLO_UTF-8'):

    name_of_outfile = 'OUT_DATAS/ESLO_transcriptions/' + f.replace('_MODIFIED.xml', '_BRUTE.txt')
    tree = etree.parse('IN_DATAS/ESLO_UTF-8/' + f)

    try:
        with open(name_of_outfile, 'w', encoding='utf-8') as out_file:
            for element in tree.xpath('/Trans/Episode/Section/Turn'):
                out_file.write(element.text)
    except UnicodeDecodeError:
        print('Erreur de décodage pour_________________________' + str(f))

    print(compteur, '\t', f, '\tdone ✅')
    compteur += 1

# shutil.rmtree('ESLO_UTF-8')

end = time.time()
temps = end - begin
minutes = round((temps / 60), 2)
print('Temps d\'execution : ' + str(minutes) + ' minute.s.')