```python
import unittest
from email_creator.name_generator import generate_name

class TestNameGenerator(unittest.TestCase):

    def test_generate_name(self):
        """Test if the generate_name function produces a non-empty string."""
        name = generate_name()
        self.assertIsInstance(name, str)
        self.assertTrue(len(name) > 0)

    def test_generate_name_uniqueness(self):
        """Test if the generate_name function produces unique names on subsequent calls."""
        name_set = set()
        for _ in range(100):
            name = generate_name()
            self.assertNotIn(name, name_set)
            name_set.add(name)

    def test_generate_name_format(self):
        """Test if the generated name follows the expected format (e.g., no numbers, special characters)."""
        for _ in range(10):
            name = generate_name()
            self.assertRegex(name, r'^[A-Za-z]+$', "Generated name contains invalid characters")

if __name__ == '__main__':
    unittest.main()
```