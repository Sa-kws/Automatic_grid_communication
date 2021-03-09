class Page():
    ROW_SIZE = 3
    COL_SIZE = 4
    WARNING_MESSAGE = 'PAGE NON GENEREE :\nErreur d\'index - La position du vocabulaire core n\'existe pas dans la grille.\nChangez la taille de la grille, ou la position du vocabulaire core.'

    def __init__(self):
        self.Page = Page

    def __new__(cls, ID, name):
        tableau = []
        cls.ID = ID

        # Initialisation d'une grille à la taille des valeurs indiquées dans les attributs ROW_SIZE et COL_SIZE
        # Sortie : Tableau vide en ROW_SIZE*COL_SIZE
        for i in range(0, cls.ROW_SIZE):
            entre = []
            for j in range(0, cls.COL_SIZE):
                entre.append([None])
            tableau.append(entre)

        # Parcours du vocabulaire core stocké dans l'attribut LISTE_CORE de la classe Grid()
        # La LISTE_CORE doit être au format : [[word, row, column], [word, row, column]...]
        # Gestion des erreurs d'indexation
        # Sortie : Tableau contenant le vocabulaire core bien placé
        for core_vocab in Grid.LISTE_CORE:
            row = core_vocab[1]
            col = core_vocab[2]
            try:
                tableau[row][col] = core_vocab
            except IndexError:
                return cls.WARNING_MESSAGE
        return tableau

    # Lorqu'on créé un objet de la classe Page(), une page au format souhaité est générée.
    # Le format de la page peut-être changé dans les attributs ROW_SIZE et COL_SIZE
    # Sortie : Tableau contenant le vocabulaire core bien placé / Type : list


    def isOccupied(self, row, col, page):
        return page[row][col][0] != None
    # Sortie : Constat de l'état de la position (occupée ou non) / Type : booléen


    def isFull(self, page):
        # Parcours de la page : si une position n'est pas occupée (c-à-d == None), la méthode s'arrête et retourne False,
        # sinon, elle parcours la totalité de page puis retourne True
        for row in range(0,len(page)):
            for col in range (0, len(page[row])):
                if page[row][col][0] == None:
                    return False
        return True
    # Sortie : Constat de l'état de la page (remplie ou non) / Type : booléen


    def isWellSized(self, page):
        return Page.WARNING_MESSAGE not in page
    # Sortie : Vérification des mesures de la page / Type : booléen

    def addSlot(self, page, row, col, word):
        # page = tableau créé via Page()
        page[row][col] = [word, row, col]
        return page
    # Sortie : Une page contenant le slot ajouté / Type : list
