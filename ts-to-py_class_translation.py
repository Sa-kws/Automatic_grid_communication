class Grid:
    ELEMENT_LIST = []
    IMAGE_LIST = []
    PAGE_LIST = []
    
    def __init__(self, ID, NumberOfCols, NumberOfRows, Gapsize):
        Grid.self = self
        ID.self = ID
        NumberOfCols.self = NumberOfCols
        NumberOfRows.self = NumberOfRows
        Gapsize.self = Gapsize
    
    def makeGrig(gridId, gridType, gridCol, gridRow, elemList, imageList, pageList):
        pass



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
