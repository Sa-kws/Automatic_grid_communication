from word2grid import Page

class Grid():
    # La grille doit toujours être créée via son attribut : grid = Grid().PAGES
    PAGES = []
    CORE_VOCABULARY = ['je', 'vouloir', 'quoi', 'pourquoi'] # Devrait être modifé
    LISTE_CORE = [['je', 0, 1], ['vouloir', 0, 0], ['quoi', 1, 1], ['pourquoi', 1, 0]] # Devrait être modifié

    def __init__(self):
        self.classeur = []

    def setCoreVoc(self):
    # Cette méthode va servir à modifier le vocabulaire core si celui-ci ne convient pas à l'utilisateur.
        print(self.LISTE_CORE, '\n')

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

            self.LISTE_CORE = newvoc
        return self.LISTE_CORE
        # Sortie : La liste du vocabulaire Core modifiée ou non, selon le choix de l'utilisateur / Type : list


    def addPage(self, core, word, used_words, grid):
        # Si le word est un voc core, on s'arrête là, puisqu'il sera déjà placé sur la page
        page = Page.Page(3,4)
        page = page.createPage()
        if core == False and word not in used_words:
            # Parcours de la page, et recherche des position vide via la méthode Page().isOccupied() (True ou False) dans la page créée
            for row_browse in range(0, len(page.tableau)):
                for col_browse in range(0, len(page.tableau[row_browse])):
                    if page.isOccupied(row_browse, col_browse) == False and word not in used_words:
                        page = page.addSlotToPage(word, row_browse, col_browse)
                        used_words.append(word)
                        print('addPage-used_words-\t', used_words)
        return self
    # Sortie : Grille précédente plus la page ajoutée / Type : list


    def finishGrid(self, page):
    # Cette méthode sert à ajouter une page qui n'est pas remplie entièrement à la grille, et est à utiliser en dernier
        if page.tableau not in self.classeur:
            self.classeur.append(page.tableau)
        print('\nTYPE FINISH GRID\n', type(self))
        return self
    # Sortie : Grille complète / Type : list


    def addFulledPage(self, page, used_words, slot):
        #row = Page._Page__COL_SIZE
        #col = Page._Page__COL_SIZE
    # Cette méthode sert à ajouter une page entièrement remplie à la grille
        # On ajoute la page, puis on réinitialise la variable page (on la vide) et on la parcours une seule fois pour ajouter le mot sur lequelle la boucle tourne
        self.classeur.append(page.tableau)

        p = Page.Page(3, 4)
        p = p.createPage()
        for row in range(0, len(page.tableau)):
            for col in range(0, len(page.tableau[row])):
                if p.isOccupied(row, col) == False and slot.get_word() not in used_words:
                    p = p.addSlotToPage(slot.get_word(), row, col)
                    used_words.append(slot.get_word())
                    break # sert à faire un seul tour de boucle
            break # sert à faire un seul tour de boucle
        return self
    # Sortie Grille précédente plus la page complète ajoutée / Type : list

    def addFolderPage(*self, path, folder_datas, grid, ID):
        used_words = []
        # On commence par vérifier si le mot ouvre un dossier, si c'est le cas, on créé la 'page cible',
        # et on la remplie avec les mots de cette page, stockés dans un fichier txt (qu'on passera dans folder_datas).
        # Pour la remplir, on reprend la méthode Grid().makeGrid() à laquelle on passe les bonnes données en argument
        if path != None:
            ID += 1
            name = 'Page_' + str(ID)
            folder_page = Page.Page(3,4)
            folder_page = folder_page.createPage()
            for word in folder_datas:
                grid = grid.makeGrid(page=folder_page, grid=grid, used_words=used_words, ID=ID, word=word, iscore=False)
            # On réutilise la méthode Grid().finishGrid() dans le cas où la nouvelle page contient moins de mots que de positions disponibles
            self = grid.finishGrid(page=folder_page)
        return self
    # Sortie : Grille précédente plus la 'page cible' ajoutée / Type : list


    def makeGrid(self, page, used_words, grid, ID, iscore, word):
        # Méthode servant à remplir la page, puis à l'ajouter à la grille.
            # Vérification qu'il reste de la place sur la page, puis ajout des mots
            if page.isFull() == False:
                print('PAGE NOT FULL ------------------')
                page = self.addPage(core=iscore, word=word, used_words=used_words, grid=grid)
            # Quand la page est pleine, on utilise la méthode Grid().addFulledPage()
            else:
                print('\n---------------------PAGE IS FULL\n')
                self = self.addFulledPage(ID=ID, grid= grid, page=page, used_words=used_words, word=word)
                ID += 1
                name = 'Page_' + str(ID)
                page = Page.Page(3,4)
                page = page.createPage()
            return self
    # Sortie :
    #           - Grid : Grille précédente + la/les page(s) ajoutée(s) / Type : list
    #           - Page : Nouvelle page qui sera réutilisée dans la suite de la boucle / Type : list
