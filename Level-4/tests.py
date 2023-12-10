import unittest
import code as c

class TestDatabase(unittest.TestCase):

    # tests for correct retrieval of stock info given a symbol
    def test_1(self):
        op = c.DB_CRUD_ops()
        expected_output = "[RESULT] ('2022-01-06', 'MSFT', 300.0)"
        actual_output = op.get_stock_info('MSFT')
        self.assertEqual(actual_output, expected_output)

    # tests for correct retrieval of stock price
    def test_3(self):
        op = c.DB_CRUD_ops()
        expected_output = "[RESULT] (300.0,)\n"
        actual_output = op.get_stock_price('MSFT')
        self.assertEqual(actual_output, expected_output)

    # tests for correct update of stock price given symbol and updated price
    def test_4(self):
        op = c.DB_CRUD_ops()
        expected_output = ""
        actual_output = op.update_stock_price('MSFT', 300.0)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
