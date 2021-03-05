from word2grid import page_par_liste as nel


phrase = 'je suis stagiaire et quoi je ai un stylo et puis je suis aussi un peu pourquoi pas et puis voilà quoi aussi Grenoble c\' loin de Dreux mince ça ne convient pas comme ça'
#phrase = ''
phrase = phrase.split(' ')


grid = nel.Grid().PAGES
page = nel.Page()
used = []

for word in phrase:
    if nel.Page.isWellSized(nel.Page, page) == False:
        print('La taille de la grille n\'est pas adaptée aux positions attribuées au vocabulaire Core. Merci de repositionner le vocabulaire Core, ou changer la taille de la grille.\nLe programme va s\'arrêter.')
        break
    else:
        # Création d'un item, ajout de l'item à un slot, avec la propriété Item().isCore (True ou False)
        item = nel.Item(word)
        slot = nel.Item.addItem(item.word, item.isCore)
        # Si le word est un voc core, on s'arrête là, puisqu'il sera déjà placé sur la page
        if item.isCore == False and word not in used:
            # Vérification qu'il reste de la place sur la page
            if nel.Page.isFull(nel.Page, page) == False:
                # Parcours de la page, et recherche des position vide via la méthode Page().isOccupied() (True ou False) dans la page créée
                for row_browse in range(0, len(page)):
                    for col_browse in range(0, len(page[row_browse])):
                        if nel.Page.isOccupied(nel.Page(), row_browse, col_browse, page) == False and word not in used:
                            page = nel.Page.addSlot(nel.Page, page, row_browse, col_browse, item.word)
                            used.append(item.word)

            else:
                grid.append(page)
                page = nel.Page()
                for row in range(0, len(page)):
                    for col in range(0,len(page[row])):
                        if nel.Page.isOccupied(nel.Page(), row, col, page) == False and word not in used:
                            page = nel.Page.addSlot(nel.Page, page, row, col, item.word)
                            used.append(word)
                            break
                    break


if page not in grid:
    grid.append(page)
print('LAST PRINT :', grid)
