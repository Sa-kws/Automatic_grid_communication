class Item():

    def __init__(self, word):
        self.word = word

    @property
    def isCore(self):
        return self.word in Grid.CORE_VOCABULARY


    def addItem(self, is_core):
        slot = []
        slot.append(self)
        slot.append(is_core)
        return slot

'''
class Slot():
    def __init__(self):
        self.Slot = self
'''

class Page():
    ROW_SIZE = 3
    COL_SIZE = 5
    WARNING_MESSAGE = 'PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.'

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
                return cls.WARNING_MESSAGE #'PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.'
        return tableau

    def isOccupied(self, row, col, page):
        return page[row][col][0] != None
            # Si la position n\'est PAS None (donc remplie), la propriété Page().occupied est True

    def lastFilled(self, next_slot_condition):
        # next_slot_condition = si le prochain
        if next_slot_condition == True:
            last_filled = []
            last_filled.append(row)
            last_filled.append(col)
        return last_filled

    def isFull(self, page):
        previous = True
        for row in range(0,len(page)):
            for col in range (0, len(page[row])):
                if page[row][col][0] == None:
                    previous = False
                    return False
        return True

    def isWellSized(self, page):
        return Page.WARNING_MESSAGE not in page

    def addSlot(self, page, row, col, item):
        # item = word de la classe Item()
        # page = tableau créé via Page()
        page[row][col] = [item, row, col]
        return page

class Grid():
    PAGES = []
    CORE_VOCABULARY = ['je', 'vouloir', 'quoi', 'pourquoi']
    LISTE_CORE = [['je', 0, 1], ['vouloir', 0, 0], ['quoi', 1, 1], ['pourquoi', 0, 3]]
    def __init__(self):
        self.Grid = Grid

    def addPage(self, grid, page):
        grid.append(page)
        return grid

    def makeGrid(self, item, word, used_words, page, grid):
        # Si le word est un voc core, on s'arrête là, puisqu'il sera déjà placé sur la page
        if item.isCore == False and word not in used_words:
            # Vérification qu'il reste de la place sur la page
            # Parcours de la page, et recherche des position vide via la méthode Page().isOccupied() (True ou False) dans la page créée
            for row_browse in range(0, len(page)):
                for col_browse in range(0, len(page[row_browse])):
                    if Page.isOccupied(Page(), row_browse, col_browse, page) == False and word not in used_words:
                        page = Page.addSlot(Page, page, row_browse, col_browse, item.word)
                        used_words.append(item.word)
        return grid

    def finishGrid(self, page, grid):
        if page not in grid:
            grid = Grid.addPage(Grid, grid, page)
        return grid

    def showGrid(self, grid):
        return grid

    def addUnfulledPage(*self, grid, page, used_words, word, item):
        grid = Grid.addPage(Grid, grid, page)
        page = Page()
        for row in range(0, len(page)):
            for col in range(0, len(page[row])):
                if Page.isOccupied(Page(), row, col, page) == False and word not in used_words:
                    page = Page.addSlot(Page, page, row, col, item.word)
                    used_words.append(word)
                    break
            break
        return grid


Class Preprocess:
    
    def addCoreWords(self, in_datas, used_words):
        stockage_intermediaire = []
        for word in in_datas:
            if Item(word).isCore == True and word not in used_words:
                used_words.append(word)
        return used_words
