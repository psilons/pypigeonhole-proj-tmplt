# test files start with test_, this is the default for unittest: test_*
# otherwise, we need to specify *_test

# start the package name with test_<original_top_package>.

import unittest

import sample_proj_app.sample_feature as sample_feature


class TestSampleFeature(unittest.TestCase):
    def test_scan_cpu(self):
        sample_feature.scan_cpu()
