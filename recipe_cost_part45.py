# === Stage 45: Добавь восстановление из резервной копии ===
# Project: RecipeCost
import os
import sys
import json
import pickle

def load_backup_file(file_path):
    """Загружает резервную копию из pickle-файла."""
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"Резервная копия не найдена: {file_path}")
        return None
    except Exception as e:
        print(f"Ошибка при загрузке резервной копии: {e}")
        return None

def load_backup_json(file_path):
    """Загружает резервную копию из JSON-файла."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Резервная копия не найдена: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка при загрузке JSON-резервной копии: {e}")
        return None
    except Exception as e:
        print(f"Ошибка при загрузке резервной копии: {e}")
        return None

def save_backup_pickle(data, file_path):
    """Сохраняет резервную копию в pickle-файл."""
    try:
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
        print(f"Резервная копия сохранена: {file_path}")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении резервной копии: {e}")
        return False

def save_backup_json(data, file_path):
    """Сохраняет резервную копию в JSON-файл."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Резервная копия сохранена: {file_path}")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении резервной копии: {e}")
        return False
