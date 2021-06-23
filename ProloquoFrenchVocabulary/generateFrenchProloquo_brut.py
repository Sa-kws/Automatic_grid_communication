import time
begin = time.time()

import json
import os
from collections import OrderedDict
import re

try:
    os.remove('Proloquo_FR_brut.csv')
except FileNotFoundError:
    pass
try:
    os.remove('coordonnates_folder_names.txt')
except FileNotFoundError:
    pass

tour = 0
re_error = 0

indesirables = [x.replace('\n', '') for x in open('mots_indésirables_picto.txt', 'r', encoding='utf-8')]
folders_name = [x.replace('\n', '').replace('-', ' ').replace(' Adjectifs','').replace(' Verbes','').upper() for x in open('french_repositories.txt', 'r', encoding='utf-8')]
folders_name = sorted(folders_name)
composed_words = [x.replace('\n','').replace('-', ' ') for x in open('mots_composés.txt', 'r', encoding='utf-8')]
truncated_words = [x.replace('\n','') for x in open('mots_tronqués.txt', 'r', encoding='utf-8')]

FOLDER = 'Proloquo_text_screens'


# Fonction qui va permettre de récupérer les coordonnés des mots repérés sur l'image + stockage dans une liste des coordonnées
def formCoordonate(str_to_split, word_position):
    coordonnee = str_to_split.split(',')
    coordonnee[0] = int(coordonnee[0].replace('{x : ', ''))
    coordonnee[1] = int(coordonnee[1].replace(' y:', '').replace('}', ''))
    word_position.append(coordonnee)
    return coordonnee, word_position

all_names = []
grid = []


for file in os.listdir(FOLDER):

    nom = ''
    tour += 1
    all_file = ''
    to_add = []

    file = os.path.join(FOLDER, file)
    f = open(file, 'r', encoding='utf-8')
    json_file = json.load(f)
    f.close()


    del json_file[0]

    for annotation in json_file:
        mot = annotation['DESCRIPTION']
        # Récupération des coordonnées
        # A = [x, y]
        # word_position = [A,B,C,D]
        # A = position en bas à gauche
        # B = position en bas à droite
        # C = position en haut à droite
        # D = position en haut à gauche
        word_position = []
        A, word_position = formCoordonate(annotation['VERTICES'][0], word_position)
        B, word_position = formCoordonate(annotation['VERTICES'][1], word_position)
        C, word_position = formCoordonate(annotation['VERTICES'][2], word_position)
        D, word_position = formCoordonate(annotation['VERTICES'][3], word_position)
        if mot not in indesirables:

            # Suppression des métadonnées de l'ipad
            if A[1] >200 and A[1] <1420 and '↑' not in mot:

                # A[1] == ordonné du point A du mot
                # D[1] == ordonné du point D du mot
                if A[1] < 290 and D[1] >240:

                    # Sélection du titre à partir d'une certaine ordonnée (935) du point A afin d'éliminer le bouton retour
                    if A[0] > 935:
                        nom += mot + ' '

                # On récupère le corps du vocabulaire, en éliminant le titre et le bouton retour (avec une ordonné suppérieur à 350 pour le point C du mot)
                if C[1] > 350:
                    if mot not in nom and mot:
                        all_file += mot + ' '
        past_word = mot

    nom = nom.rstrip()
    all_names.append(nom.upper())
    #all_file = all_file.rstrip().lower()

    for cw in composed_words:
        mots = cw.split(' ')
        try:
            if len(mots) == 2:
                if mots[0] in all_file and mots[1] in all_file:
                    all_file = re.sub(mots[0] + '[\s-]*', '', all_file, 1)
                    all_file = re.sub(mots[1] + ' [\s-]*', '', all_file, 1)
                    to_add.append(mots[0] + '-' + mots[1] + ' ')
            if len(mots) == 3:
                if mots[0] in all_file and mots[1] in all_file and mots[2] in all_file:
                    all_file = re.sub(mots[0] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[1] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[2] + ' ', '', all_file, 1)
                    to_add.append(mots[0] + '-' + mots[1] +'-' + mots[2] + ' ')
            if len(mots) == 4:
                if mots[0] in all_file and mots[1] in all_file and mots[2] in all_file and mots[3] in all_file:
                    all_file = re.sub(mots[0] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[1] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[2] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[3] + ' ', '', all_file, 1)
                    to_add.append(mots[0] + '-' + mots[1] +'-' + mots[2] +  '-' + mots[3] +' ')
            if len(mots) == 5:
                if mots[0] in all_file and mots[1] in all_file and mots[2] in all_file and mots[3] in all_file and mots[4] in all_file:
                    all_file = re.sub(mots[0] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[1] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[2] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[3] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[4] + ' ', '', all_file, 1)
                    to_add.append(mots[0] + '-' + mots[1] +'-' + mots[2] +  '-' + mots[3] + '-' + mots[4] + ' ')
            if len(mots) == 6:
                if mots[0] in all_file and mots[1] in all_file and mots[2] in all_file and mots[3] in all_file and mots[4] in all_file and mots[5] in all_file:
                    all_file = re.sub(mots[0] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[1] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[2] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[3] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[4] + ' ', '', all_file, 1)
                    all_file = re.sub(mots[5] + ' ', '', all_file, 1)
                    to_add.append(mots[0] + '-' + mots[1] +'-' + mots[2] +  '-' + mots[3] + '-' + mots[4] + '-' + mots[5] + ' ')
        except re.error:
            print('RE.ERROR')
            re_error += 1
    for x in to_add:
        all_file += x

    grid.append([nom, all_file])

    # Pour le développement (afin d'éviter de parcourir tout le répertoire)
    #if tour == 15:
    #    break

all_names = [x.replace(' - 2', '') for x in all_names]
all_names = list(OrderedDict.fromkeys(all_names))

for liste in grid:
    page = liste[0]
    vocabulary = liste[1].split(' ')
    for word in vocabulary:
        with open('Proloquo_FR_brut.csv', 'a', encoding='utf-8') as outfile:
            outfile.write(word.upper() + '\t' + page.lower() + '\t' + word.lower() + '@' + page.lower() + '\n')

print('Nombre d\'erreurs RE :', re_error)

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')
