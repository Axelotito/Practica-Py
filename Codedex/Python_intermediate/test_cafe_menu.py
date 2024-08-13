import unittest
from cafe_menu import CoffeeMenu  # Asegúrate de que el nombre del archivo sea correcto

class TestCoffeeMenu(unittest.TestCase):

    def setUp(self):
        self.cafe = CoffeeMenu()

    def test_get_price_existing_item(self):
        # Test para obtener el precio de un ítem existente
        price = self.cafe.get_price('latte')  # Usa minúsculas para 'latte'
        self.assertEqual(price, 2.75)

    def test_get_price_non_existing_item(self):
        # Test para un ítem que no existe en el menú
        price = self.cafe.get_price('Pokemocha')
        self.assertIsNone(price)

    def test_add_item(self):
        # Test para añadir un nuevo ítem y verificar su precio
        self.cafe.add_item("mocha", 3.50)
        price = self.cafe.get_price("mocha")
        self.assertEqual(price, 3.50)

if __name__ == '__main__':
    unittest.main()