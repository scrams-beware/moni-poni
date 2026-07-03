# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: RecipeCost
import json, os

DATA_FILE = "recipe_cost_data.json"

def save_to_json(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Save failed: {e}")
        return False

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return {"recipes": [], "ingredients": {}, "prices": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Ensure structure integrity on load
        if not all(k in data for k in ["recipes", "ingredients", "prices"]):
            return {"recipes": [], "ingredients": {}, "prices": []}
        return data
    except Exception as e:
        print(f"[ERROR] Load failed: {e}")
        return {"recipes": [], "ingredients": {}, "prices": []}

def merge_data(new_recipes, new_ingredients, new_prices):
    current = load_from_json()
    for r in new_recipes:
        if r.get("id"):
            existing_idx = next((i for i, x in enumerate(current["recipes"]) if x.get("id") == r["id"]), None)
            if existing_idx is not None:
                current["recipes"][existing_idx].update(r)
            else:
                current["recipes"].append(r)
    for ing_id, info in new_ingredients.items():
        current["ingredients"][ing_id] = info
    for p in new_prices:
        if p.get("ingredient_id") and p.get("price"):
            key = f"{p['currency']}_{p['unit']}"
            current["prices"][key] = {"value": p["price"], "currency": p["currency"]}
    return save_to_json(current)
