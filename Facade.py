import time
import random

# --- 0. Definice vlastních chyb (pro simulaci specifických problémů) ---

class NeniSklademError(Exception):
    pass

class PlatbaZamitnutaError(Exception):
    pass

# --- 1. Subsystémy (Sklad, Banka, Logistika) ---

class SkladovySystem:
    """Subsystém 1: Hlídá zásoby."""
    def zkontroluj_dostupnost(self, produkt):
        print(f"   [Sklad]: Hledám ve skladu produkt '{produkt}'...")
        time.sleep(0.5)
        
        # Simulace: Produkty začínající na 'X' nejsou skladem (pro testování chyby)
        if produkt.startswith("X"):
            print(f"   [Sklad]: CHYBA! Produkt '{produkt}' již není skladem.")
            raise NeniSklademError(f"Produkt '{produkt}' vyprodán.")
        else:
            print(f"   [Sklad]: Produkt '{produkt}' je připraven k expedici.")
            return True

class BankovniSystem:
    """Subsystém 2: Řeší finance."""
    def proved_platbu(self, castka):
        print(f"   [Banka]: Pokus o stržení částky {castka} Kč...")
        time.sleep(0.5)
        
        # Simulace: Částky nad 10 000 Kč zamítne (nedostatek prostředků)
        if castka > 10000:
            print("   [Banka]: CHYBA! Platba zamítnuta (nedostatek limitu/prostředků).")
            raise PlatbaZamitnutaError("Platba neprošla.")
        else:
            print("   [Banka]: Platba úspěšně ověřena a provedena.")
            return True

class LogistickySystem:
    """Subsystém 3: Řeší dopravu."""
    def odeslat_zasilku(self, produkt):
        print("   [Logistika]: Generuji přepravní štítek...")
        cislo_zasilky = random.randint(1000, 9999)
        print(f"   [Logistika]: Balík s '{produkt}' předán kurýrovi. ID: CZ-{cislo_zasilky}")

# --- 2. Fasáda (E-shop Objednávka) ---

class ObjednavkovaFasada:
    """
    Fasáda, která sdružuje proces nákupu.
    Zajišťuje transakční zpracování - pokud selže platba, neposílá se balík.
    """
    def __init__(self):
        self.sklad = SkladovySystem()
        self.banka = BankovniSystem()
        self.logistika = LogistickySystem()

    def koupit_produkt(self, produkt, cena):
        print(f"\n--- FASÁDA: Zahajuji nákup: {produkt} ({cena} Kč) ---")
        
        try:
            # 1. Krok: Sklad (může vyvolat chybu)
            self.sklad.zkontroluj_dostupnost(produkt)
            
            # 2. Krok: Platba (pouze pokud je skladem, může vyvolat chybu)
            self.banka.proved_platbu(cena)
            
            # 3. Krok: Doprava (pouze pokud prošla platba)
            self.logistika.odeslat_zasilku(produkt)
            
            print("--- FASÁDA: Objednávka úspěšně dokončena! ---")
            return True

        except NeniSklademError as e:
            print(f"--- FASÁDA ZACHYTILA CHYBU: Omlouváme se, zboží došlo. ({e}) ---")
            return False
            
        except PlatbaZamitnutaError as e:
            print(f"--- FASÁDA ZACHYTILA CHYBU: Problém s platbou. ({e}) ---")
            return False
            
        except Exception as e:
            print(f"--- FASÁDA: Nastala neočekávaná chyba: {e} ---")
            return False

# --- 3. Hlavní program (Uživatel) ---

if __name__ == "__main__":
    eshop = ObjednavkovaFasada()

    print("=== E-SHOP KONZOLE (TESTOVÁNÍ FASÁDY) ===")
    print("TIP: Pro simulaci vyprodání zadejte produkt začínající na 'X'.")
    print("TIP: Pro simulaci zamítnuté karty zadejte cenu nad 10000.")

    while True:
        nazev_produktu = input("\nZadejte název produktu (nebo 'konec'): ")
        if nazev_produktu.lower() == 'konec':
            break
            
        try:
            cena_vstup = input("Zadejte cenu produktu (Kč): ")
            cena = int(cena_vstup)
        except ValueError:
            print("Chyba: Cena musí být číslo!")
            continue

        # Klient volá jen jednu metodu, nestará se o banku ani sklad
        # a nemusí ani řešit try-except bloky, protože to řeší Fasáda.
        uspech = eshop.koupit_produkt(nazev_produktu, cena)
        
        if uspech:
            print(f">> Systém: Děkujeme za nákup {nazev_produktu}.")
        else:
            print(f">> Systém: Nákup se nezdařil. Zkuste to znovu.")
