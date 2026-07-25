# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: RecipeCost
def print_recipe_report(recipe: dict, ingredient_costs: list) -> None:
    """Compact one-line-per-recipe report with details."""
    name = recipe.get("name", "Unknown")
    servings = recipe.get("servings", 1)
    total_cost = sum((i["weight"] * i["unit_price"]) for i in ingredient_costs if i.get("recipe_id") == name or not i.get("recipe_id"))
    cost_per_serving = (total_cost / servings) if servings else float('inf')
    print(f"{'─'*40}")
    print(f"  {name} | {servings} порций | себестоимость: {cost_per_serving:.2f} руб/порцию")
