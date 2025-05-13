import random

# Vygeneruj 10 náhodných čísel mezi 1 a 100
puvodni_pole = [random.randint(1, 100) for _ in range(10)]

# Seřaď pole
serazene_pole = sorted(puvodni_pole)

# Výpis
print("Původní pole:", puvodni_pole)
print("Seřazené pole:", serazene_pole)
