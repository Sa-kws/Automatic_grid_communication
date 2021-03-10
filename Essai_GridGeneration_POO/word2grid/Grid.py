class Grid():
    # La grille doit toujours être créée via son attribut : grid = Grid().PAGES
    PAGES = []
    CORE_VOCABULARY = ['je', 'vouloir', 'quoi', 'pourquoi'] # Devrait être modifé
    LISTE_CORE = [['je', 0, 1], ['vouloir', 0, 0], ['quoi', 1, 1], ['pourquoi', 1, 0]] # Devrait être modifié

    def __init__(self):
        self.Grid = Grid

    def setCoreVoc(*self):
    # Cette méthode va servir à modifier le vocabulaire core si celui-ci ne convient pas à l'utilisateur.
        print(Grid.LISTE_CORE, '\n')

        if input("La liste de Vocabulaire Core convient-elle ? ['y' or 'n']") != 'y':
            import re
            regex = r'[0-9]*'
            # On présente la liste à l'utilisateur et on lui demande si celle-ci lui convient,
            # si ce n'est pas le cas, on lui demande d'entrer sa propre liste selon un format spécifique
            new_voc = input('Entrez votre liste de vocabulaire au format suivant :\n\n\tmot;position de ligne;position de colonne_mot;position de ligne;position de colonne_ ...\n')
            newvoc = new_voc.split('_')
            for liste in range(0, len(newvoc)):
                newvoc[liste] = newvoc[liste].split(';')
            # Ensuite, on met en forme l'entrée pour que celle-ci soit conforme à notre programme
            for core in range(0, len(newvoc)):
                for element in range(0, len(newvoc[core])):
                    if re.fullmatch(regex, newvoc[core][element]):
                        newvoc[core][element] = int(newvoc[core][element])

            Grid.LISTE_CORE = newvoc
        return Grid.LISTE_CORE
        # Sortie : La liste du vocabulaire Core modifiée ou non, selon le choix de l'utilisateur / Type : list


    def addPage(self, core, word, used_words, page, grid):
        # Si le word est un voc core, on s'arrête là, puisqu'il sera déjà placé sur la page
        if core == False and word not in used_words:
            # Parcours de la page, et recherche des position vide via la méthode Page().isOccupied() (True ou False) dans la page créée
            for row_browse in range(0, len(page)):
                for col_browse in range(0, len(page[row_browse])):
                    if Page.isOccupied(Page, row_browse, col_browse, page) == False and word not in used_words:
                        page = Page.addSlot(Page, page, row_browse, col_browse, word)
                        used_words.append(word)
        return grid
    # Sortie : Grille précédente plus la page ajoutée / Type : list


    def finishGrid(*self, page, grid):
    # Cette méthode sert à ajouter une page qui n'est pas remplie entièrement à la grille, et est à utiliser en dernier
        if page not in grid:
            grid.append(page)
        return grid
    # Sortie : Grille complète / Type : list


    def addFulledPage(*self, ID, grid, page, used_words, word):
    # Cette méthode sert à ajouter une page entièrement remplie à la grille
        # On ajoute la page, puis on réinitialise la variable page (on la vide) et on la parcours une seule fois pour ajouter le mot sur lequelle la boucle tourne
        grid.append(page)
        page = Page(ID, 'test-')
        for row in range(0, len(page)):
            for col in range(0, len(page[row])):
                if Page.isOccupied(Page, row, col, page) == False and word not in used_words:
                    page = Page.addSlot(Page, page, row, col, word)
                    used_words.append(word)
                    break # sert à faire un seul tour de boucle
            break # sert à faire un seul tour de boucle
        return grid
    # Sortie Grille précédente plus la page complète ajoutée / Type : list

    def addFolderPage(*self, path, folder_datas, grid, ID):
        used_words = []
        # On commence par vérifier si le mot ouvre un dossier, si c'est le cas, on créé la 'page cible',
        # et on la remplie avec les mots de cette page, stockés dans un fichier txt (qu'on passera dans folder_datas).
        # Pour la remplir, on reprend la méthode Grid().makeGrid() à laquelle on passe les bonnes données en argument
        if path != None:
            ID += 1
            name = 'Page_' + str(ID)
            folder_page = Page(ID, name)
            for word in folder_datas:
                grid, page = Grid.makeGrid(page=folder_page, used_words=used_words, grid=grid, ID=ID, word=word, iscore=False)
            # On réutilise la méthode Grid().finishGrid() dans le cas où la nouvelle page contient moins de mots que de positions disponibles
            grid = Grid.finishGrid(page=folder_page, grid=grid)
        return grid
    # Sortie : Grille précédente plus la 'page cible' ajoutée / Type : list


    def makeGrid(*self, page, used_words, grid, ID, iscore, word):
        # Méthode servant à remplir la page, puis à l'ajouter à la grille.
            # Vérification qu'il reste de la place sur la page, puis ajout des mots
            if Page.isFull(Page, page) == False:
                grid = Grid.addPage(Grid, iscore, word, used_words, page, grid)
            # Quand la page est pleine, on utilise la méthode Grid().addFulledPage()
            else:
                grid = Grid.addFulledPage(ID=ID, grid= grid, page=page, used_words=used_words, word=word)
                ID += 1
                name = 'Page_' + str(ID)
                page = Page(ID, name)
            return grid, page
    # Sortie :
    #           - Grid : Grille précédente + la/les page(s) ajoutée(s) / Type : list
    #           - Page : Nouvelle page qui sera réutilisée dans la suite de la boucle / Type : list
