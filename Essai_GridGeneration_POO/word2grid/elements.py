import pandas
import re

class Grid():
    PAGES = []
    SLOTS = []
    ROW_SIZE = 3
    COL_SIZE = 6
    LISTE_CORE = [['je', 0, 2], ['vouloir', 0, 1], ['aimer', 1, 1], ['quoi', 1, 2]]

    def __init__(self):
        self.Grid = Grid


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

    # A revoir
    def export_to_csv(self):
        #os.mkdir("Classeurs")
        num = 1
        for page in self.PAGES:
            name = 'page_'
            name = name + str(num)
            num += 1
            df = page
            writer = pandas.ExcelWriter(path='Grid_sheets.xlsx',engine=None)
            df.to_excel('Grid_sheets.xlsx', sheet_name=name)
            '''DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None,
                               header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None,
                               merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None,
                               storage_options=None)'''


class Page():
    SLOTS = Grid.SLOTS

    def __init__(self):
        self.Page = Page
        print('\t📜 La page est créée. 📜')

    # Retourne une page (pandas.df) intégrant le vocabulaire core.
    # Pour le moment, le vocab est figé et limité, à réfléchir
    def makePage(self):
        df = pandas.DataFrame(columns=[str(x + 1) for x in range(0, Grid.COL_SIZE)], index=range(Grid.ROW_SIZE)).astype(str)
        row = 0
        core = []
        for cr in Grid.LISTE_CORE:
            core.append(cr[0])
        for i in df.iterrows():
            row += 1
            col = 0
            for val in range(0, len(i[1])):
                col += 1
                if col < 3 and row < 2:
                    try:
                        df[str(col)][0, 1] = core[0], core[1]
                        del core[0:2]
                    except IndexError:
                        return False
        return df

    def switch(self, liste_core, liste_vocab):
        to_switch = []
        index_core = 0
        for core_vocab in liste_core:
            row_core = core_vocab[1]
            col_core = core_vocab[2]
            index_voc = 0
            for normal_vocab in liste_vocab:
                row_normal = normal_vocab[0]
                col_normal = normal_vocab[1]
                if row_core == row_normal and col_core == col_normal:
                    to_switch.append(normal_vocab[2])
                    liste_vocab[index_voc][2] = liste_core[index_core][0]
                index_voc += 1
            index_core += 1
        for swtch in to_switch:
            for corvoc in liste_core:
                if corvoc[0] == swtch:
                    pass
        x = 0
        
        # ➰➰➰➰---------Reprendre ICI-----------❌❌
        core_vocabulary = []
        for r in liste_core:
            core_vocabulary.append(r[0])
        

        for word in liste_vocab:
            if word[2] in core_vocabulary:
                print(word)
                '''if to_switch[0] not in core_vocabulary:
                    liste_vocab[x][2] = liste_vocab[x][2].replace(liste_vocab[x][2], '🟠🟠')
                del to_switch[0]'''
            x += 1
        print(liste_vocab)
        # ➰➰➰➰--------------------❌❌


    def addSlots(self, slots, page):
        # Il faut passer en argument une liste de Slot, on les mettra ensuite dans un tableau
        # Possiblement : DataFrame - pandas
        # Il faut aussi passer une une page, qui correspond à un df qu'on aura créé avec la méthode makePage()
        df = page
        core = []
        for x in Grid.LISTE_CORE:
            core.append(x[0])
        for col in df:
            #for val in df[col]:
               # if val != 'nan' and val not in Grid.LISTE_CORE:
            #to_use = [slots[i][2] if slots[i][2] not in core else core[core.index(slots[i][2])] for i in range(0, Grid.ROW_SIZE)]
            to_use = []
            for i in range(0, Grid.ROW_SIZE):
                if slots[i][2] not in core:
                    to_use.append(slots[i][2])
                else:
                    to_use.append(core[core.index(slots[i][2])])
                    del core[core.index(slots[i][2])]
            df[col] = [x for x in to_use]
            del slots[0:Grid.ROW_SIZE]
        Grid.PAGES.append(df)
        return df
    # On passe en argument (slots) la liste de slots qu'on souhaite ajouter à la page, ensuite,
    # on initialise une liste (to_use) dans laquelle on ajoute le nombre de slots par colonne selon le nombre
    # de ligne (Slot.ROW_NUMBER). Ensuite, on parcours to_use pour remplir la colonne du DataFrame.
    # Une fois la colonne remplie, on supp les slots déjà ajoutés de la liste de slots originale pour ne pas
    # les reprendre dans to_use.
    # ?? (On pourrait copier la liste dans la fonction afin de ne pas toucher l'originale)


class Slot():
    LISTE_SLOTS = []
    def __init__(self):#, row_num, col_num):
        # ceci implique que le numéro de la ligne et de la colonne doit être passé en argument lorsque
        # l'on créé la clase
        # Type : int
        # Exemple : slot = Slot(3,2)
        self.Slot = Slot
        #self.ROW_NUMBER = row_num
        #self.COL_NUMBER = col_num

    @property
    # Manque le mot positionné, chercher comment l'ajouter
    # Initialement : Item.WORD en argument, après Self, mais retourne l'argument de la Classe, et non de l'objet instancié
    # Puis essai avec item.WORD en argument également, fonctionne, mais en fonction, non en propriété
    def position(self):
        position = []
        position.append(Grid.ROW_SIZE)
        position.append(Grid.COL_SIZE)
        #position.append(item.WORD)
        return position # Retourne une liste

    # Il faut passer l'item qu'on veut ajouter au slot en argument
    def addItem(self, item_list):
        # position est une liste de position, pas nécessairement issue de la propriété de la classe
        # Exemple : [4,8] avec 4 = Rows ; 8 = Columns
        # item must be list
        position = []
        if len(item_list) == Grid.ROW_SIZE * Grid.COL_SIZE:
            pos = 0
            row = 0
            while row < Grid.ROW_SIZE:
                col = 0
                while col < Grid.COL_SIZE:
                    inter = []
                    col += 1
                    inter.append(row)
                    inter.append(col)
                    inter.append(item_list[pos])
                    self.LISTE_SLOTS.append(inter)
                    pos += 1
                row += 1

            print('\tL\'item est associé au slot, et ajouté à la liste de slots.')
            return self.LISTE_SLOTS  # Retourne une liste de position comprenant une liste avec [row, column, word]
        else:
            return '❌❌--- Il n\'y a pas le même nombre d\'items et de slots. ---❌❌\n\t--> Aucun item n\'a été ajouté à la liste.'



    @property
    def slots(self):
        slts = []
        for slt in Slot.LISTE_SLOTS:
           slts.append(slt)
        return slts



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
        print('L\'item', word, 'est créé.')

    def makeItem(self):
        item = self.WORD
        return item # Return str


    @property
    # ⚠ S'applique sur l'item directement, PAS sur le retour str de la ❌ méthode Item().makeItem() ❌
    def isCore(self):
        for el in range(0,len(Grid.LISTE_CORE)):
            #print(Grid.LISTE_CORE[el][0])
            if self.WORD == Grid.LISTE_CORE[el][0]:
                #print(self.WORD, 'work')
                return True
            else:
                pass
