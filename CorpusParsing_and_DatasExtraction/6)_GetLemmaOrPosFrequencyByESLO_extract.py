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

frequence_eslo1 = {}
frequence_eslo2 = {}
compteur = 0
lemme_pos = []
print('Variables initialisées')

for fichier in os.listdir('OUT_DATAS/ESLO_transcriptions'):
    compteur += 1
    lemme = ''

    name_of_infile = 'OUT_DATAS/Eslo_transcriptions/'+fichier
    if to_get == 1:
        name_of_outfile_eslo1 = 'OUT_DATAS/lemmas_frequency_ESLO1.txt'
        name_of_outfile_eslo2 = 'OUT_DATAS/lemmas_frequency_ESLO2.txt'
    elif to_get == 2:
        name_of_outfile_eslo1 = 'OUT_DATAS/POS_frequency_ESLO1.txt'
        name_of_outfile_eslo2 = 'OUT_DATAS/POS_frequency_ESLO2.txt'


    with open(name_of_infile, 'r', encoding='utf-8') as in_file:
        for ligne in in_file:
            lemme += ligne.replace('\n', ' ')


    doc = nlp(lemme)
    for token in doc:
        if to_get == 1:
            lemme = [re.sub(r'[^\w\s]', '', token.lemma_.lower()), 0]
        elif to_get == 2:
            lemme = [token.pos_, 0]
        if 'ESLO1' in fichier:
            if lemme[0] != ' ' and lemme[0] != '':
                if lemme[0] in frequence_eslo1:
                    frequence_eslo1[lemme[0]] = [frequence_eslo1[lemme[0]][0] +1, lemme[1]]
                else:
                    frequence_eslo1[lemme[0]] = [1, lemme[1]]

        else:
            if lemme[0] != ' ' and lemme[0] != '':
                if lemme[0] in frequence_eslo2:
                    frequence_eslo2[lemme[0]] = [frequence_eslo2[lemme[0]][0] +1, lemme[1]]
                else:
                    frequence_eslo2[lemme[0]] = [1, lemme[1]]

    print(compteur, '--', fichier, '\tdone ✅')


frequence_eslo1 = sorted(frequence_eslo1.items(), key=operator.itemgetter(1))
frequence_eslo1.reverse()

frequence_eslo2 = sorted(frequence_eslo2.items(), key=operator.itemgetter(1))
frequence_eslo2.reverse()
print('Dictionnaires triés ✅')

with open(name_of_outfile_eslo1, 'w', encoding='utf-8') as out:
    for key, value in frequence_eslo1:
        out.write(str(key) + '\t' + str(value[0]) + '\n')

with open(name_of_outfile_eslo2, 'w', encoding='utf-8') as out:
    for key, value in frequence_eslo2:
        out.write(str(key) + '\t' + str(value[0]) + '\n')
print('Fichiers de sortie', name_of_outfile_eslo1, 'et', name_of_outfile_eslo2,'créés et remplis.')

#shutil.rmtree('ESLO_transcriptions')

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')