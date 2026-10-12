import random

class RPG:
    def __init__(self, jmeno: str, vek: int, misto: str = "vesnice", hp: int = 100, mp: int = 25):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        self.hp = hp
        self.mp = mp

    def predstav_se(self):
        return f"Jsem {self.jmeno} aktuálně mám HP - {self.hp} a MP - {self.mp}"


class Knight(RPG):
    def __init__(self, jmeno: str, vek: int, skilltree: str, brnění: str, mec: str,
                 misto: str = "vesnice", hp: int = 100, mp: int = 25):
        super().__init__(jmeno, vek, misto, hp, mp)
        self.skilltree = skilltree
        self.brnění = brnění
        self.mec = mec

        if "Mythril" in brnění or "mythril" in brnění:
            self.obrana = 25
        elif "Orichalk" in brnění or "orichalk" in brnění:
            self.obrana = 40
        else:
            self.obrana = 10

    def zautoc_knight(self):
        if random.random() < 0.2:  
            mana_cost = round(random.uniform(5, 15), 2)
            
            if self.mp >= mana_cost:
                self.mp -= mana_cost
                self.mp = round(self.mp, 2)
                return f"Magický útok! Ubral jsi {mana_cost} many (zbývá MP: {self.mp})"
            else:
                return "Nemáš dost many na magický útok!"
        else:
            return f"hajá hačá 'zautočil jsi a ubral jsi': {round(random.uniform(10, 20), 2)}"
    
    def zablokuj(self):
        if random.randint(0, 1) > 0:
            return "odrazil jsi útok"
        else:
            demage = round(random.uniform(10, 99), 2)
            
            demage = max(0, demage - self.obrana)
            demage = round(demage, 2)
            
            self.hp -= demage
            self.hp = round(self.hp, 2)

            if self.hp <= 0:
                self.hp = 0
                return "zemřel jsi"
            else:
                return f"dostal jsi zásah za {demage} (brnění ubralo {self.obrana})"
            
    def predstav_se2(self):
        return (f"Jsem {self.jmeno} aktuálně mám HP - {self.hp} a MP - {self.mp} "
                f"jsem oblečen v: {self.brnění} a mám v ruce {self.mec}")


class Mag(RPG):
    def __init__(self, jmeno: str, vek: int, misto: str = "vesnice", hp: int = 100, mp: int = 50):
        super().__init__(jmeno, vek, misto, hp, mp)
        self.obleceni = "Hvězdný plášť archmága"
        self.ochrana_ohen = 30
        self.ochrana_temno = 25

    def utok(self):
        if self.mp < 5:
            if random.random() < 0.10:
                return "Nemáš na slabý útok! Upadás do bezvědomí, ale zásah se ti podařilo vyblokovat."
            else:
                self.hp = round(random.uniform(10, 100), 2)
                return (f"Nemáš na slabý útok! Upadás do bezvědomí a dostal jsi hit! "
                        f"Zbývá ti {self.hp} HP a {self.mp} many")

        utoky = [
            ("světelný", 20, 35, 8, 18, [
                "oslepil nepřítele jasnou září",
                "spálil nepřítele posvátným světlem",
                "vypálil nepříteli oči svatou energií"
            ]),
            ("ohnivý", 22, 38, 9, 18, [
                "zapálil nepřítele a nechal ho hořet",
                "spálil nepříteli část zbroje",
                "proměnil okolí v ohnivé peklo"
            ]),
            ("vodní", 18, 32, 8, 17, [
                "smetl nepřítele proudem vody",
                "udusil nepřítele vodní bublinou",
                "zmrazil nepříteli končetiny"
            ]),
            ("zemní", 25, 40, 10, 17, [
                "zavalil nepřítele kamením",
                "srazil nepřítele silnou otřesnou vlnou",
                "uvěznil nepřítele v zemi"
            ]),
            ("temný", 20, 36, 9, 15, [
                "vysál nepříteli životní sílu",
                "zahalil nepřítele temnotou a strachem",
                "proklel nepřítele stínovou magií"
            ]),
            ("časový", 35, 55, 14, 6, [
                "způsobil vážné zestárnutí a dočasně snížil maximální HP",
                "vytrhl nepřítele z časové linie a zanechal ho zmateného",
                "zrychlil čas kolem nepřítele a nechal ho zestárnout o desítky let",
                "potrhal mu oblečení a způsobil bolestivé zestárnutí"
            ]),
            ("jedový (poison)", 30, 50, 12, 5, [
                "otrávil nepřítele silným jedem (každé kolo ztrácí HP)",
                "vstříkl jed přímo do krve a způsobil silnou otravu",
                "potrhal mu oblečení a zanechal jedovaté rány",
                "způsobil masivní otravu, která se šíří tělem"
            ]),
            ("antimagický", 40, 60, 15, 4, [
                "dočasně zablokoval manu a výrazně snížil MP nepřítele",
                "rozbil nepříteli magické vazby a zneškodnil jeho kouzla",
                "potrhal mu oblečení a vypálil magické kanály",
                "vytvořil antimagickou zónu, ve které nepřítel nemůže kouzlit"
            ]),
        ]

        vybrany = random.choices(utoky, weights=[u[4] for u in utoky], k=1)[0]
        nazev, min_d, max_d, cost, _, efekty = vybrany

        if self.mp < cost:
            self.mp = max(0, round(self.mp - 3, 2))
            return f"Nemáš dost many na {nazev} útok! Útočíš slabým útokem za 5 (zbývá MP: {self.mp})"

        self.mp -= cost
        self.mp = round(self.mp, 2)
        poskozeni = round(random.uniform(min_d, max_d), 2)
        efekt = random.choice(efekty)

        return (f"Nepřítel dostal {nazev} útok! Ubral jsi {poskozeni} HP a {efekt}. "
                f"(Stálo tě {cost} MP, zbývá MP: {self.mp})")

    def dostan_utok(self):
        """Nepřítel útočí na maga"""
        utoky_na_maga = [
            ("světelný", 15, 30, 18, "oslepil tě jasnou září"),
            ("ohnivý", 18, 35, 18, "zapálil tě"),
            ("vodní", 14, 28, 17, "smetl tě proudem vody"),
            ("zemní", 20, 38, 17, "zavalil tě kamením"),
            ("temný", 16, 32, 15, "vysál ti životní sílu"),
            ("časový", 30, 50, 6, "způsobil ti zestárnutí"),
            ("jedový", 25, 45, 5, "otrávil tě"),
            ("antimagický", 35, 55, 4, "zablokoval ti manu"),
        ]

        vybrany = random.choices(utoky_na_maga, weights=[u[3] for u in utoky_na_maga], k=1)[0]
        nazev, min_d, max_d, _, efekt = vybrany
        poskozeni = round(random.uniform(min_d, max_d), 2)

        # Ochrana
        if nazev == "ohnivý":
            poskozeni = max(0, poskozeni - self.ochrana_ohen)
            efekt += f" (ochrana proti ohni -{self.ochrana_ohen})"
        elif nazev == "temný":
            poskozeni = max(0, poskozeni - self.ochrana_temno)
            efekt += f" (ochrana proti temnotě -{self.ochrana_temno})"

        poskozeni = round(poskozeni, 2)
        self.hp -= poskozeni
        self.hp = round(max(0, self.hp), 2)

        return (f"Dostal jsi {nazev} útok! Ubral ti {poskozeni} HP a {efekt}. "
                f"Zbývá ti {self.hp} HP a {self.mp} many")
    
class Zlodej(RPG):
    def __init__(self, jmeno, vek, misto = "vesnice", hp = 100, mp = 25):
        super().__init__(jmeno, vek, misto, hp, mp)


print("=== KNIGHT ===")
john = Knight("Greis", 28, "Knight", "Mythrilove brnění", "Orichalkový legendární meč", "Palác")
print(john.predstav_se2())
print(john.zautoc_knight())
print(john.zablokuj())
print(john.predstav_se2())

# ====================== BOJOVÁ SMYČKA ======================
print("=== BOJ: GANDALF vs NEPŘÍTEL ===\n")

gandalf = Mag("Gandalf", 201, "Hrad")  
kolo = 1

while gandalf.hp > 0 and gandalf.mp >= 0:
    print(f"---------- KOLO {kolo} ----------")
    print(gandalf.predstav_se())
    
    print("→ Gandalf útočí:")
    print(gandalf.utok())
    
    if gandalf.hp <= 0:
        print("\n💀 Gandalf upadl do bezvědomí nebo zemřel!")
        break

    print("\n→ Nepřítel útočí:")
    print(gandalf.dostan_utok())
    
    if gandalf.hp <= 0:
        print("\n💀 Gandalf byl poražen!")
        break
    
    print()
    kolo += 1
    
    if kolo > 15:
        print("Boj trval příliš dlouho – remíza!")
        break

print("\n=== KONEC BOJE ===")
print(gandalf.predstav_se())
