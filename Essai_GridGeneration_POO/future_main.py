from word2grid import new_elements as nel

c = 0
for i in open('page_a.txt', encoding='utf-8'):
    c += 1
case = nel.Grid.ROW_SIZE * nel.Grid.COL_SIZE

if case == c:
    items = []
    for word in open('page_a.txt', encoding='utf-8'):
        item = nel.Item(word.replace('\n', ''))
        str_item = item.makeItem()
        items.append(word.replace('\n',''))

    page = nel.Page()
    #page = page.addSlots(items, page.makePage())
    slots = nel.Slot()
    slots = slots.addItem(items)
    good_order = page.switch(nel.Grid.LISTE_CORE, slots)




elif case > c:
    print('Il n\'y a pas assez de mots dans le fichier. Il y manque',case - c, 'mots pour compléter la page.')
else:
    print('Il y a trop de mots dans le fichier. Il y a', c - case, 'mots en trop par rapport aux positions disponibles sur la page.')
