import unittest

class TestCelestialPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = CelestialPlatform(max_weight=100)

    def test_add_orb(self):
        """Test adding orbs and checking gravity."""
        self.assertEqual(self.platform.add_orb(30), 1.3)  # Gravity should increase
        self.assertEqual(self.platform.add_orb(20), 1.5)  # Gravity increases further
        with self.assertRaises(ValueError):
            self.platform.add_orb(60)  # Exceeds max weight

    def test_remove_orb(self):
        """Test removing orbs and checking gravity."""
        self.platform.add_orb(40)
        self.platform.add_orb(30)
        self.assertEqual(self.platform.remove_orb(40), 1.3)  # Gravity recalculated
        with self.assertRaises(ValueError):
            self.platform.remove_orb(50)  # Orb not present on platform

if __name__ == '__main__':
    unittest.main()