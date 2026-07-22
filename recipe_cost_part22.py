# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: RecipeCost
def check_expired_reminders():
    """Проверяет напоминания о просроченных ингредиентах и выводит предупреждения."""
    expired = []
    today = datetime.date.today()
    for ingredient in ingredients:
        if "last_date" in ingredient and ingredient["last_date"]:
            last = ingredient["last_date"]
            if isinstance(last, str):
                try:
                    last = datetime.strptime(last[:10], "%Y-%m-%d").date()
                except ValueError:
                    continue
            days_ago = (today - last).days
            if days_ago > 3 and ingredient.get("category") in ("meat", "fish", "dairy"):
                expired.append({
                    "name": ingredient["name"],
                    "last_date": str(last),
                    "category": ingredient["category"]
                })

    if expired:
        print("\n⚠️  Напоминания о скоропортящихся ингредиентах:")
        for item in sorted(expired, key=lambda x: x["last_date"], reverse=True):
            print(f"   - {item['name']} (последний срок: {item['last_date']}) — категория: {item['category']}")
    else:
        print("\n✅ Все скоропортящиеся ингредиенты в норме. Просроченных напоминаний нет.")


# Пример использования:
if __name__ == "__main__":
    ingredients = [
        {"name": "Молоко", "price": 85, "unit": "л", "category": "dairy", "last_date": "2024-10-15"},
        {"name": "Курица", "price": 350, "unit": "кг", "category": "meat", "last_date": "2024-11-01"},
        {"name": "Рыба треска", "price": 600, "unit": "кг", "category": "fish", "last_date": "2024-10-28"},
    ]

    check_expired_reminders()
