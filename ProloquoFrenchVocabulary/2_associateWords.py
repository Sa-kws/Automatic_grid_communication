import time
begin = time.time()

import os
import json
import re
from collections import OrderedDict

FOLDER = 'Proloquo_text_screens'
nb_ValueError = 0
OUTFILE = 'Vocabulaire_Français.txt'
all_words = []
erase_file = open(OUTFILE, 'w', encoding='utf-8')
erase_file.close()


# Fonction qui va permettre de récupérer les coordonnés des mots repérés sur l'image + stockage dans une liste des coordonnées
def formCoordonate(str_to_split, word_position):
    coordonnee = str_to_split.split(',')
    coordonnee[0] = int(coordonnee[0].replace('{x : ', ''))
    coordonnee[1] = int(coordonnee[1].replace(' y:', '').replace('}', ''))
    word_position.append(coordonnee)
    return coordonnee, word_position

# Parcours du dossier contenant TOUS les fichiers json
for file in os.listdir(FOLDER):

    file = os.path.join(FOLDER, file)
    f = open(file, 'r', encoding='utf-8')
    json_file = json.load(f)
    f.close()

    # Suppression de la première annotation contenant la totalité des mots océrisés, et la plage totale de repérage
    del json_file[0]

    page_words= []

    # Parcours des annotations de chaque mot océrisé
    for annotation in json_file:
        word_position = []
        index = 0
        # Récupération des coordonnées
        A, word_position = formCoordonate(annotation['VERTICES'][0], word_position)
        B, word_position = formCoordonate(annotation['VERTICES'][1], word_position)
        C, word_position = formCoordonate(annotation['VERTICES'][2], word_position)
        D, word_position = formCoordonate(annotation['VERTICES'][3], word_position)

        # Si le point D est entre VAL1 et VAL2, alors on le zap. Il y a certainement une moyenne sur l'écart entre 2 lignes
        # Ex Entre le point C/D de la ligne 1 et A/B de la ligne 2



        # Elimination des mots océrisés non désirable (métadatas de l'iPad)
        if A[1] >200 and A[1] <1420 and '↑' not in annotation['DESCRIPTION']:


            # Recherche de proximité entre deux mots (cf readme)
            try:
                print(annotation['DESCRIPTION'])
                print('word_two_A_x :', A[0])
                print('word_two_A_y :', A[1])
                print('word_one_B_x :', word_one_B_point_x)
                print('word_one_B_y :', word_one_B_point_y)
                print('\n')
                # Distance abscisse (x) entre le mot1 (word_one_B) et le mot2 inférieur à 20 + Distance ordonnés (y) compris entre -10 et 10
                # Les conditions 2 et 3 fonctionnent, mais uniquement pour trouver les mots qui devraient ê ensemble, il faut une autre condition pour les espaces interlinéaires
                if A[0] - word_one_B_point_x <25 and A[1] - word_one_B_point_y < 3 and A[1] - word_one_B_point_y > -3:
                    word = word_one_B + ' ' + annotation['DESCRIPTION']
                    try:
                        # Suppression du mot précédent, qui est à présent lié sur le nouveau bouton
                        del page_words[page_words.index(word_one_B)]
                    except ValueError:
                        print('ValueError :', word_one_B)
                        nb_ValueError += 1
                else:
                    word = annotation['DESCRIPTION']
                page_words.append(word)
            except NameError:
                word = annotation['DESCRIPTION']
                print('Premier tour')
                page_words.append(word)


            # Stockage des coordonnées du point B
            word_one_B_point_x = B[0]
            word_one_B_point_y = B[1]
            word_one_B = annotation['DESCRIPTION']

    try:
        # Récupération du nom du dossier
        page_name = page_words[0]
        with open(OUTFILE, 'a', encoding='utf-8') as out_file:
            out_file.write(page_name + '_FOLDER\n')
        del page_words[0]
    except IndexError:
        print('IndexError', page_words)

    # Ecriture du vocabalaire Français dans un fichier
    for wrd in page_words:
        if wrd not in all_words:
            all_words.append(wrd)
            with open(OUTFILE, 'a', encoding='utf-8') as out_file:
                out_file.write(wrd + '\n')
    break #sert le temps du développement, pour éviter de parcourir tous les fichier json

print('ValueError :', nb_ValueError)


end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')
