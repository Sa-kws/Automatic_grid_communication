import numpy as np
import pandas as pd
class Page():
    ROWS = 3
    COLUMNS = 6
    def __init__(self):
        self.Page = Page

    def makePage(self):
        #return np.zeros(shape=(self.ROWS, self.COLUMNS), dtype=str)
        return pd.DataFrame(columns=[x + 1 for x in range(0, self.COLUMNS)], index=range(self.ROWS)).astype(str)


class Slot():
    SLOTS = ['SLOT' for x in range(0,3)]
    def __init__(self):
        self.Slot = Slot

    def addSlots(self, page):
        support = page
        # l'argument page correspond à l'objet Page() créé par la fonction Page.makePage()
        for i in support:
            support[i] = [x for x in self.SLOTS]
        return support
    # Remplace les valeurs du DataFrame créé par Page.makePage() par la valeur 'SLOT'

class item():
    pass

class Button():
    pass

class Grid():
    pass

class Folder():
    CLICK = True
    def openPage(self, name):
        #name == str, nom du dossier, servira à nommer la nouvelle page
        if self.CLICK == True:
            name = Page.makePage(Page())
            name = Slot.addSlots(Slot(), name)
        return name
