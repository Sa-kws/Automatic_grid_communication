class Slot():

    def __init__(self):
        self.Slot = Slot

    def addItem(self, is_core):
        slot = []
        slot.append(self)
        slot.append(is_core)
        return slot
