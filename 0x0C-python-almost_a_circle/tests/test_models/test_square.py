#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    def test_init(self):
        """Test initializer"""
        s = Square(10, 30, 40, 50)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)
        self.assertEqual(s.id, 50)

    def test_size_setter(self):
        """Test size setter"""
        s = Square(10)
        s.size = 20
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)

    def test_size_setter_typeerror(self):
        """Test size setter type error"""
        s = Square(10)
        with self.assertRaises(TypeError):
            s.size = '20'

    def test_size_setter_valueerror(self):
        """Test size setter value error"""
        s = Square(10)
        with self.assertRaises(ValueError):
            s.size = -20

    def test_size_getter(self):
        """Test size getter"""
        s = Square(10)
        self.assertEqual(s.size, 10)

    def test_str(self):
        """Test str"""
        s = Square(10, 20, 30, 40)
        self.assertEqual(str(s), '[Square] (40) 20/30 - 10')

    def test_update_args(self):
        """Test update args"""
        s = Square(10, 20, 30, 40)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (1) 3/4 - 2')

    def test_size_typeerror(self):
        """Test non-ints for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")

    def test_wsize_typeerror(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(10.5)

    def test_hsize_valueerror(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-2)

    def test_x_typeerror(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")

    def test_y_typeerror(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "hello")

    def test_size_valueerror(self):
        """Test ints <= 0 for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_update_kwargs(self):
        """Test update kwargs"""
        s = Square(10, 20, 30, 40)
        s.update(id=1, size=2, x=3, y=4)
        self.assertEqual(str(s), '[Square] (1) 3/4 - 2')

    def test_to_dictionary(self):
        """Test to dictionary"""
        s = Square(10, 20, 30, 40)
        d = {'id': 40, 'size': 10, 'x': 20, 'y': 30}
        self.assertEqual(s.to_dictionary(), d)

    def test_init_with_nagative_size(self):
        """Test initialization with negative size"""
        with self.assertRaises(ValueError):
            Square(-10)

    def test_update_with_nagative_size(self):
        """Test update with negative size"""
        s = Square(10)
        with self.assertRaises(ValueError):
            s.update(size=-20)

    def test_str_with_zero_id(self):
        """Test string representation with id=0"""
        s = Square(10, 20, 30, 0)
        self.assertEqual(str(s), '[Square] (0) 20/30 - 10')

    def test_size_setter_with_invalid_type(self):
        """Test size setter with invalid type"""
        s = Square(10)
        with self.assertRaises(TypeError):
            s.size = 'invalid'

    def test_to_dictionary_with_not_none_id(self):
        """Test to dictionary with not None id"""
        s = Square(10, 20, 30, 40)
        d = s.to_dictionary()
        self.assertTrue(isinstance(d['id'], int))

    def test_to_dictionary_with_none_id(self):
        """Test to dictionary with None id"""
        s = Square(10, 20, 30)
        d = s.to_dictionary()
        self.assertTrue(isinstance(d['id'], int))

    def test_multiple_updates(self):
        """Test multiple updates"""
        s = Square(10)
        s.update(1)
        s.update(2)
        self.assertEqual(s.id, 2)

    def test_multiple_updates_with_kwargs(self):
        """Test multiple updates with kwargs"""
        s = Square(10)
        s.update(id=1, size=20)
        s.update(size=30)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 30)


if __name__ == '__main__':
    unittest.main()
