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