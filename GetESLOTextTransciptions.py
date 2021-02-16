import time
begin = time.time()

import glob
import os
import re

reg1 = r'<[\s]*[A-Z]*[a-z]'
reg2 = r'</'

os.mkdir("ESLO_modified")
dossier = glob.glob('ESLO_2//*')

for fichier in dossier:
    transcriptions = []
    name = fichier.replace('ESLO_2\\', '')
    name = name.replace('.trs', '.xml')
    name = 'ESLO_modified/' + name
    with open(fichier, 'r') as f:
        for o in f:
            o = o.replace('\t', '',6)
            if re.match(reg1, o) or re.match(reg2, o): pass
            elif o == '\n': pass
            else: transcriptions.append(o)
    with open(name, 'w') as out:
        for enonce in transcriptions:
            out.write(enonce)

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')