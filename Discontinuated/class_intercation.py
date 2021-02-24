import numpy as np

class Grid:
    def __init__(self):
        self.Grid = self

class Page:
    GRID_ROW = 2
    GRID_COL = 4
    GAP_SIZE = 1
    def __init__(self):
        self.Page = self

    def makePage(self, name):
        return 'Page_' + name, np.zeros(shape=(self.GRID_ROW, self.GRID_COL), dtype=str)
    # Initialisation d'une page avec les positions d'items (2 lignes / 4 colonnes) de type str

    def makeSentence():
        pass
    # OR
    def clickItem():
        pass

    def openPage():
        pass


class GridElement:
    TYPE = str
    COLUMNS = Page.GRID_COL
    ROWS = Page.GRID_ROW
    #FOLDER = [x if x is dossier for x in open(liste_folder, 'r')]

    # Pour avoir la position d'un item il faut parcourir une liste et créer une position
    # Row_1xCol_1 ; Row_1xCol_2 ; ... et y ajouter un item

    def __init__(self):
        self.GridElement = self

    def affiche():
        print('This is working')

    def createPosition(self):
        self.itemize = self.GridElement
        grid_pos = []
        for row in range(0, self.ROWS):
            for col in range(0, self.COLUMNS):
                inter = []
                inter.append(row + 1)
                inter.append(col + 1)
                grid_pos.append(inter)
        return grid_pos
    # retourne une liste des positions possibles sur une page

    def addItem(self, list_position):
        # list_position = grid_pos (createPosition). Il faut passer en paramètre la variable
        # dans laquelle on stock le résultat de createPosition
        liste_items = []
        for pos in list_position:
            inter = []
            # for word in liste_lemme ESLO
            inter.append('word')
            inter.append(pos)
            liste_items.append(inter)
        return liste_items
    # retourne une liste d'items associés à une position


grid = GridElement()
position = grid.createPosition()
items = grid.addItem(position)

print(grid, '\n\n', position, '\n\n', items)

def main():
    words=[]
    for i in open('Decoded_ESLO_vocab.txt',encoding='utf-8'):
        if i == '\n':
            pass
        else:
            word = i.split('\'')
            words.append(word[1])
main()