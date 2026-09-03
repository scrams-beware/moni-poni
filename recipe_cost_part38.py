# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: RecipeCost
def test_edge_cases(recipe_cost):
    # 1. Пустой рецепт и пустой каталог
    recipe_cost.katalog.clear()
    recipe_cost.ingred.clear()
    assert recipe_cost.calc_cost(0, 0) == 0.0

    # 2. Ноль порций
    recipe_cost.katalog["r1"] = {"название": "Р", "ингредиенты": {}, "порции": 1}
    assert recipe_cost.calc_cost("r1", 0) == 0.0

    # 3. Отрицательные порции возвращают 0
    assert recipe_cost.calc_cost("r1", -5) == 0.0

    # 4. Невалидный ID рецепта
    assert recipe_cost.calc_cost("n_such_id", 1) == 0.0

    # 5. Неизвестный ингредиент в рецепте
    recipe_cost.ingred["i1"] = {"название": "И", "цена": 100}
    recipe_cost.katalog["r1"]["ингредиенты"]["x"] = {"название": "Х", "количество": 1}
    assert recipe_cost.calc_cost("r1", 1) == 0.0

    # 6. Цена ингредиента 0 — бесплатно
    recipe_cost.ingred["i1"] = {"название": "И", "цена": 0}
    recipe_cost.katalog["r1"]["ингредиенты"]["i1"] = {"название": "И", "количество": 10}
    assert recipe_cost.calc_cost("r1", 1) == 0.0

    # 7. Дробные порции
    recipe_cost.katalog["r1"]["ингредиенты"]["i1"] = {"название": "И", "количество": 1}
    assert recipe_cost.calc_cost("r1", 0.5) == 50.0
    assert recipe_cost.calc_cost("r1", 1.5) == 150.0

    # 8. Дробные количества ингредиентов
    recipe_cost.katalog["r2"] = {"название": "Р2", "ингредиенты": {"i1": {"название": "И", "количество": 0.5}}, "порции": 1}
    assert recipe_cost.calc_cost("r2", 1) == 50.0

    # 9. Очень большие числа
    recipe_cost.katalog["r1"]["ингредиенты"]["i1"] = {"название": "И", "количество": 1}
    assert recipe_cost.calc_cost("r1", 1000000) == 100000000.0

    # 10. Цена в миллион
    recipe_cost.ingred["i1"] = {"название": "И", "цена": 1000000}
    recipe_cost.katalog["r1"]["ингредиенты"]["i1"] = {"название": "И", "количество": 1}
    assert recipe_cost.calc_cost("r1", 1) == 1000000.0
