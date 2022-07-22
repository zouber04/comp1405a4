import unittest
import a4p as a4
import logging

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
LOG.setLevel(logging.INFO)


class TestA4(unittest.TestCase):

    def setUp(self):
        # Run before each test method
        self.test_input= 'test_input.txt'
        self.test_output = 'test_output.txt'
        self.test_list = [
            ["Ham", "Pig meat", 30, 200],
            ["Cereal", "Milled grains", 10, 400],
            ["Ice cream", "Cold battered cream", 7, 35],
            ["Whipped Cream", "Fluffy beaten milk cream", 12, 44]
        ]
        a4.product_list = []
        self.assertEqual(a4.product_list, [])

    def test_load_inventory(self):
        # not going to assume that it works with floating point
        a4.load_inventory(self.test_input)
        self.assertEqual(a4.product_list, self.test_list)

    def test_save_inventory(self):
        a4.product_list = self.test_list.copy()
        a4.save_inventory(self.test_output)
        a4.load_inventory(self.test_input)
        self.assertEqual(a4.product_list, self.test_list)

    def test_add_product(self):
        a4.product_list = self.test_list.copy()
        expected = self.test_list.copy() + [["Tomato", "Red fruit", 4, 500]]
        a4.add_new_product("Tomato", "Red fruit", 4, 500)
        self.assertEqual(a4.product_list, expected)

    def test_remove_product(self):
        a4.product_list = self.test_list.copy()
        expected = self.test_list.copy()
        expected.remove(["Cereal", "Milled grains", 10, 400])
        
        # Remove existing item
        a4.remove_product("Cereal")
        self.assertEqual(a4.product_list, expected)

        # Remove non-existing item
        a4.remove_product("Burger")
        self.assertEqual(a4.product_list, expected)

    def test_add_product_stock(self):
        a4.product_list = self.test_list.copy()
        expected = self.test_list.copy()
        expected[1][3] += 5     # Add 500 cereal stock
        
        # Add product stock to existing item
        a4.add_product_stock("Cereal", 500)
        self.assertEqual(a4.product_list, expected)

        # Add product stock to non-existing item
        a4.add_product_stock("Burger", 500)
        self.assertEqual(a4.product_list, expected)

    def test_sell_product(self):
        a4.product_list = self.test_list.copy()
        expected = self.test_list.copy()
        
        # Sell valid number of existing product stock
        expected[1][3] -= 399   # Sell 399 cereal stock
        self.assertTrue(a4.sell_product("Cereal", 399))
        self.assertEqual(a4.product_list, expected)

        # Sell invalid number of existing product stock
        self.assertFalse(a4.sell_product("Ice cream", 36))
        self.assertEqual(a4.product_list, expected)

        # Sell non-existing product
        self.assertFalse(a4.sell_product("Burger", 1))
        self.assertEqual(a4.product_list, expected)

    def test_list_products(self):
        a4.product_list = self.test_list.copy()
        
        # Printing all products using * arg
        LOG.info("Printing all products using '*' arg")    
        a4.list_products("*")

        # Printing single product matching keyword in name
        LOG.info("Printing single product matching keyword 'ham' in name")
        a4.list_products("ham")

        # Printing single product matching keyword in description
        LOG.info("Printing single product matching keyword 'grains' in description")
        a4.list_products("grains")

        # Printing multiple products matching specific keyword in name or desc
        LOG.info("Printing multiple products matching keyword 'cream'")
        a4.list_products("cream")

    def test_main(self):
        a4.product_list = self.test_list.copy()

    def tearDown(self):
        # Run after each test method
        a4.product_list = []
        self.assertEqual(a4.product_list, [])

if __name__ == "__main__":
    unittest.main()