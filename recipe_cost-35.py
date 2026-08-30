# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: RecipeCost
def show_summary(recipe):
    """Показать сводку по рецепту: ингредиенты, себестоимость, маржа."""
    print(f"\n{'─'*50}")
    print(f"Рецепт: {recipe.name}")
    print(f"{'─'*50}")
    if not recipe.ingredients:
        print("  (Нет ингредиентов)")
        return
    total_cost = 0
    for ing in recipe.ingredients:
        cost = ing.price * ing.quantity
        total_cost += cost
        print(f"  {ing.quantity:>2} x {ing.name} = {cost:.2f} руб.")
    print(f"{'─'*50}")
    print(f"  Итого: {total_cost:.2f} руб.")
    if recipe.portions:
        per_portion = total_cost / recipe.portions
        print(f"  На порцию: {per_portion:.2f} руб.")
    if recipe.selling_price:
        margin = (recipe.selling_price - total_cost) / recipe.selling_price * 100
        print(f"  Прибыль: {margin:+.1f}%")
    print(f"{'─'*50}\n")
