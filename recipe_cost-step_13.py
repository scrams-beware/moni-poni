# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: RecipeCost
def fuzzy_search(query, data, fields):
    query = query.strip().lower()
    if not query:
        return []
    results = []
    for item in data:
        score = 0
        for field in fields:
            val = str(item.get(field, '')).strip().lower()
            if query in val:
                score += 1
        if score > 0:
            results.append((score, item))
    return [item for _, item in sorted(results, reverse=True)]
