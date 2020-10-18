# test files start with test_, this is the default for unittest: test_*
# otherwise, we need to specify *_test

# start the package name with test_<original_top_package>.

import unittest

import sample_proj_cmpl.my_app as my_app


class TestSampleFeature(unittest.TestCase):
    def test_scan_cpu(self):
        my_app.scan_cpu()
