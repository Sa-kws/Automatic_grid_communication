
#from word2grid import elements as el

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
vocab = ['je', 'vouloir', 'aimer', 'quoi', 'ça', 'toi']
'''
# ---------- Code à taper dans main() : ----------
# Initialisation d'une Page :
page_accueil = el.Page()
page_accueil = page_accueil.addPage()
# Transformation des valeurs de la Page en Slots :
slots_accueil = el.Slot()
slots_accueil = slots_accueil.addSlots(page_accueil)
# Ouverture d'une page via un click sur Dossier :
page_lieu = el.Item()
page_lieu = page_lieu.clickItem(page_lieu, pages[1])

# ---------- Brouillon : ----------

item = el.Item()




            # Maintenant : df[slot] = le mot
            # ajout du mot dans une liste (liste_mots_usés)
            # ajout d'une condition : si le mot est dans la liste mits usés, alors on pass, sinon, df[slot] = le mot suivant


#print(page_accueil)
#print('\n')
#print(page_lieu)


    #put word in slot please :)
'''



from word2grid import new_elements as nel
item = nel.Item('vouloir')
item = item.makeItem()
print(item)
slot = nel.Slot(3,2)
print(slot.position)
slotitem = slot.addItem(slot.position, item)
print(slotitem)
page = nel.Page().makePage()
print(page)
filled_slots = nel.Page().addSlots(vocab, page)
print(filled_slots)




