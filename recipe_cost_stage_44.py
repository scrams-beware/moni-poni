# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: RecipeCost
import shutil, os, json, datetime

def backup_data_file(db_path, backup_dir=None):
    if not os.path.exists(db_path):
        return None
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(db_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(db_path)}.{timestamp}.bak")
    shutil.copy2(db_path, backup_path)
    return backup_path

def get_backup_list(db_path, backup_dir=None):
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(db_path), "backups")
    if not os.path.exists(backup_dir):
        return []
    backups = [f for f in os.listdir(backup_dir) if f.endswith(".bak")]
    backups.sort(key=lambda f: f, reverse=True)
    return backups
