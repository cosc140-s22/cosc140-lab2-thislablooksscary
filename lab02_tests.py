import enum
import unittest

from lab02 import FoodCategory, FoodItem, FoodServing, Meal

class TestLab2(unittest.TestCase):
    def test_food_category(self):
        self.assertTrue(issubclass(FoodCategory, enum.Enum))
        self.assertListEqual(dir(FoodCategory), ['DAIRY', 'FRUIT', 'GRAIN', 'OIL', 'OTHER', 'PROTEIN', 'VEGETABLE', '__class__', '__doc__', '__members__', '__module__'])

    def test_food_item(self):
        self.assertTrue(issubclass(FoodItem, object))
        item1 = FoodItem('tofu', FoodCategory.PROTEIN, 123)
        self.assertEqual(str(item1), 'tofu (FoodCategory.PROTEIN) 123cal/100g')

        with self.assertRaises(AttributeError):
            FoodItem('bad food', FoodCategory.STUFF, 100)

        with self.assertRaises(ValueError):
            FoodItem('bad food', FoodCategory.PROTEIN, 'nothing')

    def test_food_serving(self):
        self.assertTrue(issubclass(FoodServing, object))

        item1 = FoodItem('tofu', FoodCategory.PROTEIN, 123)
        serving1 = FoodServing(item1, 50)
        self.assertIs(serving1.food(), item1)
        self.assertEqual(serving1.amount(), 50)
        self.assertEqual(serving1.calories(), item1.calories_per_100g()//2)

        self.assertEqual(str(serving1), '50g of tofu (FoodCategory.PROTEIN) 123cal/100g')

    def test_meal(self):
        self.assertTrue(issubclass(FoodServing, object))
        meal = Meal()
        meal.addFood(FoodServing(FoodItem('tofu', FoodCategory.PROTEIN, 123), 50))
        meal.addFood(FoodServing(FoodItem('broccoli', FoodCategory.VEGETABLE, 27), 80))
        meal.addFood(FoodServing(FoodItem('noodles', FoodCategory.GRAIN, 348), 70))
        meal.addFood(FoodServing(FoodItem('sticky toffee pudding', FoodCategory.OTHER, 348), 112))
        self.assertEqual(meal.calories(), 714)

        s = '''50g of tofu (FoodCategory.PROTEIN) 123cal/100g
80g of broccoli (FoodCategory.VEGETABLE) 27cal/100g
70g of noodles (FoodCategory.GRAIN) 348cal/100g
112g of sticky toffee pudding (FoodCategory.OTHER) 348cal/100g
'''
        self.assertEqual(str(meal), s)

if __name__ == '__main__':
    unittest.main(verbosity=2)
