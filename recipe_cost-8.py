# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: RecipeCost
def print_menu():
    print("\n=== RecipeCost Menu ===")
    print("1. Add Ingredient (name, price_per_unit)")
    print("2. Add Recipe (name, servings)")
    print("3. Add Item to Recipe (ingredient_name, amount_needed)")
    print("4. Calculate Cost for a Recipe")
    print("5. Generate Summary Report")
    print("6. Exit")

def run_cli():
    ingredients = {}
    recipes = {}
    recipe_items = {}  # {recipe_id: [(item_name, amount)]}
    
    while True:
        try:
            choice = input(print_menu()).strip()
            
            if choice == "1":
                name = input("Ingredient Name: ").strip()
                price = float(input("Price per Unit: "))
                ingredients[name] = price
                
            elif choice == "2":
                name = input("Recipe Name: ").strip()
                servings = int(input("Servings: "))
                recipes[name] = {"servings": servings, "items": []}
                
            elif choice == "3":
                recipe_name = input("Recipe Name: ").strip()
                if recipe_name not in recipes:
                    print(f"Error: Recipe '{recipe_name}' does not exist.")
                    continue
                    
                item_name = input("Ingredient Name: ").strip()
                amount_needed = float(input("Amount Needed (e.g., 0.5 kg): "))
                
                if item_name not in ingredients:
                    print(f"Error: Ingredient '{item_name}' is not registered.")
                    continue
                
                recipes[recipe_name]["items"].append((item_name, amount_needed))
                recipe_items.setdefault(recipe_name, []).append((item_name, amount_needed))
                
            elif choice == "4":
                if not recipes:
                    print("No recipes defined yet.")
                    continue
                    
                target_recipe = input("Select Recipe to Calculate: ").strip()
                if target_recipe in recipes:
                    total_cost = 0.0
                    for item_name, amount_needed in recipe_items.get(target_recipe, []):
                        unit_price = ingredients[item_name]
                        cost_for_item = unit_price * amount_needed
                        total_cost += cost_for_item
                    
                    print(f"\n--- Cost Report for '{target_recipe}' ---")
                    print(f"Servings: {recipes[target_recipe]['servings']}")
                    print(f"Total Ingredients Cost: ${total_cost:.2f}")
                    
                    if recipes[target_recipe]["servings"] > 0:
                        cost_per_serving = total_cost / recipes[target_recipe]["servings"]
                        print(f"Cost per Serving: ${cost_per_serving:.2f}")
                    else:
                        print("Cannot calculate per serving (0 servings defined).")
                else:
                    print(f"Error: Recipe '{target_recipe}' not found.")
                    
            elif choice == "5":
                if not recipes:
                    print("No data available for report.")
                    continue
                    
                print("\n=== Summary Report ===")
                total_ingredients_cost = 0.0
                for recipe_name, data in recipes.items():
                    items = recipe_items.get(recipe_name, [])
                    cost = sum(ingredients[item[0]] * item[1] for item in items)
                    servings = data["servings"]
                    
                    print(f"\nRecipe: {recipe_name}")
                    print(f"  Servings: {servings}")
                    if servings > 0:
                        per_serving = cost / servings
                        print(f"  Cost per Serving: ${per_serving:.2f}")
                        
                    for item, qty in items:
                        unit_price = ingredients[item]
                        line_cost = unit_price * qty
                        total_ingredients_cost += line_cost
                        print(f"  - {item}: {qty} units @ ${unit_price:.2f}/unit -> ${line_cost:.2f}")
                        
                print(f"\nTotal Cost of All Recipes: ${total_ingredients_cost:.2f}")
                
            elif choice == "6":
                print("Exiting RecipeCost. Goodbye!")
                break
                
            else:
                print("Invalid option, please try again.")
        except ValueError as e:
            print(f"Input error: {e}. Please enter valid numbers where required.")
        except KeyboardInterrupt:
            print("\nInterrupted by user. Exiting...")
            break
