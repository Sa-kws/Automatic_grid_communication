from word2grid import Slot

class Page():
    __ROW_SIZE = 3
    __COL_SIZE = 4
    __WARNING_MESSAGE = 'PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.'

    def __init__(self):
        self.tableau = []
        #self.__ROW_SIZE = row
        #self.__COL_SIZE = col
        self.__slots = []
        self.core_vocab = []


    def addSlots(self, slot, row, col):
        # slot = [word, core, path]
        if slot.get_is_core() == True:
            to_core = [slot.get_word(), slot.get_is_core(), slot.get_page_destination(), row, col]
            self.core_vocab.append(to_core)
        else:
            to_tableau = [slot.get_word(), slot.get_is_core(), slot.get_page_destination(), row, col]
            self.__slots.append(to_tableau)
        return self

    def createPage(self):
        for i in range(0, self.__ROW_SIZE):
            entre = []
            for j in range(0, self.__COL_SIZE):
                entre.append([None])
            self.tableau.append(entre)

        for core_vocab in self.core_vocab:
            row = core_vocab[3]
            col = core_vocab[4]
            try:
                self.tableau[row][col] = core_vocab
            except IndexError:
                self.tableau.append(self.__WARNING_MESSAGE)
                return self
        return self


    def isWellSized(self):
        return self.__WARNING_MESSAGE not in self.tableau


    def isFull(self):
        for row in range(0,len(self.tableau)):
            for col in range (0, len(self.tableau[row])):
                if self.tableau[row][col][0] == None:
                    return False
        return True

    def isOccupied(self, row, col):
        return self.tableau[row][col][0] != None

    def addSlotToPage(self, slot, row, col):
        self.tableau[row][col] = [slot, row, col]
        return self
