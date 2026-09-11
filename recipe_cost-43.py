# === Stage 43: Добавь пагинацию длинных списков ===
# Project: RecipeCost
def paginate(items, page_size=10):
    """Return (current_page, total_pages, items_on_page) for 1-based pagination."""
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    current = items[(page_size * (total_pages - 1)):(page_size * total_pages)]
    return current, total_pages, page_size
