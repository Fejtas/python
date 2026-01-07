from abc import ABC, abstractmethod

# Abstraktní třída (Interface)
class Operation(ABC):
    
    @abstractmethod
    def calculate(self, *args):
        pass

# Třída pro sčítání
class Sum(Operation):
    def calculate(self, *args):
        # Funkce sum() je vestavěná funkce Pythonu, která sečte iterovatelný objekt
        return sum(args)

# Třída pro násobení
class Multiply(Operation):
    def calculate(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

# --- Hlavní část programu ---
if __name__ == "__main__":
    # Vytvoření objektu třídy Sum
    sum_obj = Sum()
    # Volání metody calculate s hodnotami 1, 3, 5, 0.1
    vysledek_sum = sum_obj.calculate(1, 3, 5, 0.1)
    print(f"Výsledek sčítání: {vysledek_sum}")

    # Vytvoření objektu třídy Multiply
    mul_obj = Multiply()
    # Volání metody calculate s hodnotami 1, 3, 5, 0.1
    vysledek_mul = mul_obj.calculate(1, 3, 5, 0.1)
    print(f"Výsledek násobení: {vysledek_mul}")
