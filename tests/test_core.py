import unittest
import numpy as np
from mwdgt import MaheshWindDataGettingThing

class TestMaheshWindDataGettingThing(unittest.TestCase):

    def setUp(self):
        self.m = MaheshWindDataGettingThing(
            start_date='2019-12-19',
            end_date='2019-12-31',
            data_dir=r'C:\Downloads\Dissertation\New folder\Wind data'
        )

    def test_initialization(self):
        self.assertIsNotNone(self.m.start_date)
        self.assertIsNotNone(self.m.end_date)
        self.assertIsNotNone(self.m.data_dir)

    def test_getWind_shape(self):
        # Example: 3 locations [lon, lat]
        locations = np.array([
            [145.0, -36.5],
            [146.0, -37.0],
            [144.5, -35.5]
        ])
        u, v = self.m.getWind(locations)
        self.assertEqual(u.shape, (3,))
        self.assertEqual(v.shape, (3,))
        self.assertTrue(np.all(np.isfinite(u)))
        self.assertTrue(np.all(np.isfinite(v)))

if __name__ == '__main__':
    unittest.main()
