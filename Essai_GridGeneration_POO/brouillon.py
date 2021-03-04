from word2grid import page_par_liste as nel


phrase = 'je suis stagiaire et quoi je ai un stylo et puis je suis aussi un peu pourquoi pas et puis voilà quoi aussi Grenoble c\' loin de Dreux vraiment'
phrase = phrase.split(' ')


grid = nel.Grid().PAGES
page = nel.Page().makePage()


row_to_fill = 0
col_to_fill = 0
used = []

warning_message = 'PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.'
for word in phrase:
    if warning_message in page:
        print('La taille de la grille n\'est pas adaptée aux positions attribuées au vocabulaire Core. Merci de repositionner le vocabulaire Core, ou changer la taille de la grille.')
        print('Le programme va s\'arrêter.')
        break
    else:
        # Création d'un item, ajout de l'item à un slot, avec la propriété Item().isCore (True ou False)
        item = nel.Item(word)
        slot = nel.Slot().addItem(item.word, item.isCore)
        # Si le word est un voc core, on s'arrête là, puisqu'il sera déjà placé sur la page
        if item.isCore == False:
            # Vérification qu'il reste de la place sur la page
            if nel.Page.isFull(nel.Page(), page) != True:
                # Parcours de la page, et recherche des position vide via la méthode Page().isOccupied() (True ou False) dans la page créée
                for row_browse in range(0, len(page)):
                    for col_browse in range(0, len(page[row_browse])):
                        if nel.Page.isOccupied(nel.Page(), row_browse, col_browse, page) == False and word not in used:
                            page[row_browse][col_browse] = [word, row_browse, col_browse]
                            used.append(word)
            else:
                # save page
                grid.append(page)
                # initialiser une nouvelle page
                page = nel.Page().makePage()
        if grid == []:
            grid.append(page)
