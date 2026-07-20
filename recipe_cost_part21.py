# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: RecipeCost
def get_due_tomorrow():
    """Возвращает список напоминаний, срок которых наступил завтра."""
    from datetime import date, timedelta
    tomorrow = date.today() + timedelta(days=1)
    due = []
    for item in _reminders:
        if isinstance(item["due"], date) and item["due"] == tomorrow:
            due.append(item)
    return due

def mark_reminder_done(reminder_id):
    """Отметить напоминание как выполненное."""
    for i, item in enumerate(_reminders):
        if item.get("id") == reminder_id or (not "id" in item and i < len(_reminders)):
            item["done"] = True
            _reminders.pop(i)
            return True
    return False

def add_reminder(note, due_date=None):
    """Добавить напоминание с текстом и датой."""
    from datetime import date
    if isinstance(due_date, str):
        try:
            due_date = date.fromisoformat(due_date)
        except ValueError:
            return None
    item = {"note": note, "due": due_date or date.today(), "done": False}
    _reminders.append(item)
    return item

_reminders = []  # Хранилище напоминаний
