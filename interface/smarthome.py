from abc import ABC, abstractmethod

# Hlavní abstraktní třída (šablona pro ostatní)
class SmartHome(ABC):
    
    # Abstraktní metoda - musí ji mít každé zařízení
    @abstractmethod
    def setProperties(self, **kwargs):
        pass

    # Abstraktní metoda pro získání vlastností
    @abstractmethod
    def getProperties(self, **kwargs):
        pass


# Třída pro světla - dědí ze SmartHome
class Lights(SmartHome):
    def __init__(self, name, room, type_of_light, luminosity, color):
        self.name = name
        self.room = room
        self.type_of_light = type_of_light
        self.luminosity = luminosity
        self.color = color

    # Nastavení vlastností
    def setProperties(self, **kwargs):
        # Projdeme všechny argumenty, které jsme dostali
        for klic, hodnota in kwargs.items():
            # BONUS: Kontrola, jestli taková vlastnost vůbec existuje
            if hasattr(self, klic):
                setattr(self, klic, hodnota) # Dynamické nastavení atributu
            else:
                print(f"Chyba: Vlastnost '{klic}' u světla neexistuje!")

    # Získání vlastností
    def getProperties(self, **kwargs):
        # Vytvořím si slovník se všemi aktuálními daty
        data = {
            "name": self.name,
            "room": self.room,
            "type_of_light": self.type_of_light,
            "luminosity": self.luminosity,
            "color": self.color
        }

        # Pokud nebyly zadány žádné filtry, vrátím všechno
        if not kwargs:
            return data
        
        # Jinak vrátím jen to, o co si uživatel řekl v kwargs
        vybrane = {}
        for k in kwargs:
            if k in data:
                vybrane[k] = data[k]
        return vybrane

    # BONUS: Hezký výpis při print()
    def __str__(self):
        return f"Světlo: {self.name} ({self.room}) - Jas: {self.luminosity}%, Barva: {self.color}"


# Třída pro routery - dědí ze SmartHome
class Routers(SmartHome):
    def __init__(self, name, room, IP, supported_frequencies, mesh):
        self.name = name
        self.room = room
        self.IP = IP
        self.supported_frequencies = supported_frequencies
        self.mesh = mesh

    def setProperties(self, **kwargs):
        for klic, hodnota in kwargs.items():
            if hasattr(self, klic):
                setattr(self, klic, hodnota)
            else:
                print(f"Chyba: Vlastnost '{klic}' u routeru neexistuje!")

    def getProperties(self, **kwargs):
        data = {
            "name": self.name,
            "room": self.room,
            "IP": self.IP,
            "supported_frequencies": self.supported_frequencies,
            "mesh": self.mesh
        }

        if not kwargs:
            return data
        
        # Filtrování (stejné jako u světel)
        vybrane = {}
        for k in kwargs:
            if k in data:
                vybrane[k] = data[k]
        return vybrane

    def __str__(self):
        mesh_text = "Ano" if self.mesh else "Ne"
        return f"Router: {self.name} [{self.IP}] - Mesh: {mesh_text}"


# --- TESTOVÁNÍ KÓDU ---
if __name__ == "__main__":
    print("--- Test 1: Pokus o vytvoření abstraktní třídy ---")
    try:
        test = SmartHome()
    except Exception as e:
        print(f"Správně, nejde to: {e}")

    print("\n--- Test 2: Světla ---")
    moje_svetlo = Lights("Lampa u gauče", "Obývák", "LED", 80, "Žlutá")
    print(moje_svetlo)
    
    # Změna jasu a barvy
    print("Měním jas a barvu...")
    moje_svetlo.setProperties(luminosity=20, color="Červená")
    print(moje_svetlo)

    # Zkouška získání jen něčeho
    info = moje_svetlo.getProperties(luminosity=True)
    print(f"Aktuální jas ze slovníku: {info}")

    # Zkouška chyby (Bonus)
    print("Pokus o nastavení nesmyslu:")
    moje_svetlo.setProperties(rychlost=100)

    print("\n--- Test 3: Router ---")
    muj_router = Routers("Main WiFi", "Chodba", "192.168.0.1", [2.4, 5], True)
    print(muj_router)

    # Změna IP
    muj_router.setProperties(IP="10.0.0.138")
    print(f"Nová IP: {muj_router.getProperties(IP=True)}")
