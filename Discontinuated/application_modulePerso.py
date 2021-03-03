from word2grid import new_elements as nel
''''''
# ---------- Création des données à traiter : ----------
# 2 pages
pages = ['accueil', 'lieu']
pages = ['page_'+x for x in pages]

# 18 positions par page (-1 pour la page_accueil) (3x6)
slots = ['SLOT' for x in range(0,3)]

# 1 dossier pour la page_accueil
folder = [x for x in open('vocab_page_accueil.txt', encoding='utf-8') if x.isupper()]

# Vocabulaire à placer
#words_page_accueil = [x.replace('\n','') for x in open('vocab_page_accueil.txt', encoding='utf-8') if x.islower()]
#words_page_lieu = [x.replace('\n','') for x in open('vocab_page_lieu.txt', encoding='utf-8') if x.islower()]
page_a = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'A14_F-c', 'a15', 'a16', 'a17', 'A18_F-b']
page_b = [x.lower().replace('a','b').replace('_f-c','').replace('_f-b','') for x in page_a]
page_c = [x.lower().replace('a','c').replace('_f-c','').replace('_f-b','') for x in page_a]



# ---------- Futur main() : ----------

'''
item = nel.Item('vouloir')
item = item.makeItem()
#print(item)
slot = nel.Slot(nel.Grid.ROW_SIZE,nel.Grid.COL_SIZE)
#print(slot.position)
slotitem = slot.addItem(slot.position, item)
#print(slotitem)
page = nel.Page().makePage()
PAGE_A = nel.Page().addSlots(page_a, page)
'''

# ---------- Brouillon : ----------
'''
-------------------------------- Change df value ---XXXXXXXXXXX---
for i in filled_slots.columns:
    for val in range(0,len(filled_slots[i])):
        print(filled_slots[i][val])
        filled_slots[i][val] = 'try'
print(filled_slots)
-------------------------------------------------------------------
'''

'''
PAGE_C = nel.Grid().addFolderPage(PAGE_A, page_c)
PAGE_B = nel.Grid().addFolderPage(PAGE_A, page_b)

print('\nPAGE_A :')
print(PAGE_A)
print('\nPAGE_B :')
print(PAGE_B)
print('\nPAGE_C :')
print(PAGE_C)
'''





core_vocabulary = [['je', 0, 1], ['vouloir', 0, 0], ['aimer', 1, 0], ['quoi', 1, 1], ['pourquoi', 2, 3], ['ici', 1, 3]]
slots = [[0,5,'voyage'], [1, 2, 'patron'], [2, 4, 'regarder'], [0, 2, 'écouteurs'], [0,3, 'stylo'], [2,2, 'ordinateur'], [1,4,'crème'], [2,1, 'comprendre'], [1,5, 'marché'], [0,4, 'téléphoner'], [2,0, 'lire'], [2,5, 'prise']]
items = [x[2] for x in slots]
