import time
begin = time.time()

import os
import shutil



dossier = os.listdir('IN_DATAS/ESLO-2021-03-08')

try:
    os.mkdir('OUT_DATAS')
except FileExistsError:
    pass

try:
    os.mkdir("IN_DATAS/ESLO_UTF-8")
    os.mkdir("IN_DATAS/ESLO_ISO")
except FileExistsError:
    pass

for fich in dossier:
    fichier = open('IN_DATAS/ESLO-2021-03-08/'+fich, 'r')
    for ligne in fichier:
        if 'ISO' in ligne:
            fichier.close()
            shutil.move('IN_DATAS/ESLO-2021-03-08/'+fich, 'IN_DATAS/ESLO_ISO/'+fich)
            break
        if 'UTF-8' in ligne or 'utf-8' in ligne:
            fichier.close()
            shutil.move('IN_DATAS/ESLO-2021-03-08/'+fich, 'IN_DATAS/ESLO_UTF-8/' + fich)
            break

shutil.rmtree('IN_DATAS/ESLO-2021-03-08')

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')