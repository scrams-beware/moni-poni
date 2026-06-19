# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: RecipeCost
from dataclasses import dataclass, field
import re
from typing import Optional, List, Dict, Any

@dataclass
class Ingredient:
    name: str
    quantity: float
    unit: str
    price_per_unit: float
    
    @classmethod
    def from_input(cls, raw_name: str, raw_qty: str, raw_unit: str, raw_price: str) -> Optional['Ingredient']:
        try:
            qty = float(raw_qty.strip())
            if qty <= 0: return None
            
            price = float(raw_price.strip().replace(',', '.'))
            if price < 0: return None
            
            unit = raw_unit.strip()
            name = raw_name.strip()
            
            # Simple validation for units (allow common ones)
            valid_units = {'g', 'kg', 'ml', 'l', 'pcs', 'шт'}
            if unit.lower() not in valid_units: return None
            
            return cls(name=name, quantity=qty, unit=unit, price_per_unit=price)
        except ValueError:
            return None

@dataclass
class RecipeIngredient(Ingredient):
    recipe_id: int
    
    def total_price(self) -> float:
        return self.quantity * self.price_per_unit

def validate_recipe_ingredients(raw_data: List[Dict[str, Any]], recipe_id: int) -> List[RecipeIngredient]:
    valid = []
    for item in raw_data:
        ing = Ingredient.from_input(
            name=item.get('name', ''),
            qty=str(item.get('quantity', '')),
            unit=item.get('unit', ''),
            price=str(item.get('price_per_unit', ''))
        )
        if ing:
            valid.append(RecipeIngredient(recipe_id=recipe_id, **ing.__dict__))
    return valid

def calculate_total_cost(ingredients: List[RecipeIngredient]) -> float:
    return sum(i.total_price() for i in ingredients)
