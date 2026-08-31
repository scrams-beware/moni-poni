# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: RecipeCost
import json
import os

def integrity_check(data, expected_keys=None):
    """Проверяет наличие обязательных ключей в структуре данных."""
    if expected_keys is None:
        expected_keys = ["recipe_name", "ingredients", "servings"]
    
    for key in expected_keys:
        if key not in data:
            return False, f"Отсутствует ключ: {key}"
    
    if not isinstance(data["ingredients"], list):
        return False, "Поле ingredients должно быть списком"
    
    for i, ing in enumerate(data["ingredients"]):
        if not isinstance(ing, dict):
            return False, f"Ингредиент в позиции {i} должен быть словарём"
        if "name" not in ing or "amount" not in ing or "unit" not in ing:
            return False, f"Ингредиент в позиции {i} неполный: {ing}"
    
    return True, "Все проверки пройдены"

def repair_simple_issues(data):
    """Ремонтирует простые проблемы: дубликаты ингредиентов, пустые названия."""
    repaired = False
    
    # Убираем дубликаты по имени с сохранением последнего
    seen = {}
    unique_ingredients = []
    for ing in data.get("ingredients", []):
        name = ing.get("name", "")
        if name and name not in seen:
            seen[name] = ing
            unique_ingredients.append(ing)
    
    if len(unique_ingredients) != len(data.get("ingredients", [])):
        data["ingredients"] = unique_ingredients
        repaired = True
    
    # Заполняем пустые названия
    if "ingredients" in data:
        for ing in data["ingredients"]:
            if not ing.get("name"):
                ing["name"] = "Неизвестный ингредиент"
                repaired = True
    
    return data, repaired
