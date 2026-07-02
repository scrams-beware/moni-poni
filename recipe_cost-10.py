# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: RecipeCost
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "recipes": recipes,
        "ingredients": ingredients,
        "prices": prices,
        "last_calculation": last_calculation_timestamp if 'last_calculation_timestamp' in globals() else None,
        "exported_at": datetime.now().isoformat(),
        "version": 1.0
    }
    return json.dumps(state, indent=2)
