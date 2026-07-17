# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: RecipeCost
def archive_completed_records(records, cutoff_date=None):
    """Archive records that are completed or older than the given date."""
    if not records:
        return []
    
    archived = []
    remaining = []
    
    for record in records:
        status = record.get('status', 'active')
        created_at = record.get('created_at', '')
        
        is_completed = (status == 'completed' or status == 'finished')
        is_old = cutoff_date and created_at and created_at < cutoff_date
        
        if is_completed or is_old:
            archived.append(record)
        else:
            remaining.append(record)
    
    return remaining, archived
