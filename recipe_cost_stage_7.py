# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: RecipeCost
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def get_sort_key(r):
        val = r.get(key)
        if isinstance(val, str):
            try: int(val); return (0, val)
            except ValueError: return (1, val.lower())
        elif key == 'priority':
            p = int(float(val))
            return (-p, 0)
        else: return (0, val or '')
    sorted_records = sorted(records, key=get_sort_key, reverse=reverse)
    for i in range(len(sorted_records)):
        r = sorted_records[i]
        if 'date' not in r and 'created_at' in r:
            r['date'] = r.pop('created_at')
    return sorted_records
