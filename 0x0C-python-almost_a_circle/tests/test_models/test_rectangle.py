#!/usr/bin/python2
import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    def test_init(self):
        """Test initializer"""
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_width_setter(self):
        """Test width setter"""
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_width_setter_typeerror(self):
        """Test width setter type error"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.width = '30'

    def test_width_setter_valueerror(self):
        """Test width setter value error"""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.width = -30

    def test_width_getter(self):
        """Test width getter"""
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)

    def test_height_setter(self):
        """Test height setter"""
        r = Rectangle(10, 20)
        r.height = 30
        self.assertEqual(r.height, 30)

    def test_height_setter_typeerror(self):
        """Test height setter type error"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.height = '30'

    def test_height_setter_valueerror(self):
        """Test height setter value error"""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.height = -30

    def test_height_getter(self):
        """Test height getter"""
        r = Rectangle(10, 20)
        self.assertEqual(r.height, 20)

    def test_x_setter(self):
        """Test x setter"""
        r = Rectangle(10, 20, 30, 40)
        r.x = 50
        self.assertEqual(r.x, 50)

    def test_x_setter_typeerror(self):
        """Test x setter type error"""
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(TypeError):
            r.x = '50'

    def test_x_setter_valueerror(self):
        """Test x setter value error"""
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(ValueError):
            r.x = -50

    def test_x_getter(self):
        """Test x getter"""
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.x, 30)

    def test_y_setter(self):
        """Test y setter"""
        r = Rectangle(10, 20, 30, 40)
        r.y = 50
        self.assertEqual(r.y, 50)

    def test_y_setter_typeerror(self):
        """Test y setter type error"""
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(TypeError):
            r.y = '50'

    def test_y_setter_valueerror(self):
        """Test y setter value error"""
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(ValueError):
            r.y = -50

    def test_y_getter(self):
        """Test y getter"""
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.y, 40)

    def test_area(self):
        """Test area"""
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        """Test display"""
        r = Rectangle(2, 2)
        r.display()

    def test_str(self):
        """Test __str__"""
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(str(r), '[Rectangle] (50) 30/40 - 10/20')

    def test_update_args(self):
        """Test update args"""
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (1) 4/5 - 2/3')

    def test_update_kwargs(self):
        """Test update kwargs"""
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(str(r), '[Rectangle] (1) 4/5 - 2/3')

    def test_to_dictionary(self):
        """Test to dictionary"""
        r = Rectangle(10, 20, 30, 40, 50)
        d = {'id': 50, 'width': 10, 'height': 20, 'x': 30, 'y': 40}
        self.assertEqual(r.to_dictionary(), d)


if __name__ == '__main__':
    unittest.main()
