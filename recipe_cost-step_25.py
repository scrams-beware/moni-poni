# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: RecipeCost
def parse_date(date_str):
    """Парсинг даты в форматах DD.MM.YYYY, MM.DD.YYYY, YYYY-MM-DD."""
    import datetime
    for fmt in ('%d.%m.%Y', '%m.%d.%Y', '%Y-%m-%d'):
        try:
            return datetime.date.fromisoformat(date_str.replace('.', '-')) if fmt == '%Y-%m-%d' else datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Некорректная дата: {date_str}. Ожидаются форматы DD.MM.YYYY, MM.DD.YYYY или YYYY-MM-DD")

def validate_date_range(start_str, end_str):
    """Проверка корректности диапазона дат."""
    try:
        start = parse_date(start_str)
        end = parse_date(end_str)
        if start > end:
            raise ValueError(f"Дата начала ({start}) позже даты конца ({end}).")
        return start, end
    except Exception as e:
        print(f"Ошибка валидации дат: {e}")
        return None, None
