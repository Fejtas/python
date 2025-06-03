import math 

def vypocitej_objem_kuzele(r, v):
    if r <= 0 or v <= 0:
        return "Poloměr r a výška v musí být kladné číslo."
    
    objem = (1/3) * math.pi * (r ** 2) * v
    return f"Objem rotačního kužele je {objem:.2f} jednotek krychlových." 
# Příklad poloměr = 5, výška = 12 
r = 5
v = 12 

# Výpočet 
výsledek = vypocitej_objem_kuzele(r, v) 
print(výsledek) 
