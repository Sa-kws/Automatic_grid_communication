def getFrequency(value, total, pos):
    '''
    :param value: int - Valeur que l'on souhaite convertir en pourcentage
    :param total: int - Total sur lequel on calcule le pourcentage
    :return: int - Pourcentage calculé
    '''

    pourcentage = round((100 * value) / total, 2)
    return pourcentage


file_dico = {'child_lemmas_frequency.txt' : 1,
             'child_pos_frequency.txt': 2,
             'lemmas_frequency_ESLO.txt': 3,
             'pos_frequency_ESLO.txt': 4,
             'lemmas_frequency_ESLO1.txt': 5,
             'pos_frequency_ESLO1.txt': 6,
             'lemmas_frequency_ESLO2.txt': 7,
             'pos_frequency_ESLO2.txt': 8}

total = 0
value = []


infile = input('Quel fichiez voulez-vous traiter ? (Si plusieurs fichier, insérer ";" entre chaque numéro de fichier)\n1/ child_lemmas_frequency.txt : 1\n2/child_pos_frequency.txt : 2\n3/lemmas_frequency_ESLO.txt : 3\n4/pos_frequency_ESLO.txt : 4\n5/lemmas_frequency_ESLO1.txt : 5\n6/pos_frequency_ESLO1.txt : 6\n7/lemmas_frequency_ESLO2.txt : 7\n8/pos_frequency_ESLO2.txt : 8\n"ALL" pour l\'ensemble des fichiers\n-->')
if infile != 'ALL':
    file_to_process = [int(x) for x in infile.split(';')]
else:
    file_to_process = [y for x,y in file_dico.items()]


for file in file_to_process:
    name_of_infile = 'OUT_DATAS/' + list(file_dico.keys())[list(file_dico.values()).index(file)]
    name_of_outfile = name_of_infile.replace('.txt','_PERCENTAGE.txt')

    with open(name_of_infile, 'r', encoding='utf-8') as infile:
        for pos in infile:
            pos = pos.split('\t')
            total += int(pos[1].replace('\n', ''))
            value.append([pos[0], int(pos[1].replace('\n', ''))])

    with open(name_of_outfile, 'a', encoding='utf-8') as out_file:
        for element in value:
            pourcentage = getFrequency(element[1], total, element[0])
            out_file.write(element[0] + '\t' + str(pourcentage).replace('.',',') + '%\n')



#os.remove(name_of_infile)
