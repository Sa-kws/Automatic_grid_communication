from word2grid import page_par_liste as nel


phrase = 'je suis stagiaire et quoi je ai un stylo et puis je suis aussi un peu pourquoi pas et puis voilà quoi aussi Grenoble c\' loin de Dreux mince ça ne convient pas comme ça'
phrase = phrase.split(' ')

with open('Fichier_exemple.txt', 'r', encoding='utf-8') as f:
    corpus = [x.replace('\n', '').lower().split('\t') for x in f]


grid = nel.Grid().PAGES
page = nel.Page()
used = []
used = nel.Preprocess.addCoreWords(nel.Preprocess, phrase, used)

for i in corpus:
    print(i)
    word = i[0]
    if nel.Page.isWellSized(nel.Page, page) == False:
        print('La taille de la grille n\'est pas adaptée aux positions attribuées au vocabulaire Core. Merci de repositionner le vocabulaire Core, ou changer la taille de la grille.\nLe programme va s\'arrêter.')
        break
    else:
        item = nel.Item(word)
        slot = nel.Item.addItem(item.word, item.isCore)
        if nel.Page.isFull(nel.Page, page) == False:
            grid = nel.Grid.makeGrid(nel.Grid, item, word, used, page, grid)
        else:
            grid = nel.Grid.addUnfulledPage(grid=grid, page=page, used_words=used, word=word, item=item)
            page = nel.Page()
    if '-r' in i[2]:
        page = nel.Page()
        with open(i[2]+'.txt', 'r') as page_words:
            for word_r in page_words:
                if nel.Page.isWellSized(nel.Page, page) == False:
                    print('La taille de la grille n\'est pas adaptée aux positions attribuées au vocabulaire Core. Merci de repositionner le vocabulaire Core, ou changer la taille de la grille.\nLe programme va s\'arrêter.')
                    break
                else:
                    item = nel.Item(word_r)
                    slot = nel.Item.addItem(item.word, item.isCore)
                    if nel.Page.isFull(nel.Page, page) == False:
                        grid = nel.Grid.makeGrid(nel.Grid, item, word_r, used, page, grid)
                    else:
                        grid = nel.Grid.addUnfulledPage(grid=grid, page=page, used_words=used, word=word, item=item)
                        page = nel.Page()


grid = nel.Grid.finishGrid(nel.Grid, page, grid)
print(nel.Grid.showGrid(nel.Grid, grid))
