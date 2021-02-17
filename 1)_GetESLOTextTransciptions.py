import time
begin = time.time()

import glob
import os
import re
import codecs

reg1 = r'<[\s]*[A-Z]*[a-z]'
reg2 = r'</'


os.mkdir("ESLO_modified")
dossier = glob.glob('ESLO_2//*')



'''
with codecs.open('ESLO_2/ESLO2_BOUL_1250_C.trs', 'r', encoding='mbcs') as ansi_file:
    with codecs.open("ESLO_BOUL_utf8_test.txt", "w", encoding="UTF-8") as utf_8file:
        while True:
            contents = ansi_file.read(blockSize)
            if not contents:
                break
            utf_8file.write(contents)
            
'''

for fichier in dossier:
    transcriptions = []
    name = fichier.replace('ESLO_2\\', '')
    name = name.replace('.trs', '.txt')
    name = 'ESLO_modified/' + name
    with codecs.open(fichier, 'r', encoding='mbcs') as f:
        for o in f:
            o = o.replace('\t', '',6)
            if re.match(reg1, o) or re.match(reg2, o): pass
            elif o == '\n': pass
            else: transcriptions.append(o)
    with codecs.open(name, 'w', encoding='utf-8') as out:
        for enonce in transcriptions:
            out.write(enonce)

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')