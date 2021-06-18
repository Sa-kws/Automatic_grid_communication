import time
begin = time.time()

import json
import os
from collections import OrderedDict

os.remove('Proloquo_FR_brut.csv')

tour = 0

indesirables = [x.replace('\n', '') for x in open('mots_indésirables_picto.txt', 'r', encoding='utf-8')]
folders_name = [x.replace('\n', '').replace('-', ' ').replace(' Adjectifs','').replace(' Verbes','').upper() for x in open('french_repositories.txt', 'r', encoding='utf-8')]
folders_name = sorted(folders_name)
composed_words = [x.replace('\n','') for x in open('mots_composés.txt', 'r', encoding='utf-8')]
truncated_words = [x.replace('\n','') for x in open('mots_tronqués.txt', 'r', encoding='utf-8')]
# Ecrasement du fichier de sortie
erase = open('coordonnates_folder_names.txt', 'w', encoding='utf-8')
erase.close() # Faire un truc avec os.remove
del erase

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
    all_names.append(nom)
    all_file = all_file.rstrip()
    grid.append([nom, all_file])


    # Pour le développement (afin d'éviter de parcourir tout le répertoire)
    #if tour == 15:
    #    break

all_names = [x.replace(' - 2', '') for x in all_names]
all_names = list(OrderedDict.fromkeys(all_names))

# Assemblement des mots composés :
for i in range(0,len(grid)):
    words = grid[i][1]
    for cw in composed_words:
        if cw in grid[i][1]:
            to_replace = cw.split(' ')
            length = len(cw)
            start = words.index(cw)
            final = start + length
            if len(to_replace) == 2:
                    words = words.replace(words[start:final], to_replace[0] + '-' + to_replace[1])
            if len(to_replace) == 3:
                    words = words.replace(words[start:final], to_replace[0] + '-' + to_replace[1] + '-' + to_replace[2])
            if len(to_replace) == 4:
                    words = words.replace(words[start:final], to_replace[0] + '-' + to_replace[1] + '-' + to_replace[2] + '-' + to_replace[3])
            if len(to_replace) == 5:
                    words = words.replace(words[start:final], to_replace[0] + '-' + to_replace[1] + '-' + to_replace[2] + '-' + to_replace[3] + '-' + to_replace[4])
            grid[i][1] = words


for liste in grid:
    page = liste[0]
    vocabulary = liste[1].split(' ')
    for word in vocabulary:
        with open('Proloquo_FR_brut.csv', 'a', encoding='utf-8') as outfile:
            if word.upper() in folders_name:
                outfile.write(word.upper() + '_R\t' + page.lower() + '\t' + word.lower() + '_R@' + page.lower() + '\n')
            else:
                outfile.write(word.upper() + '\t' + page.lower() + '\t' + word.lower() + '@' + page.lower() + '\n')



end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')
