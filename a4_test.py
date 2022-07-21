import unittest
import a4p as a4

def clear_product_list():
    a4.product_list = []

product_list = [
            ['Beans', 'High in protein', 20, 500],
            ['Corn', 'Yellow veggie', 15, 140]
]
class TestA4(unittest.TestCase):

    def setUp(self):
        # Run before each test method
        self.test_input= 'test_input.txt'
        self.test_output = 'test_output.txt'
        self.test_list = [
            ["Ham", "Pig meat", 30, 200],
            ["Cereal", "Milled grains", 10, 400],
            ["Ice cream", "Cold battered cream", 7, 35]
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
        pass

    def tearDown(self):
        # Run after each test method
        a4.product_list = []
        self.assertEqual(a4.product_list, [])

if __name__ == "__main__":
    unittest.main()