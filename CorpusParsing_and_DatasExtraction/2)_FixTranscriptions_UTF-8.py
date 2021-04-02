import time
begin = time.time()

import os

compteur = 1

for fichier in os.listdir('IN_DATAS/ESLO_UTF-8'):

    name_of_infile = 'IN_DATAS/ESLO_UTF-8/' + fichier
    name_of_outfile = 'IN_DATAS/ESLO_UTF-8/' + fichier.replace('.trs', '_MODIFIED.xml')


    with open(name_of_infile, 'r') as file:
        for ligne in file:
            if '/>' not in ligne and 'DOCTYPE' not in ligne:
                with open(name_of_outfile, 'a') as outfile:
                    outfile.write(ligne)
            elif 'scope=' in ligne:
                with open(name_of_outfile, 'a') as outfile:
                    outfile.write(ligne)
    print(compteur, '\t', fichier, '\tdone')
    compteur += 1
    os.remove('IN_DATAS/ESLO_UTF-8/'+fichier)

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')