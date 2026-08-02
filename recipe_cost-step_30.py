# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: RecipeCost
class Profile:
    def __init__(self, name, discount_rate=0, tax_rate=0):
        self.name = name
        self.discount_rate = discount_rate  # 0..1
        self.tax_rate = tax_rate            # 0..1
    def apply(self, cost):
        return cost * (1 - self.discount_rate) * (1 + self.tax_rate)

profiles_db = {}

def add_profile(name, discount=0, tax=0):
    profiles_db[name] = Profile(name, discount, tax)

def get_profile(name):
    return profiles_db.get(name)

def list_profiles():
    return dict(profiles_db)
