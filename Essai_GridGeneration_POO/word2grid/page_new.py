from word2grid import Grid

class Page():
    #SLOTS = []
    ROW_SIZE = 3
    COL_SIZE = 4
    WARNING_MESSAGE = 'PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.'
    
    def __init__(self):
        self.Page = Page


    def createPage(self):
      
        self.tableau = []
        
        # Initialisation d'une grille à la taille des valeurs indiquées dans les attributs ROW_SIZE et COL_SIZE
        # Sortie : Tableau vide en ROW_SIZE*COL_SIZE
        for i in range(0, self.ROW_SIZE):
            entre = []
            for j in range(0, self.COL_SIZE):
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
                return self.WARNING_MESSAGE
        return self
    
    
    
    def addSlot(self, slot, row, col):
        self.tableau[row][col] = [slot, row, col]
        return self

    
    
    def isOccupied(self, row, col):
        return self.tableau[row][col][0] != None
    
    
    
