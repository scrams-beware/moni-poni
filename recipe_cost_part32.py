# === Stage 32: Добавь журнал действий пользователя ===
# Project: RecipeCost
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action, details=""):
        self.entries.append({"action": action, "details": details, "timestamp": time.time()})

    def get_last(self, n=5):
        return self.entries[-n:]

    def get_all(self):
        return self.entries
