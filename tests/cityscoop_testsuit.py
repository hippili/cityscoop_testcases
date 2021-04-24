import unittest
from tests.cityscoop_login import cityscoop_login
from tests.cityscoop_search import cityscoop_search
from tests.cityscoop_profile import cityscoop_profile
from tests.cityscoop_about import cityscoop_about



login = unittest.TestLoader().loadTestsFromTestCase(cityscoop_login)
search = unittest.TestLoader().loadTestsFromTestCase(cityscoop_search)
profile = unittest.TestLoader().loadTestsFromTestCase(cityscoop_profile)
about = unittest.TestLoader().loadTestsFromTestCase(cityscoop_about)



test_suite = unittest.TestSuite(
     [login, search, profile, about])

unittest.TextTestRunner().run(test_suite)
