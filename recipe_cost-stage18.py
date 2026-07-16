# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: RecipeCost
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag('{self.name}')"


def add_tag(recipe, tag_name):
    """Добавить тег к рецепту. Возвращает True если успешно."""
    if not recipe.tags:
        recipe.tags = []
    for t in recipe.tags:
        if t.name == tag_name:
            return False
    recipe.tags.append(Tag(tag_name))
    return True


def remove_tag(recipe, tag_name):
    """Удалить тег из рецепта. Возвращает True если удалён."""
    if not recipe.tags:
        return False
    for i, t in enumerate(recipe.tags):
        if t.name == tag_name:
            del recipe.tags[i]
            return True
    return False


def get_tag_names(recipe):
    """Возвращает список имён тегов рецепта."""
    return [t.name for t in (recipe.tags or [])]
