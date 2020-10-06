# Top package has to be unique too, and in general it should be
# test_<src package>. The test_* pattern is the unit test runner's default.
# If we follow defautls, we could avoid configurations.

import unittest
import global_unique_name_package.dummy_src as ds


class DummyTest(unittest.TestCase):
    def test_calc(self):
        c = ds.calc(5, 10)
        self.assertTrue(c == 35)
