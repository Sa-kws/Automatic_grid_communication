from word2grid import Page
from word2grid import Slot
from word2grid import Grid

def main(*self, in_datas):
    ID = 0
    name = 'Page_' + str(ID)
    p = Page.Page(3,4)
    p = p.createPage()

    used_words = []
    print(dir(Grid))
    g = Grid.Grid()
    grid = g.classeur

    # Proposition à l'utilisateur de modifier le Vocabulaire Core
    g.LISTE_CORE = g.setCoreVoc()
    print(g.LISTE_CORE)


    # Vérification de la taille de la grille
    if p.isWellSized() == False:
        print(p._Page__WARNING_MESSAGE)
        print('Le programme va s\'arrêter.')
    else:
        # Création de la grille avec les valeurs d'entrée
        for ligne in in_datas:
            word = ligne[0]
            iscore = ligne[1]
            path = ligne[2]
            # folder_datas = open(word + '.txt', 'r', encoding='utf-8')
            if path != None:
                folder_datas = ['folder_page', word, 'folder_datas', '...']
                g = g.addFolderPage(path=path, folder_datas=folder_datas, grid=g, ID=ID)
            g = g.makeGrid(page=p, used_words=used_words, grid=g.classeur, ID=ID, word=word, iscore=iscore)
            print('\tConstruction de la grille')
        print('PB ICI ?????')
        g.classeur = g.finishGrid(page=p)
        print('Grille finie')
    return self
