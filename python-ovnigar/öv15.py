"""
1. Implementera en klass Djur med attributet namn. 
Skapa två subklasser till Djur: Fagel och Fisk.
Fagel ska ha ett attribut vingspann. 
Fisk ska ha ett attribut maxdjup. 
Skapa två subklasser till Fisk: Haj och Torsk. 
Haj ska ha ett attribut antalTänder. 
Torsk ska ha ett attribut hastighet.  

2. Skriv en funktion fånga(haj, torsk) som returnerar True ifall 
(a) torskens hastighet är mindre än 30 och (b) hajens maxdjup är 
minst lika stort som torskens, annars False.
"""

class Djur:
    def __init__(self, namn):
        self.namn = namn
    def at(self):
        print("Djur äta.")
    def sov(self):
        print("Djur sova.")

class Fagel(Djur):
    def __init__(self, namn, vingspann):
        super().__init__(namn)
        self.vingspan = vingspann

class Fisk(Djur):
    def __init__(self, namn, maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup
    def simma(self):
        print("Fisk simma.")

class Haj(Fisk):
    def __init__(self, namn, maxdjup, antalTander):
        super().__init__(namn,maxdjup)
        self.antalTander = antalTander
    def at(self, djur):
        print(f"Haj äta {djur}.")

class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet):
        super().__init__(namn,maxdjup)
        self.hastighet = hastighet


def fanga(haj, torsk):
        if torsk.hastighet < 30 and torsk.maxdjup <= haj.maxdjup:
            return True
        else:
            return False


