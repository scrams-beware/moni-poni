# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: RecipeCost
def load_data_from_json(file_path):
    try:
        import json
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Файл JSON должен содержать объект (словарь), а не массив или скаляр.")
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле '{file_path}': {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла '{file_path}': {type(e).__name__}: {e}")
        return None
