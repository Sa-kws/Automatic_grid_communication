from word2grid import Grid
from word2grid import Page
from word2grid import Slot



def main(datas):
    grid = Grid.Grid()
    page = Page.Page()
    used_words = []
    for ligne in datas:
        ligne[0] = word
        ligne[1] = isCore
        ligne[2] = pageDestination
        s = Slot.Slot(word, isCore, pageDestination)
        grid, page = grid.makeGrid(page, used_words, s)
    return grid
