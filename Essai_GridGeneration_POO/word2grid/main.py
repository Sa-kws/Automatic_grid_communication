from word2grid import Page
from word2grid import Slot
from word2grid import Grid
def main(in_datas):
    ID = 0
    name = 'Page_' + str(ID)
    page = Page.Page(ID, name)

    used_words = []
    grid = Grid().PAGES

    # Proposition à l'utilisateur de modifier le Vocabulaire Core
    Grid.LISTE_CORE = Grid.setCoreVoc()


    # Vérification de la taille de la grille
    if Page.isWellSized(Page, page) == False:
        print(Page.WARNING_MESSAGE)
        print('Le programme va s\'arrêter.')
    else:
        # Création de la grille avec les valeurs d'entrée
        for ligne in in_datas:
            word = ligne[0]
            iscore = ligne[1]
            path = ligne[2]
            # folder_datas = open(word + '.txt', 'r', encoding='utf-8')
            folder_datas = [word]
            grid = Grid.addFolderPage(path=path, folder_datas=folder_datas, grid=grid, ID=ID)
            grid, page = Grid.makeGrid(page=page, used_words=used_words, grid=grid, ID=ID, word=word, iscore=iscore)
        grid = Grid.finishGrid(page=page, grid=grid)
    return grid
