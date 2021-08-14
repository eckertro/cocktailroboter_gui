class Cocktail():
    def __init__(self, name, beschreibung, mengen):
        self.name = name
        self.beschreibung = beschreibung
        self.mengen = mengen
    
    def getName(self):
        return self.name
    
    def getBeschreibung(self):
        return self.beschreibung
    
    def getMengen(self):
        return self.mengen
    
