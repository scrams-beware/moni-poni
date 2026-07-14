# === Stage 17: Добавь группировку записей по категориям ===
# Project: RecipeCost
def group_by_category(records, categories):
    grouped = {}
    for rec in records:
        cat = rec.get("category") or "Uncategorized"
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(rec)
    return groups
