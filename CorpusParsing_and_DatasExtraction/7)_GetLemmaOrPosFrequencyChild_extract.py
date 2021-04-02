import time
begin = time.time()

to_get = int(input('Fréquence lemmes : entrez 1\nFréquence POS : entrez 2\n'))

import spacy
import re
import operator
import os
print('Modules importés ✅')

nlp = spacy.load('fr_core_news_sm')
print('Modèle SpaCy chargé ✅')

frequence = {}
compteur = 0
print('Variables initialisées ✅')

for fichier in os.listdir('OUT_DATAS/Child_transcriptions'):
    compteur += 1
    lemme = ''

    name_of_infile = 'OUT_DATAS/Child_transcriptions/'+fichier
    if to_get == 1:
        name_of_outfile = 'OUT_DATAS/child_lemmas_frequency.txt'
    elif to_get == 2:
        name_of_outfile = 'OUT_DATAS/child_POS_frequency.txt'


    with open(name_of_infile, 'r', encoding='utf-8') as in_file:
        for ligne in in_file:
            lemme += ligne.replace('\n', ' ')

    doc = nlp(lemme)

    for token in doc:
        if to_get == 1:
            lemme = re.sub(r'[^\w\s]', '', token.lemma_.lower())
        elif to_get == 2:
            lemme = token.pos_
        if lemme != ' ' and lemme != '' and lemme != 'SPACE':
            if lemme in frequence:
                frequence[lemme] += 1
            else:
                frequence[lemme] = 1

    print(compteur, '--', fichier, '\tdone ✅')


frequence = sorted(frequence.items(), key=operator.itemgetter(1))
frequence.reverse()
print('Dictionnaire trié ✅')

with open(name_of_outfile, 'w', encoding='utf-8') as out:
    for key, value in frequence:
        out.write(str(key) + '\t' + str(value) + '\n')

print('Fichier de sortie', name_of_outfile,'créé et rempli.')

#shutil.rmtree('Child_transcriptions')

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')