from word2grid import Page
from word2grid import Slot # Méthode fillPageWithCore()

class Grid():
    PAGES = []
    CORE_VOCABULARY = ['je', 'vouloir', 'quoi', 'pourquoi'] # Devrait être modifé
    LISTE_CORE = [['je', 0, 1], ['vouloir', 0, 0], ['quoi', 1, 1], ['pourquoi', 1, 0]] # Devrait être modifié

    def __init__(self):
        self.classeur = []



    def fillPageWithCore(self, page):
        for core_vocab in page.core_vocab:
            row = core_vocab[3]
            col = core_vocab[4]
            try:
                page.tableau[row][col] = core_vocab
            except IndexError:
                page.tableau.append(page.__WARNING_MESSAGE)
        return page


    def fillPage(self, slot, page, used_words):
        for row in range(0, len(page.tableau)):
            for col in range(0, len(page.tableau[row])):
                if page.isOccupied(row, col) == False and slot.get_word() not in used_words:
                    page = page.addSlotToPage(slot.get_word(), row, col)
                    last_position = pos = [row, liste.index(slot.get_word())]
                    used_words.append(slot.get_word())

        return page

    def fillClasseur(self, page):
        self.PAGES.append(page)
        return self

    def makeGrid(self, page, used_words, slot):
        if page.isFull() == False:
            page = self.fillPage(slot, page, used_words)
        # Quand la page est pleine, on utilise la méthode Grid().addFulledPage()
        else:
            self = self.fillClasseur(page)
            page = Page.Page()
            page = page.createPage()

        return self, page
