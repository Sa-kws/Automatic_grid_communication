from word2grid import page_par_liste as nel


phrase = 'je suis stagiaire et quoi je ai un stylo'
phrase = phrase.split(' ')




page = nel.Page().makePage()

row_to_fill = 0
col_to_fill = 0
used = []
for word in phrase:
    # Création d'un item, ajout de l'item à un slot, avec la propriété Item().isCore (True ou False)
    item = nel.Item(word)
    slot = nel.Slot().addItem(item.word, item.isCore)
    # Si le word est un voc core, on s'arrête là, puisqu'il sera déjà placé sur la page
    if item.isCore == False:
        # Parcours de la page, et recherche des position vide dans la page créée via la méthode Page().isOccupied() (True ou False)
        for row_browse in range(0, len(page)):
            for col_browse in range(0, len(page[row_browse])):
                if nel.Page.isOccupied(nel.Page(), row_browse, col_browse, page) == False and word not in used:
                    page[row_browse][col_browse] = [word, row_browse, col_browse]
                    used.append(word)

grid = nel.Grid().addPage(page)
print(grid)
print(nel.Page.isFull(nel.Page(), page))