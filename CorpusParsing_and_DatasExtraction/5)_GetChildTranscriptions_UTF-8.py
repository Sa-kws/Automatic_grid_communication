# -*- coding: utf-8 -*-
import time

begin = time.time()

import os
import shutil
from lxml import etree

try:
    os.mkdir("OUT_DATAS/Child_transcriptions")
except FileExistsError:
    print('Folder Child_transcriptions already exists')

compteur = 1
child_speakers = [x.replace('\n','') for x in open('OUT_DATAS/child_locuteurs.txt')]


for f in os.listdir('IN_DATAS/ESLO_UTF-8'):

    child_transcriptions = []
    name_of_child_outfile = 'OUT_DATAS/Child_transcriptions/' + f.replace('_MODIFIED.xml', '_BRUTE_CHILD.txt')
    tree = etree.parse('IN_DATAS/ESLO_UTF-8/' + f)



    for attribute in tree.xpath('/Trans/Speakers/Speaker'):
        if attribute.attrib['name'] in child_speakers:
            id_child_loc = attribute.attrib['id']
            for transcription in tree.xpath('/Trans/Episode/Section/Turn[@speaker="'+id_child_loc+'"]'):
                child_transcriptions.append(transcription.text)


    if len(child_transcriptions) != 0:
        with open(name_of_child_outfile, 'a', encoding='utf-8') as child_out_file:
            for trans in child_transcriptions:
                child_out_file.write(trans)

    print(compteur, '\t', f, '\tdone ✅')
    compteur += 1

#shutil.rmtree('ESLO_UTF-8')

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')