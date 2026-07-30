# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: RecipeCost
def calculate_metrics(ingredients: list, portions: int) -> dict:
    """Вычисляет ключевые метрики себестоимости рецепта."""
    total_cost = sum((ing['price'] * ing['amount']) for ing in ingredients if isinstance(ing.get('quantity'), (int, float)))
    cost_per_portion = total_cost / portions if portions else 0.0
    avg_price_ingredient = sum(ing['price'] for ing in ingredients) / len(ingredients) if ingredients else 0.0
    return {
        'total_cost': round(total_cost, 2),
        'cost_per_portion': round(cost_per_portion, 2),
        'avg_price_ingredient': round(avg_price_ingredient, 2),
        'num_ingredients': len(ingredients)
    }
