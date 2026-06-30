# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: RecipeCost
import json, sys

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        ingredients_map = {}
        for ing in data.get('ingredients', []):
            key = f"{ing['name'].lower()} {ing['unit']}"
            ingredients_map[key] = {'price': float(ing['price']), 'unit': ing['unit']}
        
        recipes = []
        for rec in data.get('recipes', []):
            recipe_id = rec['id']
            base_servings = rec.get('base_servings', 1)
            
            ingredients_needed = {}
            total_cost = 0.0
            
            for item in rec.get('ingredients', []):
                ing_name = item['name'].lower()
                unit = item['unit']
                key = f"{ing_name} {unit}"
                
                if key not in ingredients_map:
                    print(f"Предупреждение: ингредиент '{key}' не найден в справочнике.")
                    continue
                
                price_per_unit = ingredients_map[key]['price']
                amount_needed = item['amount'] / base_servings * rec.get('servings', 1)
                
                cost_for_this_ing = amount_needed * price_per_unit
                total_cost += cost_for_this_ing
                
                if key not in ingredients_needed:
                    ingredients_needed[key] = {'total_amount': 0, 'cost': 0}
                
                ingredients_needed[key]['total_amount'] += amount_needed
                ingredients_needed[key]['cost'] += cost_for_this_ing
            
            recipes.append({
                'id': recipe_id,
                'name': rec['name'],
                'servings': rec.get('servings', base_servings),
                'ingredients': list(ingredients_needed.values()),
                'total_cost': round(total_cost, 2)
            })
        
        return {'ingredients': ingredients_map, 'recipes': recipes}
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

# Пример использования (раскомментируйте для запуска с данными):
# if __name__ == "__main__":
#     sample_data = '{"ingredients":[{"name":"яйцо","unit":"шт","price":50},{"name":"мука","unit":"кг","price":80}],"recipes":[{"id":1,"name":"Омлет","servings":2,"base_servings":2,"ingredients":[{"name":"яйцо","amount":4},{"name":"мука","amount":0.1}]}]}'
#     loaded = load_initial_data(sample_data)
#     print(f"Загружено {len(loaded['recipes'])} рецептов.")
