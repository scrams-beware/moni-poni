# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: RecipeCost
def print_usage_scenarios():
    """
    Демонстрирует основные сценарии использования RecipeCost.
    """
    print("=" * 60)
    print("SCENARIO 1: Добавление ингредиентов и расчёт себестоимости")
    print("=" * 60)
    print(">>> from recipe_cost import Ingredient, Recipe, Report")
    print(">>> flour = Ingredient('flour', 100, 5.0)")
    print(">>> eggs = Ingredient('eggs', 10, 2.5)")
    print(">>> butter = Ingredient('butter', 250, 3.0)")
    print(">>> cake = Recipe('cake', 500, [flour, eggs, butter])")
    print(">>> print(cake.cost_per_portion)")
    print()

    print("=" * 60)
    print("SCENARIO 2: Загрузка из JSON и генерация отчёта")
    print("=" * 60)
    print(">>> import json")
    print(">>> data = json.load(open('recipe_data.json'))")
    print(">>> report = Report.generate(data)")
    print(">>> report.display('cost_report.txt')")
    print()

    print("=" * 60)
    print("SCENARIO 3: Сравнение рецептов")
    print("=" * 60)
    print(">>> recipe_a = load_recipe('a.json')")
    print(">>> recipe_b = load_recipe('b.json')")
    print(">>> print(Report.compare(recipe_a, recipe_b))")
    print()

    print("=" * 60)
    print("SCENARIO 4: Экспорт в CSV")
    print("=" * 60)
    print(">>> report.to_csv('recipes.csv')")
    print(">>> report.to_html('report.html')")
    print()

    print("=" * 60)
    print("SCENARIO 5: Подсчёт общих ингредиентов")
    print("=" * 60)
    print(">>> common = Recipe.find_common(recipe_a, recipe_b)")
    print(">>> print(common)")
    print()

    print("=" * 60)
    print("SCENARIO 6: Загрузка и отображение базы рецептов")
    print("=" * 60)
    print(">>> base = Base.load('recipes_db.json')")
    print(">>> base.display_all()")
    print(">>> base.save('recipes_db_updated.json')")
    print()


if __name__ == "__main__":
    print_usage_scenarios()
