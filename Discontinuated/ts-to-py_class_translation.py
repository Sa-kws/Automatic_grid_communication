import pandas as pd
import numpy as np
class Grid:
    ELEMENT_LIST = []
    #IMAGE_LIST = []
    PAGE_LIST = []
    GRID_ROW = 4
    GRID_COL = 8
    DATA = ['Salut', 'je', 'suis', 'Sarah']
    
    def __init__(self, NumberOfCols, NumberOfRows, Gapsize):
        #self.ID = ID # à quoi cela correspond ?
        self.NumberOfCols =  NumberOfCols # à définir
        self.NumberOfRows = NumberOfRows # à définir
        self.GapSize= 1
    
    def makeGrig(self, data):
        return np.zeros(shape=(len(data), 8))

        # Ajouter la liste des items
        # Ajouter la liste des pages


class FolderGoTo:
    def __init__(self, GoTo):
        FolderGoTo.self = self
        FolderGoTo.GoTo = GoTo
        
    def goFolder(goto):
        pass


class GridElement:
    
    ELEMENT_FORMS_LIST = []
    INTERACTIONS_LIST = []
    
    def __init__(self, ID, Type, POS, VisibilityLevel, x, y, columns, rows):
        GridElement.self = self
        GridElement.ID = ID
        GridElement.Type = Type
        GridElement.POS = POS
        GridElement.VisibilityLevel = VisibilityLevel
        GridElement.x = 0
        GridElement.y = 0
        GridElement.columns = 1
        GridElement.rows = 1


class Intercation: 
    def __init__(self, ID, ActionList):
        Intercation.self = self
        Intercation.ID = ID
        Intercation.ActionList = []


class Action:
    def __init__(self, ID, Options):
        Action.self = self
        Action.ID = ID
        Action.Options = []


class Page:
    def __init__(self, ID, Name, ElementIDsList, NumberOfCols, NumberOfRows, GapSize):
        Page.self = self
        Page.ID = ID
        Page.Name = Name
        Page.ElementIDsList = []
        Page.NumberOfCols = NumberOfCols
        Page.NumberOfRows = NumberOfRows
        Page.GapSize = GapSize

    def makePage(self, ):
        pass

grille = Grid(8,4,1)
grille = grille.makeGrig(data=['Salut', 'je', 'suis', 'Sarah'])
print(grille)
print(dir(np))
'''
1/ Créer une grille
2/ Créer des pages
3/ Ajouter les pages à la grille
4/ Créer des items
5/ Ajouter des items aux pages
6/ Créer des dossiers
7/ Ajouter des dossiers aux pages
8/ Lier les dossiers aux pages
'''