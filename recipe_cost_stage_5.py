# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: RecipeCost
def delete_record(table_name, record_id):
    """Удаление записи по ID с безопасной обработкой отсутствия."""
    if not table_name or not record_id:
        raise ValueError("Идентификаторы таблицы и записи не могут быть пустыми.")
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Проверка существования ID перед удалением для мягкого поведения или логирования
        cursor.execute(f"SELECT 1 FROM {table_name} WHERE id = ?", (record_id,))
        if not cursor.fetchone():
            print(f"[INFO] Запись с ID {record_id} в таблице '{table_name}' не найдена. Удаление пропущено.")
            conn.close()
            return False
        
        # Выполнение удаления
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (record_id,))
        if cursor.rowcount > 0:
            print(f"[SUCCESS] Запись с ID {record_id} успешно удалена из '{table_name}'.")
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"[ERROR] Ошибка при работе с базой данных: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()
    
    return True
