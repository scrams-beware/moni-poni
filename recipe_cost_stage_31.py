# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: RecipeCost
def switch_profile(new_username):
    if new_username:
        for user in users.values():
            user['is_active'] = False
        active_user = next((u for u in users.values() if u['username'] == new_username), None)
        if not active_user:
            print(f"Профиль пользователя '{new_username}' не найден.")
            return
        active_user['is_active'] = True
        print(f"Переключение на профиль: {active_user['username']}")

def get_active_profile():
    for user in users.values():
        if user['is_active']:
            return user
    return None
