import unittest 
from café_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    def test_get_price_existing_item():
        menu = CoffeeMenu.get_price("espresso")

    def test_get_price_non_existing_item():
        menu = CoffeeMenu.get_price('Pokemocha')


    def test_add_item(self):
        menu = CoffeeMenu.add_item("mocha", 3.50)
        self.assertEqual(menu["mocha"], 3.50)

if __name__ == "__main__":
    unittest.main()