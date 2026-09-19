# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: RecipeCost
def _format_report(results):
    """Форматирует результаты калькуляции в читаемый отчёт."""
    lines = []
    lines.append("=== Отчёт RecipeCost ===")
    lines.append(f"Всего рецептов: {len(results)}")
    lines.append("-" * 30)
    for r in results:
        name = r.get("name", "Без имени")
        cost = r.get("cost", 0)
        portions = r.get("portions", 1)
        per = r.get("per_portion", 0)
        lines.append(f"{name}: {cost:.2f} за {portions} порции ({per:.2f}/порц.)")
    lines.append("-" * 30)
    total_cost = sum(r.get("cost", 0) for r in results)
    lines.append(f"Итого себестоимость: {total_cost:.2f}")
    return "\n".join(lines)
