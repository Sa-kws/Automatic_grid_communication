class Slot():

    def __init__(self, word, isCore):
        # word = str que l'on souhaite traiter et placer sur la grille
        # is Core = Booléen un indiquant si le mot traité fait parti du vocabulaire core ou non
        self.word = word
        self.isCore = isCore

    def addItem(self, is_core):
        slot = []
        slot.append(self)
        slot.append(is_core)
        return slot

    @property
    def openFolder(self, path_to_folder):
        if path_to_folder != None:
            return path_to_folder
        else:
            return None

class Page():
    ROW_SIZE = 3
    COL_SIZE = 4
    WARNING_MESSAGE = 'PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.'
    def __init__(self):
        self.Page = Page

    def __new__(cls, ID, name):
        tableau = []
        cls.ID = ID
        #tableau.append([ID, name])
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
    LISTE_CORE = [['je', 0, 1], ['vouloir', 0, 0], ['quoi', 1, 1], ['pourquoi', 1, 0]]
    def __init__(self):
        self.Grid = Grid


    def addPage(self, core, word, used_words, page, grid):
        # Si le word est un voc core, on s'arrête là, puisqu'il sera déjà placé sur la page
        if core == False and word not in used_words:
            # Vérification qu'il reste de la place sur la page
            # Parcours de la page, et recherche des position vide via la méthode Page().isOccupied() (True ou False) dans la page créée
            for row_browse in range(0, len(page)):
                for col_browse in range(0, len(page[row_browse])):
                    if Page.isOccupied(Page, row_browse, col_browse, page) == False and word not in used_words:
                        page = Page.addSlot(Page, page, row_browse, col_browse, word)
                        used_words.append(word)
        return grid

    def finishGrid(*self, page, grid):
        if page not in grid:
            grid.append(page)
        return grid

    def addFulledPage(*self, ID, grid, page, used_words, word):
        grid.append(page)
        page = Page(ID, 'test-')
        for row in range(0, len(page)):
            for col in range(0, len(page[row])):
                if Page.isOccupied(Page, row, col, page) == False and word not in used_words:
                    page = Page.addSlot(Page, page, row, col, word)
                    used_words.append(word)
                    break
            break
        return grid

    def addFolderPage(*self, path, folder_datas, grid, ID):
        used_words = []
        # On commence par vérifier que le mot n'ouvre pas un dossier, si c'est le cas, on créé la page.
        if path != None:
            ID += 1
            name = 'Page_' + str(ID)
            folder_page = Page(ID, name)
            for word in folder_datas:
                grid, page = Grid.makeGrid(page=folder_page, used_words=used_words, grid=grid, ID=ID, word=word, iscore=False)


            grid = Grid.finishGrid(page=folder_page, grid=grid)
        return grid

    def makeGrid(*self, page, used_words, grid, ID, iscore, word):
            if Page.isFull(Page, page) == False:
                grid = Grid.addPage(Grid, iscore, word, used_words, page, grid)
            else:
                grid = Grid.addFulledPage(ID=ID, grid= grid, page=page, used_words=used_words, word=word)
                ID += 1
                name = 'Page_' + str(ID)
                page = Page(ID, name)

            return grid, page

class Preprocess:
    
    def addCoreWords(self, in_datas, used_words):
        stockage_intermediaire = []
        for word in in_datas:
            if Slot(word).isCore == True and word not in used_words:
                used_words.append(word)
        return used_words

def main(in_datas):
    ID = 0
    name = 'Page_' + str(ID)
    page = Page(ID, name)

    used_words = []
    grid = Grid().PAGES

    if Page.isWellSized(Page, page) == False:
        print(Page.WARNING_MESSAGE)
        print('Le programme va s\'arrêter.')
    else:
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

#def if __name__ == '__main__':
#    main()