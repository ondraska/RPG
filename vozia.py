class Vozidlo:
    def __init__(self, znacka :str, rok_vyroby:int , stav_nadrze:int = 100 ):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze
        pass
 
 
    def zvuk_motoru(self):
        return "brrbbrbrbr"
 
    def info(self):
        return f"znacka vozidla {self.znacka} a rok {self.rok_vyroby}"
 
    def startuje(self):
        if (self.stav_nadrze > 0):
            return f"{self.zvuk_motoru()} vzidlo startuje"
        else:
            return "dosla stava"
 
class Auto(Vozidlo):
    def __init__(self, znacka :str, rok_vyroby:int , typ_prevodovky:str, stav_nadrze:int = 100 ):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.typ_prevodovky = typ_prevodovky
        self.stav_nadrze = stav_nadrze
        pass
 
    def zvuk_motoru(self):
        return " vrum vrum vrum"
 
    def info(self):
        return f"znacka vozidla {self.znacka} a rok {self.rok_vyroby} a typ prevodovky {self.typ_prevodovky}"
 
    def zatrub(self):
        return"tututututu"
    def startuje(self):
        if (self.stav_nadrze > 0):
            return f"{self.zvuk_motoru()} auto startuje"
        else:
            return "dosla stava"
 
class Moped(Vozidlo):
    def __init__(self, znacka :str, rok_vyroby:int , ma_slapadla: bool, stav_nadrze:int = 100 ):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.ma_slapadla = ma_slapadla
        self.stav_nadrze = stav_nadrze
        pass
 
 
    def zvuk_motoru(self):
        return "trrrrrrr"
 
    def slapej(self):
        return f"budes slapat : {self.ma_slapadla}"
 
    def info(self):
        return f"znacka vozidla {self.znacka} a rok {self.rok_vyroby}"
 
    def startuje(self):
        if (self.stav_nadrze > 0):
            return f"{self.zvuk_motoru()} vzidlo startuje"
        else:
            return "dosla stava"
 
 
        
 
 
 
vozidlo = Vozidlo("skoda", 2012, 30)
print(vozidlo.zvuk_motoru())
print(vozidlo.info())
print(vozidlo.startuje())
 
 
auto = Auto("audi", 2015, "manual",  0)
print(auto.zvuk_motoru())
print(auto.info())
print(auto.startuje())
print(auto.zatrub())
 
 
moped = Moped("aprilia", 2025, False, 60)
print(moped.zvuk_motoru())
print(moped.info())
print(moped.startuje())
print(moped.slapej())
 
 
garaz = [auto, moped]
 
for vozidlo in garaz:
    print(auto.info())
    print(auto.startuje())
    print(moped.info())
    print(moped.startuje())