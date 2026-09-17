# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: RecipeCost
def demo():
    """Показывает основной пользовательский сценарий: добавление ингредиентов,
    создание рецепта, расчёт себестоимости и генерация отчёта."""
    from recipecost import (
        Ingredient, Recipe, CostReport,
        add_ingredient, add_ingredient_to_recipe,
        calculate_cost, generate_report,
        IngredientNotFoundError, RecipeNotFoundError,
    )

    # 1. Добавляем ингредиенты в базу
    flour = add_ingredient("flour", "pound", 5.50)
    eggs = add_ingredient("eggs", "dozen", 3.00)
    sugar = add_ingredient("sugar", "pound", 2.25)
    print("Ингредиенты добавлены: flour, eggs, sugar")

    # 2. Создаём рецепт
    recipe = Recipe("Simple Cake", 8)
    add_ingredient_to_recipe(recipe, flour, 2)
    add_ingredient_to_recipe(recipe, eggs, 3)
    add_ingredient_to_recipe(recipe, sugar, 1.5)
    print(f"Рецепт '{recipe.name}' создан с {len(recipe.ingredients)} ингредиентами")

    # 3. Расчёт стоимости
    cost = calculate_cost(recipe)
    print(f"Себестоимость: ${cost:.2f} за {recipe.servings} порций")
    print(f"Цена за порцию: ${cost / recipe.servings:.2f}")

    # 4. Генерация отчёта
    report = generate_report(recipe, cost)
    print("\n--- Отчёт ---")
    print(report)

    # 5. Проверка ошибок
    try:
        add_ingredient_to_recipe(recipe, flour, -1)
    except IngredientNotFoundError as e:
        print(f"\nОбработка ошибки: {e}")

    try:
        bad_recipe = Recipe("Nonexistent", 2)
        calculate_cost(bad_recipe)
    except RecipeNotFoundError as e:
        print(f"Обработка ошибки: {e}")

    print("\nДемо-сценарий завершен успешно!")

if __name__ == "__main__":
    demo()
