import copy
class Slot():

    def __init__(self, word, isCore, pageDestination):
        # word = str que l'on souhaite traiter et placer sur la grille
        # is Core = Booléen un indiquant si le mot traité fait parti du vocabulaire core ou non
        self.__word = copy.copy(word)
        self.__isCore = copy.copy(isCore)
        self.__pageDestination = copy.copy(pageDestination)

    # Accesseur
    def get_word(self):
        return self.__word

    # Accesseur
    def get_is_core(self):
        return self.__isCore

    def get_page_destination(self):
        return self.__pageDestination

    def __str__(self):
        return str(self.__word) + ';' + str(self.__isCore) + ';' + str(self.__pageDestination)
