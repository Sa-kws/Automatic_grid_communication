import pandas
import re

class Grid():
    PAGES = []
    SLOTS = []
    LISTE_CORE = ['je', 'vouloir', 'aimer', 'quoi']
    def __init__(self):
        self.Grid = Grid
        self.LISTE_CORE = ['je', 'vouloir', 'aimer', 'quoi']

    # Ajout d'une page ouverte via un dossier
    def addFolderPage(self, page_source, page_target):
        # page_source = df contenant les slots item + le slot dossier
        # page_target = df contenant les slots du dossier qu'on voudrait ouvrir
        regex = r'[A-Z]{1}[0-9]{2}_F-[bc]'
        fin = False
        for i in page_source.columns:
            for val in range(0, len(page_source[i])):
                if re.fullmatch(regex, page_source[i][val]):
                    new_page_folder = Page().addSlots(page_target, Page().makePage())
                    fin = True
                    page_source[i][val] = page_source[i][val].lower().replace('_f-c','').replace('_f-b','')
                    break
            if fin == True:
                break
        return new_page_folder

    # Ajout d'un ensemble de pages qui seront passées en arguments
    def addPages(self):
        pass

    def export_to_csv(self, grid, name):
        name = 'page_'
        num = 1
        for page in grid:
            name = name + str(num)
            num += 1
            df = page
            pandas.df.to_csv(name, sep='\t')


class Page():
    SLOTS = Grid.SLOTS

    def __init__(self):
        self.Page = Page

    def makePage(self):
        return pandas.DataFrame(columns=[str(x + 1) for x in range(0, Slot.COL_NUMBER)], index=range(Slot.ROW_NUMBER)).astype(str)

    def addSlots(self, slots, page):
        # Il faut passer en argument une liste de Slot, on les mettra ensuite dans un tableau
        # Possiblement : DataFrame - pandas
        # Il faut aussi passer une une page, qui correspond à un df qu'on aura créé avec la méthode makePage()
        df = page
        for col in df:
            to_use = []
            to_use = [slots[i] for i in range(0, Slot.ROW_NUMBER)]
            #print('--- TO_USE : ', to_use)
            df[col] = [x for x in to_use]
            del slots[0:Slot.ROW_NUMBER]
        Grid.PAGES.append(df)
        return df
    # On passe en argument (slots) la liste de slots qu'on souhaite ajouter à la page, ensuite,
    # on initialise une liste (to_use) dans laquelle on ajoute le nombre de slots par colonne selon le nombre
    # de ligne (Slot.ROW_NUMBER). Ensuite, on parcours to_use pour remplir la colonne du DataFrame.
    # Une fois la colonne remplie, on supp les slots déjà ajoutés de la liste de slots originale pour ne pas
    # les reprendre dans to_use.
    # ?? (On pourrait copier la liste dans la fonction afin de ne pas toucher l'originale)


class Slot():
    ROW_NUMBER = 3
    COL_NUMBER = 6
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
    #PAGE_DESTINATION = Grid.addPage()
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
