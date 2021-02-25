import pandas as pd

class Grid():
    PAGES = []
    SLOTS = []
    LISTE_CORE = ['je', 'vouloir', 'aimer', 'quoi']
    def __init__(self):
        self.Grid = Grid
        self.LISTE_CORE = ['je', 'vouloir', 'aimer', 'quoi']

    # Ajout d'un ensemble de pages qui seront passées en arguments
    def addPage():
        pass


class Page():
    SLOTS = Grid.SLOTS

    def __init__(self):
        self.Page = Page

    def makePage(self):
        return pd.DataFrame(columns=[str(x + 1) for x in range(0, Slot.COL_NUMBER)], index=range(Slot.ROW_NUMBER)).astype(str)

    def addSlots(self, slots, page):
        # Il faut passer en argument une liste de Slot, on les mettra ensuite dans un tableau
        # Possiblement : DataFrame - pandas
        # Il faut aussi passer une une page, qui correspond à un df qu'on aura créé avec la méthode makePage()
        df = page
        for col in df.columns:
            print(col)
            used_words = []
            # Erreur : le df se rempli entièrement avec un mot, puis recommence avec le suivant ect...
            for word in slots:
                if word in used_words:
                   pass 
                else:
                    used_words.append(word)
                    df[col] = word
        return df


class Slot():
    ROW_NUMBER = 6
    COL_NUMBER = 3
    ITEM_IS_CORE = False
    def __init__(self, row_num, col_num):
        # ceci implique que le numéro de la ligne et de la colonne doit être passé en argument lorsque l'on créé la clase
        # Type : int
        # Exemple : slot = Slot(3,2)
        self.Slot = Slot
        self.ROW_NUMBER = row_num
        self.COL_NUMBER = col_num

    @property
    # Manque le mot positionné, chercher comment l'ajouter
    # Initialement : Item.WORD en argument, après Self, mais retourne l'argument de la Classe, et non de l'objet instancié
    # Puis essai avec item.WORD en argument également, fonctionne, mais en fonction, non en propriété
    def position(self):
        position = []
        position.append(self.ROW_NUMBER)
        position.append(self.COL_NUMBER)
        #position.append(item.WORD)
        return position # Retourne une liste

    # Il faut passer l'item qu'on veut ajouter au slot en argument
    def addItem(self, position, item):
        # position est une liste de position, pas nécessairement issue de la propriété de la classe
        # Exemple : [4,8] avec 4 = Rows ; 8 = Columns
        filled_slot = position
        filled_slot.append(item)
        return filled_slot # Retourne une liste avec [row, column, word]



    # Sert à créer une liste de slots, qu'on passera en argument à la méthode addSlots() de la classe Page()
    def groupSlots(self):
        pass
    # A voir si on ne peut pas créer la liste dans le script final, dans lequel on pourrait faire
    # open(fichier) for mot in fichier:
    #       créer un item en passant les mots un par un en argument
    #       mettre l'item dans un slot
    #       ajouter ce slot à une liste

class Item():
    WORD = ''
    PAGE_DESTINATION = Grid.addPage()
    def __init__(self, word):
        self.Item = Item
        self.WORD = word
        # ceci implique que le word doit être passé en argument lorsque l'on créé la clase
        # Exemple : item = Item('mot d'exemple')

    def makeItem(self):
        item = self.WORD
        #print('item is : \'' + item + '\'')
        return item # Return str

    @property
    def isCore(self):
        if self.WORD in Grid.LISTE_CORE:
            return True
        else:
            return False
