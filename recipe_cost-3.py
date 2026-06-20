# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: RecipeCost
class RecipeCostState:
    def __init__(self):
        self.ingredients = {}  # id -> {name, price_per_unit}
        self.recipes = {}      # name -> {ingredients: [{id, amount}], servings}
        self.history = []      # list of operations for reporting

    def add_ingredient(self, ingredient_id: str, name: str, price: float):
        if not self.ingredients.get(ingredient_id):
            self.ingredients[ingredient_id] = {"name": name, "price_per_unit": price}
            self.history.append(f"ADD_INGREDIENT:{ingredient_id}:{name}")

    def add_recipe(self, recipe_name: str, servings: int, ingredient_entries: list):
        if not self.recipes.get(recipe_name):
            entries_data = [{"id": e[0], "amount": float(e[1])} for e in ingredient_entries]
            self.recipes[recipe_name] = {"ingredients": entries_data, "servings": servings}
            self.history.append(f"ADD_RECIPE:{recipe_name}:{servings}")

    def get_total_cost(self, recipe_name: str) -> float | None:
        if not self.recipes.get(recipe_name):
            return None
        data = self.recipes[recipe_name]
        total = 0.0
        for entry in data["ingredients"]:
            ing_id = entry["id"]
            amount = entry["amount"]
            price_unit = self.ingredients.get(ing_id, {}).get("price_per_unit", 0)
            total += amount * price_unit
        return round(total / data["servings"], 2)

    def get_report(self):
        lines = ["=== RecipeCost Report ===", f"Ingredients: {len(self.ingredients)}"]
        for name, data in self.recipes.items():
            cost = self.get_total_cost(name)
            lines.append(f"{name}: {cost} per serving")
        return "\n".join(lines)
