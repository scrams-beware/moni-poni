# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: RecipeCost
def print_summary():
    """Выводит краткую сводку по текущим данным рецепта."""
    if not recipe:
        print("Нет данных для отображения.")
        return
    total = sum(ingredient["price"] * ingredient["amount"] for ingredient in ingredients)
    cost_per_portion = total / num_servings if num_servings else 0.0
    print(f"Рецепт: {recipe.get('name', 'Без названия')}")
    print(f"Ингредиенты: {len(ingredients)} шт.")
    print(f"Порций: {num_servings}")
    print(f"Общая стоимость ингредиентов: {total:.2f} руб.")
    print(f"Себестоимость одной порции: {cost_per_portion:.2f} руб.")
