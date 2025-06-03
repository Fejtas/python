def vypocitej_objem_jehlanu(a, v): 
    if a <= 0 or v <= 0:
        return "Strana a a výška v musí být kladné číslo." 
    
    objem = (1/3) * (a ** 2) * v 
    return f"Objem pravidelného čtyřbokého jehlanu je {objem:.2f} jednotek krychlových." 

# Příklad: strana a = 4, výška = 9 
a = 4 
v = 9 

# Výpočet 
výsledek = vypocitej_objem_jehlanu(a, v) 
print (výsledek) 
