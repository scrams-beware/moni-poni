# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: RecipeCost
def migrate_to_v46():
    """Миграция: добавляем поля cost_per_unit и unit_label в структуру рецепта."""
    global recipes
    if 'recipes' not in globals():
        recipes = []
    for recipe in recipes:
        if 'cost_per_unit' not in recipe:
            recipe['cost_per_unit'] = 0
        if 'unit_label' not in recipe:
            recipe['unit_label'] = 'шт'
