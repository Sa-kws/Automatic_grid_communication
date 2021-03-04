class Item():

    def __init__(self, word):
        self.word = word

    @property
    def isCore(self):
        if self.word in Grid.CORE_VOCABULARY:
            return True
        else:
            return False

class Slot():
    def __init__(self):
        self.Slot = self

    def addItem(self, item, is_core):
        slot = []
        slot.append(item)
        slot.append(is_core)
        return slot

class Page():
    ROW_SIZE = 10
    COL_SIZE = 10
    def __init__(self):
        self.Page = Page

    def __new__(cls):
        tableau = []
        for i in range(0, cls.ROW_SIZE):
            entre = []
            for j in range(0, cls.COL_SIZE):
                entre.append([None])
            tableau.append(entre)

        for core_vocab in Grid.LISTE_CORE:
            row = core_vocab[1]
            col = core_vocab[2]
            try:
                tableau[row][col] = core_vocab
            except IndexError:
                #print('PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.')
                return 'PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.'
        return tableau


    def isOccupied(self, row, col, page):
        #last_unfilled = []
        if page[row][col][0] != None:
            # Si la position n\'est PAS None (donc remplie), la propriété Page().occupied est True
            return True
        else:
            #last_unfilled.append(row)
            #last_unfilled.append(col)
            return False


    def isFull(self, page):
        previous = True
        for row in range(0,len(page)):
            for col in range (0, len(page[row])):
                if page[row][col][0] == None:
                    previous = False
                    return False
        return True


class Grid():
    PAGES = []
    CORE_VOCABULARY = ['je', 'vouloir', 'quoi', 'pourquoi']
    LISTE_CORE = [['je', 0, 1], ['vouloir', 0, 0], ['quoi', 1, 1], ['pourquoi', 0, 3]]
    def __init__(self):
        self.Grid = Grid

    def addPage(self, page):
        Grid.PAGES.append(page)
        return Grid.PAGES
