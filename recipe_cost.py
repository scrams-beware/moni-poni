# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: RecipeCost
class RecipeCost:
    def __init__(self):
        self.recipes = {}
        self.ingredients = {}
    
    def add_ingredient(self, name, price_per_unit, unit='g'):
        if name not in self.ingredients:
            self.ingredients[name] = {'price': price_per_unit, 'unit': unit}
        return self
    
    def add_recipe(self, name):
        if name not in self.recipes:
            self.recipes[name] = []
        return self
    
    def add_item_to_recipe(self, recipe_name, ingredient_name, amount):
        if recipe_name in self.recipes and ingredient_name in self.ingredients:
            self.recipes[recipe_name].append({
                'ingredient': ingredient_name,
                'amount': amount
            })
        return self
    
    def calculate_cost(self, recipe_name, servings=1):
        if recipe_name not in self.recipes:
            print(f"Recipe '{recipe_name}' not found.")
            return 0.0
        
        total_cost = 0.0
        for item in self.recipes[recipe_name]:
            ingredient_data = self.ingredients[item['ingredient']]
            cost_per_unit = ingredient_data['price'] / (1 if ingredient_data['unit'] == 'g' else 1000)
            unit_amount = amount * servings
            total_cost += cost_per_unit * unit_amount
        
        return round(total_cost, 2)

if __name__ == '__main__':
    app = RecipeCost()
    
    # Ingredients
    app.add_ingredient('flour', 1.5).add_ingredient('sugar', 2.0).add_ingredient('eggs', 3.5)
    
    # Recipes
    cake_recipe = app.add_recipe('Chocolate Cake')\
        .add_item_to_recipe('Chocolate Cake', 'flour', 200)\
        .add_item_to_recipe('Chocolate Cake', 'sugar', 150)\
        .add_item_to_recipe('Chocolate Cake', 'eggs', 3)
    
    print(f"Cost of one Chocolate Cake: {cake_recipe.calculate_cost('Chocolate Cake')}")
