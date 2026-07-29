# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: RecipeCost
def reset_demo_data():
    """Сбрасывает все данные в начальные демо-значения."""
    global recipes, ingredients, categories, suppliers, costs
    if 'recipes' not in globals():
        recipes = {}
    if 'ingredients' not in globals():
        ingredients = {}
    if 'categories' not in globals():
        categories = {}
    if 'suppliers' not in globals():
        suppliers = {}
    if 'costs' not in globals():
        costs = {}

def clear_all_data():
    """Полностью очищает все данные и состояние."""
    global recipes, ingredients, categories, suppliers, costs
    for key in ['recipes', 'ingredients', 'categories', 'suppliers', 'costs']:
        if key in globals() and isinstance(globals()[key], dict):
            del globals()[key]

if __name__ == '__main__':
    reset_demo_data()
    print('Demo data reset successfully.')
