import unittest
import code as c

"""
code.py has 5 methods namely:
(1) get_stock_info
(2) get_stock_price
(3) update_stock_price
(4) exec_multi_query
(5) exec_user_script

All methods are vulnerable!

Here we show an exploit against (2) get_stock_price which is applicable to methods (1) and (3) as well.
We believe that methods (4) and (5) shouldn't exist at all in the code. Have a look on solution.py for the why.
"""

class TestDatabase(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
