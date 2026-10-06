import random

class RPG:
    def __init__(self, jmeno:str, vek:int, misto:str = "vesnice", hp:int=100, mp:int=25):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        self.hp = hp
        self.mp = mp
        pass


    def predstav_se(self):
        return (f"Jsem {self.jmeno} aktuálně mám HP - {self.hp} a MP - {self.mp} ")
    

class Knight(RPG):
    def __init__(self, jmeno: str, vek: int, skilltree:str, brnění:str, mec:str,  misto: str = "vesnice", hp:int=100, mp:int=25):
        super().__init__(jmeno, vek, misto)
        self.skilltree = skilltree
        self.brnění = brnění
        self.mec = mec

    def zautoc_knight(self):
        return (f"hajá hačá 'zautočil jsi a ubral jsi': {round(random.uniform(10, 20), 2)}")
    
    def zablokuj(self):
        if(random.randint(0,1) > 0):
            return (f"odrazil jsi utok")
        else:
            demage = round(random.uniform(10, 99), 2)
            self.hp -= demage
            self.hp = round(self.hp, 2)

            if self.hp < 0:
                return("zemřel jsi")
            else:   
                return(f"dostal jsi zásah")
            
    def predstav_se2(self):
        return (f"Jsem {self.jmeno} aktuálně mám HP - {self.hp} a MP - {self.mp} jsem oblecen v: {self.brnění} a mám v ruce {self.mec} ")

john = Knight("Greis", 28, "Knight", "Mythrilove brnění", "Orichalkový legendární měč", "Palác")
print(john.predstav_se2())
print(john.zautoc_knight())
print(john.zablokuj())
print(john.predstav_se2())
