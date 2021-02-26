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
vocab = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'A14_F-c', 'a15', 'a16', 'a17', 'A18_F-b']



from word2grid import new_elements as nel

# ---------- Futur main() : ----------

item = nel.Item('vouloir')
item = item.makeItem()
print(item)
slot = nel.Slot(3,2)
print(slot.position)
slotitem = slot.addItem(slot.position, item)
print(slotitem)
page = nel.Page().makePage()
filled_slots = nel.Page().addSlots(vocab, page)

print(filled_slots)



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
