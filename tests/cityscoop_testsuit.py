import unittest
from tests.cityscoop_login import cityscoop_login
from tests.cityscoop_search import cityscoop_search



login = unittest.TestLoader().loadTestsFromTestCase(cityscoop_login)
search = unittest.TestLoader().loadTestsFromTestCase(cityscoop_search)



test_suite = unittest.TestSuite(
    [login, search])

unittest.TextTestRunner().run(test_suite)
