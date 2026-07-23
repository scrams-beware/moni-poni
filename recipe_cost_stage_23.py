# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: RecipeCost
import sys, os
SCRIPT = os.path.abspath(__file__)
if SCRIPT.endswith('.py'):
    from . import _helpers
else:
    import _helpers as _helpers


def console_table(rows, headers):
    """Print a simple text table to stdout."""
    if not rows:
        return

    widths = []
    for i in range(len(headers)):
        w = len(str(headers[i]))
        for row in rows:
            w = max(w, len(str(row[i])))
        widths.append(w)

    lines = []
    sep = "─" * sum(widths + [2]) + "+"
    header_line = "|  ".join(
        str(h).ljust(widths[i]) for i in range(len(headers))
    )
    lines.append(sep)
    lines.append(f"| {header_line} |")
    lines.append(sep)

    row_strs = []
    for row in rows:
        cells = [str(row[i]).ljust(widths[i]) if i < len(row) else " " * widths[i]
                 for i in range(len(headers))]
        row_strs.append(f"| {' | '.join(cells)} |")

    lines.extend(row_strs + ["|", sep])
    sys.stdout.write("\n".join(lines))


def print_report(recipe):
    if recipe is None:
        return
    parts = []
    for key in ("name", "servings"):
        v = getattr(recipe, key, "")
        parts.append((key.upper(), str(v)))
    cost_parts = {}
    for ing in _helpers.INGREDIENTS.get(recipe.name, []):
        cost_parts[ing["name"]] = (ing["amount"], ing["price"])

    rows = [(k, v) for k, v in parts] + [
        ("ingredient", "cost"),
    ]
    headers = ["item", "value"]
    console_table(rows, headers)


def print_menu():
    recipes = _helpers.RECIPES if hasattr(_helpers, 'RECIPES') else []
    rows = [(r["name"], r.get("servings", 1)) for r in recipes]
    headers = ["recipe", "default servings"]
    console_table(rows, headers)


def print_summary():
    total = _helpers._total_cost if hasattr(_helpers, '_total_cost') else 0.0
    n = len(_helpers.RECIPES) if hasattr(_helpers, 'RECIPES') else 0
    rows = [("recipes loaded", str(n)), ("estimated total cost", f"${total:.2f}")]
    headers = ["metric", "value"]
    console_table(rows, headers)


def main():
    print("=== RecipeCost Calculator ===")
    print_summary()
    print_menu()
