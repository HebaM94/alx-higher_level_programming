#!/usr/bin/python3
"""Unittest for rectangle.py

Unittest classes:
    TestRectangle_instantiation - line 22
    TestRectangle_width - line 131
    TestRectangle_height - line 200
    TestRectangle_x - line 269
    TestRectangle_y - line 333
    TestRectangle_order_of_initialization - line 398
    TestRectangle_area - line 421
    TestRectangle_stdout - line 448
    TestRectangle_update - line 537
    TestRectangle_to_dictionary - line 786"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Define unittests for Rectangle class instantiation"""

    def test_rectangle_is_base(self):
        """Test if created Rectangle object is an instance of Base"""
        self.assertIsInstance(Rectangle(10, 5), Base)

    def test_no_args(self):
        """Test no arguments passed to Rectangle class"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test one argument passed to Rectangle class"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test two arguments passed to Rectangle class"""
        rect1 = Rectangle(10, 5)
        rect2 = Rectangle(8, 4)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_three_args(self):
        """Test three arguments passed to Rectangle class"""
        rect1 = Rectangle(10, 5, 5)
        rect2 = Rectangle(8, 4, 4)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_four_args(self):
        """Test four arguments passed to Rectangle class"""
        rect1 = Rectangle(10, 5, 5, 4)
        rect2 = Rectangle(8, 4, 4, 5)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_five_args(self):
        """Test five arguments passed to Rectangle class"""
        self.assertEqual(9, Rectangle(10, 5, 5, 4, 9).id)

    def test_more_than_five_args(self):
        """Test more than five arguments passed to Rectangle class"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 5, 4, 9, 1)

    def test_width_private(self):
        """Test if width attribute is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 5, 4, 9).__width)

    def test_height_private(self):
        """Test if height attribute is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 5, 4, 9).__height)

    def test_x_private(self):
        """Test x coordinate attribute is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 5, 4, 9).__x)

    def test_y_private(self):
        """Test y coordinate attribute is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 5, 4, 9).__y)

    def test_width_getter(self):
        """Test the getter method for width attribute"""
        rect = Rectangle(10, 5, 5, 4, 9)
        self.assertEqual(10, rect.width)

    def test_width_setter(self):
        """Test the setter method for width attribute"""
        rect = Rectangle(8, 5, 5, 4, 9)
        rect.width = 10
        self.assertEqual(10, rect.width)

    def test_height_getter(self):
        """Test the getter method of the height attribute"""
        rect = Rectangle(10, 5, 5, 4, 9)
        self.assertEqual(5, rect.height)

    def test_height_setter(self):
        """Test the setter method of the height attribute"""
        rect = Rectangle(10, 6, 5, 4, 9)
        rect.height = 10
        self.assertEqual(10, rect.height)

    def test_x_getter(self):
        """Test the getter method of the x-coordinate attribute"""
        rect = Rectangle(10, 5, 5, 4, 9)
        self.assertEqual(5, rect.x)

    def test_x_setter(self):
        """Test the setter method of the x-coordinate attribute"""
        rect = Rectangle(10, 5, 6, 4, 9)
        rect.x = 5
        self.assertEqual(5, rect.x)

    def test_y_getter(self):
        """Test the getter method of the y-coordinate attribute"""
        rect = Rectangle(10, 5, 5, 4, 9)
        self.assertEqual(4, rect.y)

    def test_y_setter(self):
        """Test the setter method of the y-coordinate attribute"""
        rect = Rectangle(10, 5, 5, 6, 9)
        rect.y = 4
        self.assertEqual(4, rect.y)


class TestRectangle_width(unittest.TestCase):
    """Define unittests for rectangle class width getter/setter"""

    def test_None_width(self):
        """Test None as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)

    def test_str_width(self):
        """Test a string as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("ten", 5)

    def test_float_width(self):
        """Test float number as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.5, 5)

    def test_bool_width(self):
        """Test boolean value as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 5)

    def test_list_width(self):
        """Test list as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([8, 9, 10], 5)

    def test_dict_width(self):
        """Test dictionary as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 9, "b": 10}, 5)

    def test_set_width(self):
        """Test set as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({8, 9, 10}, 5)

    def test_tuple_width(self):
        """Test tuple as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((8, 9, 10), 5)

    def test_range_width(self):
        """Test range object as argument for width attribute"""""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(10), 5)

    def test_inf_width(self):
        """Test infinity as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5)

    def test_nan_width(self):
        """Test NaN as argument for width attribute"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('NaN'), 5)

    def test_negative_width(self):
        """Test negative number as argument for width attribute"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 5)

    def test_zero_width(self):
        """Test zero as argument for width attribute"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)


class TestRectangle_height(unittest.TestCase):
    """Define unittests for rectangle class height getter/setter"""

    def test_None_height(self):
        """Test None value as an argumment to height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_str_height(self):
        """Test a string as argument for height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "five")

    def test_float_height(self):
        """Test float value as argument for height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 5.5)

    def test_bool_width(self):
        """Test boolean value as argument for height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, False)

    def test_list_height(self):
        """Test list value as argument for height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [3, 4, 5])

    def test_dict_height(self):
        """Test dict value as argument for height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {"c": 4, "d": 5})

    def test_set_height(self):
        """Test set as argument for height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {3, 4, 5})

    def test_tuple_height(self):
        """Test tuple as argument for height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, (3, 4, 5))

    def test_range_height(self):
        """Test range object as argument for height attribute"""""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, range(5))

    def test_inf_height(self):
        """Test infinity as argument for height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('inf'))

    def test_nan_height(self):
        """Test NaN as argument for height attribute"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('NaN'))

    def test_negative_height(self):
        """Test negative number as argument for height attribute"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -5)

    def test_zero_height(self):
        """Test zero as argument for height attribute"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)


class TestRectangle_x(unittest.TestCase):
    """Define unittests for rectangle class x getter/setter"""

    def test_None_x(self):
        """Test None value as an argumment to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, None)

    def test_str_x(self):
        """Test string value as an argumment to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, "five")

    def test_float_x(self):
        """Test floating point number as an argumment to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, 5.5)

    def test_bool_x(self):
        """Test boolean value as an argument to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, True)

    def test_dict_x(self):
        """Test dictionary as an argument to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, {"a": 5, "b": 4})

    def test_list_x(self):
        """Test list as an argument to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, [5, 4, 3])

    def test_set_x(self):
        """Test set as an argument to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, {5, 4, 3})

    def test_tuple_x(self):
        """Test tuple as an argument to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, (5, 4, 3))

    def test_range_x(self):
        """Test range object as an argument to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, range(5))

    def test_inf_x(self):
        """Test infinity as an argument to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, float('inf'))

    def test_nan_x(self):
        """Test NaN as an argument to x attribute"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, float('NaN'))

    def test_negative_x(self):
        """Test a negative number as an argument to x attribute"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 5, -5)


class TestRectangle_y(unittest.TestCase):
    """Define unittests for rectangle class y getter/setter"""


    def test_None_y(self):
        """Test None value as an argumment to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, None)

    def test_str_y(self):
        """Test string value as an argumment to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, "four")

    def test_float_y(self):
        """Test floating point number as an argumment to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, 4.5)

    def test_bool_y(self):
        """Test boolean value as an argument to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, True)

    def test_dict_y(self):
        """Test dictionary as an argument to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, {"a": 5, "b": 4})

    def test_list_y(self):
        """Test list as an argument to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, [5, 4, 3])

    def test_set_y(self):
        """Test set as an argument to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, {5, 4, 3})

    def test_tuple_y(self):
        """Test tuple as an argument to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, (5, 4, 3))

    def test_range_y(self):
        """Test range object as an argument to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, range(4))

    def test_inf_y(self):
        """Test infinity as an argument to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, float('inf'))

    def test_nan_y(self):
        """Test NaN as an argument to y attribute"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 5, float('NaN'))

    def test_negative_y(self):
        """Test a negative number as an argument to y attribute"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 5, 5, -4)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Define unittests for order"""


    def test_width_first(self):
        """Test initializing width before next arguments"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", "height")
            Rectangle("width", 5, "x")
            Rectangle("width", 5, 5, "y")

    def test_height_after_width(self):
        """Test initializing height after width and before next args"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "height", "x")
            Rectangle(10, "height", 5, "y")         

    def test_x_before_y(self):
        """Test initializing x before y"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 5, "x", "y")


class TestRectangle_area(unittest.TestCase):
    """Define unittests for area method of rectangle class"""

    def test_area_small(self):
        """Test the area of a small rectangle"""
        rect = Rectangle(10, 5, 0, 0, 0)
        self.assertEqual(50, rect.area())

    def test_area_large(self):
        """Test the area of a large rectangle"""
        rect = Rectangle(999999999999999, 999999999999999999)
        self.assertEqual(999999999999998999000000000000001, rect.area())

    def test_area_changed_attributes(self):
        """Test area after changing attributes"""
        rect = Rectangle(8, 4)
        rect.width = 10
        rect.height = 5
        self.assertEqual(50, rect.area())

    def test_area_one_arg(self):
        """Test if one argument is given to area()"""
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.area(10)


class TestRectangle_stdout(unittest.TestCase):
    """Defines unittests for testing __str__ and display methods
    of Rectangle class"""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout

        Args:
            rect (Rectangle): The Rectangle to be printed to stdout
            method (str): The method to run on rect

        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return (capture)

    def test_str_method_print_width_height(self):
        """Tests that print(rect) prints width and height"""
        rect = Rectangle(10, 5)
        capture = TestRectangle_stdout.capture_stdout(rect, "print")
        correct = "[Rectangle] ({}) 0/0 - 10/5\n".format(rect.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        """Tests that __str__() prints width, height, and x"""
        rect = Rectangle(10, 5, 5)
        correct = "[Rectangle] ({}) 5/0 - 10/5".format(rect.id)
        self.assertEqual(correct, rect.__str__())

    def test_str_method_width_height_x_y(self):
        """Tests that str(rect) prints width, height, x, y, id"""
        rect = Rectangle(10, 5, 5, 4, 9)
        correct = "[Rectangle] ({}) 5/4 - 10/5".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_str_method_changed_attributes(self):
        """Tests str(rect) after changing attributes of rect"""
        rect = Rectangle(5, 6, 3, 2, [9])
        rect.width = 10
        rect.height = 5
        rect.x = 5
        rect.y = 4
        self.assertEqual("[Rectangle] ([9]) 5/4 - 10/5", str(rect))

    def test_str_method_one_arg(self):
        """Tests str(rect), where only one argument is provided"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaises(TypeError):
            rect.__str__(10)

    def test_display_width_height(self):
        """Tests display method for width and height"""
        rect = Rectangle(1, 3)
        capture = TestRectangle_stdout.capture_stdout(rect, "display")
        self.assertEqual("#\n#\n#\n", capture.getvalue())

    def test_display_width_height_x(self):
        """Tests display method for width, height, and x"""
        rect = Rectangle(1, 3, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(rect, "display")
        self.assertEqual(" #\n #\n #\n", capture.getvalue())

    def test_display_width_height_y(self):
        """Tests display method for width, height, and y"""
        rect = Rectangle(1, 3, 0, 1, 1)
        capture = TestRectangle_stdout.capture_stdout(rect, "display")
        self.assertEqual("\n#\n#\n#\n", capture.getvalue())

    def test_display_width_height_x_y(self):
        """Tests display method for all arguments"""
        rect = Rectangle(1, 3, 1, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(rect, "display")
        self.assertEqual("\n #\n #\n #\n", capture.getvalue())

    def test_display_one_arg(self):
        """Tests display method when given an incorrect number of args"""
        rect = Rectangle(1, 3, 0, 1, 1)
        with self.assertRaises(TypeError):
            rect.display(1)


class TestRectangle_update(unittest.TestCase):
    """Defines unittests for testing update method
    of the Rectangle class"""

    def test_update_args_zero(self):
        """Tests update method when no args are provided"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update()
        self.assertEqual("[Rectangle] (9) 5/4 - 10/5", str(rect))

    def test_update_args_one(self):
        """Tests update method when only one arg is provided"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(6)
        self.assertEqual("[Rectangle] (6) 5/4 - 10/5", str(rect))

    def test_update_args_two(self):
        """Tests update method when two args are provided"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(6, 8)
        self.assertEqual("[Rectangle] (6) 5/4 - 8/5", str(rect))

    def test_update_args_three(self):
        """Tests update method when three args are provided"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(6, 8, 4)
        self.assertEqual("[Rectangle] (6) 5/4 - 8/4", str(rect))

    def test_update_args_four(self):
        """Tests update method when four args are provided"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(6, 8, 4, 4)
        self.assertEqual("[Rectangle] (6) 4/4 - 8/4", str(rect))

    def test_update_args_five(self):
        """Tests update method when five args are provided"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(6, 8, 4, 4, 3)
        self.assertEqual("[Rectangle] (6) 4/3 - 8/4", str(rect))

    def test_update_args_more_than_five(self):
        """Tests update method with more than five args"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(6, 8, 4, 4, 3, 2)
        self.assertEqual("[Rectangle] (6) 4/3 - 8/4", str(rect))

    def test_update_args_None_id(self):
        """Tests update method when None passed as an argument"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(None)
        correct = "[Rectangle] ({}) 5/4 - 10/5".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_update_args_None_id_and_more(self):
        """Tests update method when None is passed for id"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(None, 8, 4, 4)
        correct = "[Rectangle] ({}) 4/4 - 8/4".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_update_args_invalid_width_type(self):
        """Tests update method when str passed for width"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(6, "width")

    def test_update_args_width_zero(self):
        """Tests update method when 0 passed for width"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(6, 0)

    def test_update_args_width_negative(self):
        """Tests update method when -ve number passed for width"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(6, -10)

    def test_update_args_invalid_height_type(self):
        """Tests update method when str passed for height"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(6, 8, "height")

    def test_update_args_height_zero(self):
        """Tests update method when 0 passed for height"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(6, 8, 0)

    def test_update_args_height_negative(self):
        """Tests update method when -ve number passed for height"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(6, 8, -4)

    def test_update_args_invalid_x_type(self):
        """Tests update method when str passed for x"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(6, 8, 4, "x")

    def test_update_args_x_negative(self):
        """Tests update method when -ve number passed for x"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.update(6, 8, 4, -4)

    def test_update_args_invalid_y_type(self):
        """Tests update method when str passed for y"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(6, 8, 4, 4, "y")

    def test_update_args_y_negative(self):
        """Tests update method when -ve number passed for y"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(6, 8, 4, 4, -3)

    def test_update_args_width_first(self):
        """Tests invalid values of width parameter before others"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(6, "width", "height")  

    def test_update_args_height_second(self):
        """Tests invalid values of height parameter before x and y"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(6, 8, "height", "x")
            rect.update(6, 8, "height", 4, "y")

    def test_update_args_x_before_y(self):
        """Tests x value before y"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(6, 8, 4, "x", "y")

    def test_update_kwargs_one(self):
        """Test that one argument can be set using keyword arguments."""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(id=6)
        self.assertEqual("[Rectangle] (6) 5/4 - 10/5", str(rect))

    def test_update_kwargs_two(self):
        """Test two arguments can be set using keyword arguments."""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(width=8, id=6)
        self.assertEqual("[Rectangle] (6) 5/4 - 8/5", str(rect))

    def test_update_kwargs_three(self):
        """Tests three arguments can be set using keyword arguments"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(width=8, height=4, id=6)
        self.assertEqual("[Rectangle] (6) 5/4 - 8/4", str(rect))

    def test_update_kwargs_four(self):
        """Tests four arguments can be set using keyword arguments"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(id=6, x=4, height=4, width=8)
        self.assertEqual("[Rectangle] (6) 4/4 - 8/4", str(rect))

    def test_update_kwargs_five(self):
        """Tests five arguments passed using keyword arguments"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(y=3, x=4, id=6, width=8, height=4)
        self.assertEqual("[Rectangle] (6) 4/3 - 8/4", str(rect))

    def test_update_kwargs_None_id(self):
        """Ensures None is a valid input for the 'id' parameter"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(id=None)
        correct = "[Rectangle] ({}) 5/4 - 10/5".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_update_kwargs_invalid_width_type(self):
        """Checks TypeError raised when invalid type used for 'width'"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(width="width")

    def test_update_kwargs_width_zero(self):
        """Checks that zero is not allowed as a value for `width`"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(width=0)

    def test_update_kwargs_width_negative(self):
        """Checks ValueError raised if negative number given for `width`"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(width=-8)

    def test_update_kwargs_invalid_height_type(self):
        """Checks TypeError raised when invalid type used for `height`"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(height="height")

    def test_update_kwargs_height_zero(self):
        """Checks that zero is not allowed as a value for `height`"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(height=0)

    def test_update_kwargs_height_negative(self):
        """Checks ValueError raised if negative number given for `height`"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(height=-4)

    def test_update_kwargs_inavlid_x_type(self):
        """Checks TypeError raised when invalid type used for x-coordinate"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(x="x")

    def test_update_kwargs_x_negative(self):
        """Checks ValueError raised if negative number given for x-coordinate"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.update(x=-4)

    def test_update_kwargs_invalid_y_type(self):
        """Checks TypeError raised by y-coordinate type error"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(y="y")

    def test_update_kwargs_y_negative(self):
        """Checks ValueError raised if y-coordinate is negative"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(y=-3)

    def test_update_args_and_kwargs(self):
        """Checks mixed args and kwargs in update() method"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(6, 8, height=4, y=3)
        self.assertEqual("[Rectangle] (6) 5/4 - 8/5", str(rect))

    def test_update_kwargs_some_wrong_keys(self):
        """Tests wrong key passed for kwargs"""
        rect = Rectangle(10, 5, 5, 4, 9)
        rect.update(height=4, id=6, a=1, b=54, x=4, y=3)
        self.assertEqual("[Rectangle] (6) 4/3 - 10/4", str(rect))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Defines unittests for testing to_dictionary method
    of the Rectangle class"""

    def test_to_dictionary_output(self):
        """Checks output format of dictionary returned from to_dictionary()"""
        rect = Rectangle(10, 5, 5, 4, 9)
        correct = {'id': 9, 'width': 10, 'height': 5, 'x': 5, 'y': 4}
        self.assertDictEqual(correct, rect.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """Checks that calling to_dictionary does not modify object"""
        rect1 = Rectangle(10, 5, 5, 4, 9)
        rect2 = Rectangle(5, 9, 1, 2, 10)
        rect2.update(**rect1.to_dictionary())
        self.assertNotEqual(rect1, rect2)

    def test_to_dictionary_arg(self):
        """Checks TypeError raised when argument provided to to_dictionary()"""
        rect = Rectangle(10, 5, 5, 4, 9)
        with self.assertRaises(TypeError):
            rect.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
