# ===============================

# 1. Rodičovská třída Account

# ===============================

class Account:

    def __init__(self, username, followers):

        self.username = username

        self.followers = max(0, followers)

    def add_followers(self, count):

        self.followers += count

        if self.followers < 0:

            self.followers = 0

    def __str__(self):

        return f"Uživatel: {self.username}, sledujících: {self.followers}"

    def __del__(self):

        print(f"Účet {self.username} byl odstraněn ze systému.")


# ===========================================

# 2. Potomek VerifiedAccount (dědí z Account)

# ===========================================

class VerifiedAccount(Account):

    def __init__(self, username, followers, badge_color):

        super().__init__(username, followers)

        self.badge_color = badge_color

    def __str__(self):

        base = super().__str__()

        return f"{base}, ověřený účet (odznak: {self.badge_color})"

    def promote(self, count):

        self.followers += count

        print(f"Účet {self.username} získal {count} nových sledujících!")


# ======================

# 3. Hlavní program

# ======================

def main():

    # 1. Jeden běžný uživatel

    user1 = Account("cool_student_23", 150)

    # 2. Jeden ověřený uživatel

    star = VerifiedAccount("singer_official", 10500, "zlatá")

    # 3. Běžný uživatel – přidání sledujících

    user1.add_followers(30)

    user1.add_followers(-10)

    # 4. Ověřený uživatel – promote()

    star.promote(500)

    # 5. Výpis obou účtů

    print(user1)

    print(star)

    # 6. Odstranění objektů

    del user1

    del star


# Spuštění hlavního programu

main()
 
