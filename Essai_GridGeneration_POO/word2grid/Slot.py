import copy
class Slot():

    def __init__(self, word, isCore):
        # word = str que l'on souhaite traiter et placer sur la grille
        # is Core = Booléen un indiquant si le mot traité fait parti du vocabulaire core ou non
        self.__word = copy.copy(word)
        self.__isCore = copy.copy(isCore)

    # Accesseur
    def get_word(self):
        return self.__word

    # Accesseur
    def get_is_core(self):
        return self.__isCore

    def __str__(self):
        return '('+ str(self.__word) + ',' + str(self.__isCore) + ')'
