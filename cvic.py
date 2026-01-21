import sys
import time
import random
import socket
import os
import platform

# --- KONFIGURACE BAREV (ANSI) ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# --- ASCII ART DEXTER MORGAN ---
# Pouzivame 'raw string' (r""), aby zpetna lomitka nedelala problemy
DEXTER_ASCII = r"""
                           .. .  ..
                        . .: :: :: :. .
                       . .:: :: :: ::. .
                      . .::.:: . . ::. . .
                      . ::'         `:: .
                    .  :.  .......   .:  .
                   . .:   : ----- :   :. .
                   . ::  : / .-. \ :  :: .
                   . ::  :| ( O ) |:  :: .
                   . ::  :|  '-'  |:  :: .
                   . ::. : \  I  / : .:: .
                   .  ::. : '---' : .::  .
                    .  .:. ...... .:.  .
                  _  .  .::. ... .::.  .  _
                 ( \  .  .:: ... ::.  .  / )
                  \ \.  . .::. .::. .  ./ /
                   \ \  .  `:::::'  .  / /
              _--'  \ \ .   . : .   . / /  '--_
             /       \ \  . . : .  . / /       \
            /   / \   \ \   . : .   / /   / \   \
           /   /   \   \ \  ..:..  / /   /   \   \
          /   /     \   \ \  : :  / /   /     \   \
         /   /       \   \ \ :_: / /   /       \   \
        /   /         \   \ '---' /   /         \   \
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_print(text, speed=0.04, color=GREEN, end="\n"):
    """Simuluje psani na stroji/terminalu."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Nahodna variace rychlosti pro lidsky efekt
        time.sleep(speed + random.uniform(-0.01, 0.01))
    sys.stdout.write(RESET + end)

def loading_bar(task_name):
    """Falesny progress bar ve stylu Mr. Robot."""
    print(f"{CYAN}[*] {task_name}...{RESET}")
    sys.stdout.write(f"{RED}[")
    for _ in range(30):
        sys.stdout.write("#")
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.1))
    sys.stdout.write(f"] {GREEN}DONE{RESET}\n")
    time.sleep(0.5)

def get_system_intel():
    """Ziska skutecne informace o systemu uzivatele."""
    try:
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        os_info = platform.system() + " " + platform.release()
        return hostname, ip_addr, os_info
    except:
        return "UNKNOWN", "0.0.0.0", "UNKNOWN"

def entropy_encrypter():
    """Vizualni sifrovani zpravy."""
    clear_screen()
    typing_print("Zadej zprávu pro zašifrování (AES-256 simulace): ", color=WHITE, end="")
    msg = input(f"{GREEN}")
    print(RESET)
    
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    
    # Efekt Matrix/Sumu
    print(f"\n{RED}--- INICIALIZACE ŠIFROVÁNÍ ---{RESET}")
    for _ in range(15):
        temp_str = "".join([random.choice(chars) for _ in range(len(msg))])
        sys.stdout.write(f"\r{GREEN}{temp_str}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    
    # Finalni 'hash'
    final_hash = "".join([hex(ord(c))[2:] for c in msg])
    print(f"\r{BOLD}{YELLOW}PAYLOAD: {final_hash}{RESET}\n")
    typing_print("Zpráva byla skryta v šumu. Nikdo se nedívá.", speed=0.05)
    input(f"\n{WHITE}[Stiskni ENTER pro návrat]{RESET}")

def system_audit():
    """Skenuje 'dusi' pocitace."""
    clear_screen()
    h, i, o = get_system_intel()
    
    typing_print(f"Připojování k lokálnímu uzlu...", speed=0.03)
    loading_bar("Obcházení firewallu")
    
    print(f"\n{RED}----------------------------------------")
    print(f" CÍL IDENTIFIKOVÁN")
    print(f"----------------------------------------{RESET}")
    print(f" HOSTNAME : {WHITE}{h}{RESET}")
    print(f" ADRESA   : {WHITE}{i}{RESET}")
    print(f" SYSTÉM   : {WHITE}{o}{RESET}")
    print(f"{RED}----------------------------------------{RESET}\n")
    
    typing_print("Vím, kdo jsi. Vím, kde bydlí tvá data.", color=YELLOW, speed=0.06)
    input(f"\n{WHITE}[Stiskni ENTER pro návrat]{RESET}")

def psychological_protocol():
    """Generuje nahodne myslenky ve stylu Mr. Robot."""
    quotes = [
        "Kontrola je iluze.",
        "Démoni v nás nezmizí jen proto, že je ignorujeme.",
        "Svět je jen jedna velká hoax. Spamujeme jeden druhého svými komentáři.",
        "Chtěl jsem zachránit svět, ale neumím zachránit ani sebe.",
        "Jsme jen nuly a jedničky v chaosu."
    ]
    clear_screen()
    q = random.choice(quotes)
    typing_print(f"\"{q}\"", speed=0.1, color=CYAN)
    time.sleep(1)
    input(f"\n{WHITE}[Stiskni ENTER pro probuzení]{RESET}")

def dexter_protocol():
    """Zobrazi ASCII art Dextera."""
    clear_screen()
    typing_print("Probouzení Temného pasažéra...", speed=0.06, color=RED)
    time.sleep(1)
    loading_bar("Příprava sklíček")
    clear_screen()
    
    # Tisk ASCII artu najednou (typing efekt by byl moc pomaly)
    print(f"{RED}{BOLD}{DEXTER_ASCII}{RESET}")
    
    time.sleep(0.5)
    typing_print("\n\"Dnes večer je ta noc.\"", speed=0.12, color=WHITE)
    time.sleep(1)
    typing_print("Dívám se na krev. Vidím v ní vzorce. Vidím v ní tebe.", color=RED, speed=0.06)
    
    input(f"\n{WHITE}[Stiskni ENTER a ukliď nepořádek]{RESET}")


def main_menu():
    clear_screen()
    logo = f"""{RED}
    .  .
    |\/|
    |  |r. Robot Protocol v1.1
    {RESET}"""
    print(logo)
    
    print(f"{WHITE} 1.{RESET} {GREEN}Analýza Systému (Intel){RESET}")
    print(f"{WHITE} 2.{RESET} {GREEN}Šifrování Zprávy (Entropy){RESET}")
    print(f"{WHITE} 3.{RESET} {GREEN}Psychologický Protokol (Elliot){RESET}")
    print(f"{WHITE} 4.{RESET} {RED}Protokol: Bay Harbor Butcher (Dexter){RESET}")
    print(f"{WHITE} 5.{RESET} {WHITE}Smazat stopy (Exit){RESET}")
    
    choice = input(f"\n{WHITE}root@fsociety:~# {RESET}")
    return choice

# --- SPUSTENI ---
if __name__ == "__main__":
    try:
        clear_screen()
        typing_print("Ahoj, příteli...", speed=0.1, color=RED)
        time.sleep(0.5)
        
        while True:
            user_choice = main_menu()
            
            if user_choice == '1':
                system_audit()
            elif user_choice == '2':
                entropy_encrypter()
            elif user_choice == '3':
                psychological_protocol()
            elif user_choice == '4':
                dexter_protocol()
            elif user_choice == '5':
                clear_screen()
                typing_print("Bonsoir, Elliot.", color=RED)
                break
            else:
                typing_print("Chyba syntaxe.", color=RED, speed=0.02)
                time.sleep(0.5)
                
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Nucené ukončení. Data vymazána.{RESET}")
        sys.exit()
