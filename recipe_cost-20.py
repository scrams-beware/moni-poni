# === Stage 20: Добавь восстановление записей из архива ===
# Project: RecipeCost
def restore_from_archive(archive_path, base_dir):
    """Восстанавливает записи из текстового архива .rec в текущий проект."""
    import json, os
    if not os.path.isfile(archive_path):
        print(f"Файл не найден: {archive_path}")
        return 0
    
    with open(archive_path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f.readlines()]
    
    records = []
    current = {}
    state = "ingredient"  # ingredient | portion | price | recipe
    
    for line in lines:
        if not line:
            continue
        
        parts = line.split("::")
        
        if len(parts) >= 2 and parts[0].strip().lower() == "recipe":
            current = {"name": parts[1], "portions": int(parts[2]) if len(parts) > 3 else 4, 
                       "ingredients": [], "costs": []}
            state = "ingredient"
        elif len(parts) >= 3 and state == "ingredient":
            current["ingredients"].append({"name": parts[1], "amount": float(parts[2]), "unit": parts[3]})
            state = "price"
        elif len(parts) >= 2 and state in ("price", "portion"):
            try:
                val = int(parts[0])
                if current["ingredients"]:
                    unit_price = float(parts[1]) / sum(i["amount"] for i in current["ingredients"])
                    total_cost = sum(i["amount"] * unit_price for i in current["ingredients"])
                    cost_per_portion = total_cost / max(current["portions"], 1)
                    current["costs"] = [total_cost, cost_per_portion]
                state = "recipe"
            except (ValueError, ZeroDivisionError):
                continue
    
    if current and len(current.get("ingredients", [])) > 0:
        records.append(current)
    
    print(f"Восстановлено {len(records)} рецептов из архива")
    return len(records)
