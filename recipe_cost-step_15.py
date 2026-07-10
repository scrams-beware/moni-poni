# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: RecipeCost
def weekly_stats_by_date(self):
    """Returns dict {date: {'recipes': list, 'total_cost': float, 'avg_per_serving': float}} for each date present."""
    from collections import defaultdict
    stats = defaultdict(lambda: {"recipes": [], "total_cost": 0.0, "total_servings": 0})
    for recipe in self._recipes.values():
        if not recipe.is_valid():
            continue
        d = recipe.serving_date() or today()
        stats[d]["recipes"].append(recipe)
        stats[d]["total_cost"] += recipe.total_cost
        stats[d]["total_servings"] += recipe.total_servings
    return {date: {"recipes": s["recipes"], "total_cost": round(s["total_cost"], 2),
                    "avg_per_serving": round(s["total_cost"] / max(s["total_servings"], 1), 2)}
            for date, s in sorted(stats.items())}
