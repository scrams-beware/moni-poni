# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: RecipeCost
import datetime

def monthly_stats(self):
    """Расчёт месячной статистики по датам."""
    if not self.entries:
        return {}
    
    stats = {}
    for entry in self.entries:
        date_str = entry.get('date', '')
        if date_str:
            try:
                dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                month_key = f"{dt.year}-{dt.month:02d}"
            except ValueError:
                continue
            
            cost = float(entry.get('total_cost', 0))
            
            if month_key not in stats:
                stats[month_key] = {'cost': 0, 'count': 0}
            
            stats[month_key]['cost'] += cost
            stats[month_key]['count'] += 1
    
    for month in stats:
        stats[month]['avg_cost'] = round(stats[month]['cost'] / stats[month]['count'], 2) if stats[month]['count'] > 0 else 0
    
    return stats

if __name__ == '__main__':
    app = RecipeCostApp()
    
    # Добавление записей с датами
    app.add_entry(
        {'recipe': 'Борщ', 'date': '2024-1-5', 'total_cost': 35.5, 'portions': 4}
    )
    app.add_entry(
        {'recipe': 'Салат', 'date': '2024-1-15', 'total_cost': 22.0, 'portions': 3}
    )
    app.add_entry(
        {'recipe': 'Паста', 'date': '2024-2-3', 'total_cost': 18.75, 'portions': 2}
    )
    
    monthly = app.monthly_stats()
    print("Месячная статистика:")
    for month, data in sorted(monthly.items()):
        print(f"  {month}: средняя стоимость - {data['avg_cost']} руб., записей - {data['count']}")
