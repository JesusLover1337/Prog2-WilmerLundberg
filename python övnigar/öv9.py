class Elev:
    def __init__(self,namn,ålder,godkänd):
        self.namn:str = namn
        self.ålder:int = ålder
        self.godkänd:bool = godkänd
        self.glad:bool = True if godkänd else False
    def presentera(self):
        print(f"Hej! Jag heter {self.namn}.") 



