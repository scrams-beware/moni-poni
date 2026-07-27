# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: RecipeCost
def run_demo():
    print("=== RecipeCost Demo ===")
    
    # 1. Добавить ингредиенты
    recipe = {"name": "Паста Карбонара", "portions": 4}
    ingredients = [
        {"item": "Спагетти", "amount": 0.3, "unit": "кг"},
        {"item": "Бекон", "amount": 0.15, "unit": "кг"},
        {"item": "Яйца (L)", "amount": 4, "unit": "шт."},
        {"item": "Сыр Пармезан", "amount": 0.06, "unit": "кг"},
    ]
    
    # 2. Добавить цены
    prices = {
        "Спагетти": 180,     # руб/кг
        "Бекон": 450,         # руб/кг
        "Яйца (L)": 65,       # руб/шт
        "Сыр Пармезан": 900,  # руб/кг
    }
    
    # 3. Рассчитать стоимость ингредиентов
    total_ingredients = sum(ing["amount"] * prices[ing["item"]] for ing in ingredients)
    cost_per_portion = total_ingredients / recipe["portions"]
    
    print(f"Рецепт: {recipe['name']}")
    print(f"Ингредиентов: {len(ingredients)} шт.")
    print(f"Порций: {recipe['portions']}")
    print(f"Общая стоимость ингредиентов: {total_ingredients:.2f} руб.")
    print(f"Стоимость на порцию: {cost_per_portion:.2f} руб.")
    
    # 4. Показать детали по каждому ингредиенту
    print("\nДетализация:")
    for ing in ingredients:
        cost = ing["amount"] * prices[ing["item"]]
        print(f"  • {ing['item']:15s}: {ing['amount']} × {prices[ing['item']]} = {cost:.2f} руб.")
    
    # 5. Простой отчёт-итог
    print("\n=== ИТОГО ===")
    print(f"Всего на ингредиенты: {total_ingredients:.2f} руб.")
    print(f"На одну порцию:      {cost_per_portion:.2f} руб.")
    
    # 6. Простой тест: если стоимость > 500 — выводим предупреждение
    if cost_per_portion > 500:
        print("⚠️  Порция дороже 500 руб! Возможно, нужно поискать дешевле.")
    else:
        print("✅ Цена на порцию в пределах нормы.")

if __name__ == "__main__":
    run_demo()
