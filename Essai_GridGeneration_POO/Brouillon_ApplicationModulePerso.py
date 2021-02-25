from word2grid import elements as el

# ---------- Création des données à traiter : ----------
# 2 pages
pages = ['accueil', 'lieu']
pages = ['page_'+x for x in pages]

# 18 positions par page (-1 pour la page_accueil) (3x6)
slots = ['SLOT' for x in range(0,3)]

# 1 dossier pour la page_accueil
folder = [x for x in open('vocab_page_accueil.txt', encoding='utf-8') if x.isupper()]

# Vocabulaire à placer
words_page_accueil = [x.replace('\n','') for x in open('vocab_page_accueil.txt', encoding='utf-8') if x.islower()]
words_page_lieu = [x.replace('\n','') for x in open('vocab_page_lieu.txt', encoding='utf-8') if x.islower()]

page_accueil = el.Page()
page_accueil = page_accueil.makePage()
page_lieu = el.Page()
page_lieu = page_lieu.makePage()



# Changement des valeurs vers des positions (slots)
for i in page_accueil:
    page_accueil[i] = [x for x in slots]


# Ouverture d'une page 
if floder.click == True:
    open page

'''
#remplir les slots de words :
#--------------------------

positionner les mots sur les slots --> parcours de la liste de mots :
for mots in liste_mots : mots sur slot dispo (besoin de parcourir le df aussi)
'''
#Essai 1 : 
for i in slots_accueil:
    try:
        slots_accueil[i] = [x for x in words_page_accueil]
    except ValueError:
        print('Changement de colonne')
print(slots_accueil)


'''
IL FAUT PRENDRE UN MOT ET LE POSER SUR UNE POSITION, PRENDRE UN MOT ET LE POSER, PRENDRE UN MOT ET LE POSER...
'''

'''
compteur = 0
used_words = []
for i in page_accueil.iterrows():
    # i est un tuple : i[0] = Row ; i[1] = ValeurS de la ligne
    for j in i[1]:
        #print('j', compteur, type(j), j)
        for word in words_page_accueil:
            unused_words = []
            if word in used_words:
                unused_words.append(word)

            else:
                compteur += 1
                used_words.append(word)
                try:
                    # page_accueil[str(compteur)] = [x for x in word] #/ NOT WORKING
                    for slot in page_accueil[str(compteur)]:
                        for unu_word in unused_words:
                           print(unu_word)
                    page_accueil[str(compteur)].replace('SLOT', word, inplace=True)

                except ValueError:
                    print('Erreur passée - VALUE ERROR')
                except KeyError:
                    print('Erreur passée - KEY ERROR')

'''
'''
                try:
                    for sl in page_accueil[str(compteur)]:
                        print(sl)

                except KeyError:
                    print('Erreur passée - KEY ERROR')
'''
