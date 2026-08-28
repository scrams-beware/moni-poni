# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: RecipeCost
TEMPLATES = {
    "snack": {
        "name": "Snack",
        "portions": 1,
        "ingredients": [
            {"name": "bread", "amount": 2, "unit": "slices"},
            {"name": "cheese", "amount": 30, "unit": "g"},
            {"name": "butter", "amount": 15, "unit": "g"},
            {"name": "salt", "amount": 2, "unit": "g"},
        ],
    },
    "soup": {
        "name": "Soup",
        "portions": 4,
        "ingredients": [
            {"name": "potato", "amount": 500, "unit": "g"},
            {"name": "onion", "amount": 200, "unit": "g"},
            {"name": "carrot", "amount": 200, "unit": "g"},
            {"name": "oil", "amount": 30, "unit": "ml"},
            {"name": "salt", "amount": 5, "unit": "g"},
            {"name": "water", "amount": 2000, "unit": "ml"},
        ],
    },
    "salad": {
        "name": "Salad",
        "portions": 3,
        "ingredients": [
            {"name": "cucumber", "amount": 300, "unit": "g"},
            {"name": "tomato", "amount": 400, "unit": "g"},
            {"name": "lettuce", "amount": 200, "unit": "g"},
            {"name": "olive_oil", "amount": 30, "unit": "ml"},
            {"name": "lemon_juice", "amount": 15, "unit": "ml"},
            {"name": "salt", "amount": 3, "unit": "g"},
        ],
    },
}
