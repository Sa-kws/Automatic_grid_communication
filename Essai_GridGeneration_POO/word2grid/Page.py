from word2grid import Grid

class Page():
    # __SLOTS = []
    __ROW_SIZE = 0
    __COL_SIZE = 0
    __WARNING_MESSAGE = 'PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.'
    def __init__(self, row, col):
        self.tableau = []
        self.__ROW_SIZE = row
        self.__COL_SIZE = col
        self.__slots = []

    # Chaque page peut avoir son propre nombre mais Grid le régule
    def createPage(self):
        # Initialisation d'une grille à la taille des valeurs indiquées dans les attributs ROW_SIZE et COL_SIZE
        # Sortie : Tableau vide en ROW_SIZE*COL_SIZE
        for i in range(0, self.__ROW_SIZE):
            entre = []
            for j in range(0, self.__COL_SIZE):
                entre.append([None])
            self.tableau.append(entre)

        # Parcours du vocabulaire core stocké dans l'attribut LISTE_CORE de la classe Grid()
        # La LISTE_CORE doit être au format : [[word, row, column], [word, row, column]...]
        # Gestion des erreurs d'indexation
        # Sortie : Tableau contenant le vocabulaire core bien placé
        for core_vocab in Grid.Grid.LISTE_CORE:
            row = core_vocab[1]
            col = core_vocab[2]
            try:
                self.tableau[row][col] = core_vocab
            except IndexError:
                self.tableau.append(self.__WARNING_MESSAGE)
                return self
        return self

    # Lorqu'on créé un objet de la classe Page(), une page (liste) au format souhaité est générée.
    # Le format de la page peut-être changé dans les attributs ROW_SIZE et COL_SIZE par le programmeur
    # Sortie : Tableau contenant le vocabulaire core bien placé / Type : list


    def isOccupied(self, row, col):
        return self.tableau[row][col][0] != None
    # Sortie : Constat de l'état de la position (occupée ou non) / Type : booléen


    def isFull(self):
        # Parcours de la page : si une position n'est pas occupée (c-à-d == None), la méthode s'arrête et retourne False,
        # sinon, elle parcours la totalité de page puis retourne True
        for row in range(0,len(self.tableau)):
            for col in range (0, len(self.tableau[row])):
                if self.tableau[row][col][0] == None:
                    return False
        return True
    # Sortie : Constat de l'état de la page (remplie ou non) / Type : booléen


    def isWellSized(self):
        return self.__WARNING_MESSAGE not in self.tableau
    # Sortie : Vérification des mesures de la page / Type : booléen


    def addSlots(self, slot):
        self.__slots.append(slot)
        return self


    def addSlotToPage(self, slot, row, col):
        # page = tableau créé via Page()
        #if self.isOccupied(row, col) == False:
        self.tableau[row][col] = [slot, row, col]
        return self
        #else:
        #    return 'NON PLACé, SLOT OCCUPé'
    # Sortie : Une page contenant le slot ajouté / Type : list
