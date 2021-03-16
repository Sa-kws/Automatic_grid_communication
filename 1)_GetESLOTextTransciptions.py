# -*- coding: cp1252 -*-
import re

reg1 = r'<[\s]*[A-Z]*[a-z]*[</]*'
transcriptions = []
fichier = open('name.txt', 'w', encoding='utf-8')

# Version 1
with open('ESLO2_BOUL_1250_C.trs') as trs:
    for o in trs:
        if re.match(reg1, o) or o == '\n':
            pass
        else:
            fichier.write(o)


# Version 2
annotations = [0 if re.match(reg1, o) or o == '\n' else fichier.write(o) for o in open('ESLO2_BOUL_1250_C.trs')]
del annotations

fichier.close()
