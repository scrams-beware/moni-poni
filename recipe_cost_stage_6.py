# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: RecipeCost
class RecipeFilter:
    def __init__(self, recipes):
        self.recipes = recipes
    
    def filter_by_status(self, status):
        return [r for r in self.recipes if r.get('status') == status]
    
    def filter_by_category(self, category):
        return [r for r in self.recipes if r.get('category') == category]
    
    def filter_by_tags(self, tags):
        if not tags:
            return self.recipes
        filtered = []
        for recipe in self.recipes:
            recipe_tags = set(recipe.get('tags', []))
            if any(tag in recipe_tags for tag in tags):
                filtered.append(recipe)
        return filtered
    
    def filter_combined(self, status=None, category=None, tags=None):
        result = self.recipes
        if status:
            result = [r for r in result if r.get('status') == status]
        if category:
            result = [r for r in result if r.get('category') == category]
        if tags:
            result = self.filter_by_tags(tags)
        return result
