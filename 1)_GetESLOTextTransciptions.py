# -*- coding: cp1252 -*-
import time
begin = time.time()

import re

reg1 = r'<[\s]*[A-Z]*[a-z]*[</]*'
transcriptions = []

fichier = open('name.txt', 'w', encoding='utf-8')
with open('ESLO2_BOUL_1250_C.trs') as trs:
    for o in trs:
        if re.match(reg1, o) or o == '\n':
            print(o.replace('\n',''))
            pass
        else:
            fichier.write(o)
fichier.close()

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')
