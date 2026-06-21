# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: RecipeCost
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in ['id', 'created_at']:
            continue
        records[record_id][key] = value
    
    updated_count += 1
    print(f"Запись #{record_id} обновлена успешно. Изменено: {updates}")
    return True

def delete_record(record_id):
    if record_id in records:
        del records[record_id]
        deleted_count += 1
        print(f"Запись #{record_id} удалена.")
        return True
    else:
        print(f"Ошибка: запись с ID {record_id} не найдена для удаления.")
        return False
