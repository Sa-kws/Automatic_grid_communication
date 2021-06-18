import json
import os

tour = 0

indesirables = [x.replace('\n', '') for x in open('mots_indésirables_picto.txt', 'r', encoding='utf-8')]
folders_name = [x.replace('\n', '').replace('-', ' ').replace(' Adjectifs','').replace(' Verbes','').upper() for x in open('french_repositories.txt', 'r', encoding='utf-8')]
folders_name = sorted(folders_name)

# Ecrasement du fichier de sortie
erase = open('coordonnates_folder_names.txt', 'w', encoding='utf-8')
erase.close()

FOLDER = 'Proloquo_text_screens'


# Fonction qui va permettre de récupérer les coordonnés des mots repérés sur l'image + stockage dans une liste des coordonnées
def formCoordonate(str_to_split, word_position):
    coordonnee = str_to_split.split(',')
    coordonnee[0] = int(coordonnee[0].replace('{x : ', ''))
    coordonnee[1] = int(coordonnee[1].replace(' y:', '').replace('}', ''))
    word_position.append(coordonnee)
    return coordonnee, word_position


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
                        all_file += mot + '\t'
        past_word = mot
    nom = nom.rstrip()
    all_file = all_file.rstrip()
    #print(nom)
    #print(all_file)
    #print('\n---------------------------------\n')

    # Pour le développement (afin d'éviter de parcourir tout le répertoire)
    if tour == 15:
        break
