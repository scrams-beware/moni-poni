# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: RecipeCost
import unittest

class TestRecipeCost(unittest.TestCase):
    def setUp(self):
        self.receipt = type('Receipt', (), {
            'ingredients': [
                type('Ingredient', (), {'name': 'flour', 'quantity': 2.0, 'price': 10.0, 'unit': 'kg'})(),
                type('Ingredient', (), {'name': 'sugar', 'quantity': 0.5, 'price': 20.0, 'unit': 'kg'})(),
                type('Ingredient', (), {'name': 'butter', 'quantity': 0.2, 'price': 100.0, 'unit': 'kg'})(),
            ],
            'portions': 4,
            'name': 'Test Cake',
        })()

    def test_total_cost(self):
        self.assertEqual(self.receipt.total_cost(), 70.0)

    def test_per_portion_cost(self):
        self.assertAlmostEqual(self.receipt.per_portion_cost(), 17.5)

    def test_cost_per_ingredient(self):
        costs = self.receipt.cost_per_ingredient()
        self.assertEqual(costs['flour'], 20.0)
        self.assertEqual(costs['sugar'], 10.0)
        self.assertEqual(costs['butter'], 20.0)

    def test_total_cost_empty(self):
        empty = type('Receipt', (), {
            'ingredients': [],
            'portions': 1,
        })()
        self.assertEqual(empty.total_cost(), 0.0)

    def test_cost_per_ingredient_empty(self):
        empty = type('Receipt', (), {
            'ingredients': [],
            'portions': 1,
        })()
        self.assertEqual(empty.cost_per_ingredient(), {})

    def test_per_portion_cost_empty(self):
        empty = type('Receipt', (), {
            'ingredients': [],
            'portions': 0,
        })()
        self.assertTrue(math.isinf(empty.per_portion_cost()))

if __name__ == '__main__':
    unittest.main()
