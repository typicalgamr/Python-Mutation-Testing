import unittest
from inventory import Product, PerishableProduct

class TestProduct(unittest.TestCase):
    def test_add_stock(self):
        product = Product("Laptop", 1000, 10)
        product.add_stock(5)
        self.assertEqual(product.quantity, 15)

    def test_remove_stock(self):
        product = Product("Laptop", 1000, 10)
        product.remove_stock(3)
        self.assertEqual(product.quantity, 7)

    def test_remove_stock_insufficient(self):
        product = Product("Laptop", 1000, 2)
        with self.assertRaises(ValueError):
            product.remove_stock(5)

    def test_get_stock_value(self):
        product = Product("Laptop", 1000, 10)
        self.assertEqual(product.get_stock_value(), 10000)

class TestPerishableProduct(unittest.TestCase):
    def test_is_expired(self):
        perishable = PerishableProduct("Milk", 3, 50, "2023-10-01")
        self.assertTrue(perishable.is_expired("2023-10-02"))
        self.assertFalse(perishable.is_expired("2023-09-30"))

if __name__ == '__main__':
    unittest.main()
