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

# ---------- Code à taper : ----------
# Initialisation d'une Page :
page_accueil = el.Page()
page_accueil = page_accueil.makePage()
# Transformation des valeurs de la Page en Slots :
slots = el.Slot()
slots = slots.addSlots(page_accueil)
# Ouverture d'une page via un click sur Dossier :
page_lieu = el.Folder()
page_lieu = page_lieu.openPage(pages[1])

# ---------- Brouillon : ----------
'''
if floder.click == True:
    open page
'''