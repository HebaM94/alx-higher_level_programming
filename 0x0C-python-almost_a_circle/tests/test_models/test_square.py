#!/usr/bin/python3
"""Unittest for square.py


Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 102
    TestSquare_x - line 171
    TestSquare_y - line 235
    TestSquare_order_of_initialization - line 299
    TestSquare_area - line 314
    TestSquare_stdout - line 339
    TestSquare_update - line 431
    TestSquare_to_dictionary - line 642"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Defines unittests for testing instantiation of the Square class"""

    def test_is_base(self):
        """Test if created Square object is an instance of Base"""
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        """Test if created Square object is also a Rectangle"""
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_args(self):
        """Tests if Square can be initialized without any arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Tests only one argument"""
        sq1 = Square(10)
        sq2 = Square(5)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_two_args(self):
        """Tests two arguments"""
        sq1 = Square(10, 5)
        sq2 = Square(8, 4)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_three_args(self):
        """Tests 3 arguments"""
        sq1 = Square(10, 5, 4)
        sq2 = Square(8, 4, 3)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_four_args(self):
        """Tests 4 arguments"""
        self.assertEqual(9, Square(10, 5, 4, 9).id)

    def test_more_than_four_args(self):
        """Tests if more than 4 arguments are passed"""
        with self.assertRaises(TypeError):
            Square(10, 5, 4, 9, 5)

    def test_size_private(self):
        """Tests the '_size' is private '"""
        with self.assertRaises(AttributeError):
            print(Square(10, 5, 4, 9).__size)

    def test_size_getter(self):
        """Tests size getter method"""
        self.assertEqual(10, Square(10, 5, 4, 9).size)

    def test_size_setter(self):
        """Tests size setter method"""
        sq = Square(10, 5, 4, 9)
        sq.size = 8
        self.assertEqual(8, sq.size)

    def test_width_getter(self):
        """Tests width getter method"""
        sq = Square(10, 5, 4, 9)
        sq.size = 8
        self.assertEqual(8, sq.width)

    def test_height_getter(self):
        """Tests height getter method"""
        sq = Square(10, 5, 4, 9)
        sq.size = 8
        self.assertEqual(8, sq.height)

    def test_x_getter(self):
        """Tests x getter method"""
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        """Tests y getter method"""
        self.assertEqual(0, Square(10).y)


class TestSquare_size(unittest.TestCase):
    """Defines unittests for size of the Square class"""

    def test_None_size(self):
        """Tests None passed as a size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        """Tests string passed as a size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("ten")

    def test_float_size(self):
        """Tests float passed as a size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(10.5)

    def test_bool_size(self):
        """Tests boolean value passed as a size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_dict_size(self):
        """Tests dictionary passed as a size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 10, "b": 5})

    def test_list_size(self):
        """Tests list passed as a size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([10, 5])

    def test_set_size(self):
        """Tests set passed as a size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({10, 5, 4})

    def test_tuple_size(self):
        """Tests tuple passed as a size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((10, 5, 4))

    def test_range_size(self):
        """Test range object is not accepted for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(10))

    def test_inf_size(self):
        """Tests that infinity is rejected as a valid size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        """Tests that NaN is rejected as a valid size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('NaN'))

    def test_negative_size(self):
        """Tests negative numbers are not allowed"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)

    def test_zero_size(self):
        """Tests that zero is not allowed"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)


class TestSquare_x(unittest.TestCase):
    """Defines unittests for testing x attribute"""

    def test_None_x(self):
        """Tests None value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, None)

    def test_str_x(self):
        """Tests string value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "x")

    def test_float_x(self):
        """Tests float value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 5.5)

    def test_bool_x(self):
        """Tests boolean value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, True)

    def test_dict_x(self):
        """Tests dictionary value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {"a": 1, "b": 2})

    def test_list_x(self):
        """Tests list value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, [1, 2, 3])

    def test_set_x(self):
        """Tests set value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {1, 2, 3})

    def test_tuple_x(self):
        """Tests tuple value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, (1, 2, 3))

    def test_range_x(self):
        """Test range object for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, range(5))

    def test_inf_x(self):
        """Tests infinity value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('inf'))

    def test_nan_x(self):
        """Tests NaN value of x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('NaN'), 2)

    def test_negative_x(self):
        """Tests negative integer value of x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -5)


class TestSquare_y(unittest.TestCase):
    """Defines unittests for testing y attribute"""

    def test_None_y(self):
        """Tests None value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, None)

    def test_str_y(self):
        """Tests string value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, "y")

    def test_float_y(self):
        """Tests floating point number value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, 4.5)

    def test_boolean_y(self):
        """Tests boolean value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, True)

    def test_dict_y(self):
        """Tests dictionary value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, {"a": 1, "b": 2})

    def test_list_y(self):
        """Tests list value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, [1, 2, 3])

    def test_set_y(self):
        """Tests set value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, {1, 2, 3})

    def test_tuple_y(self):
        """Tests tuple value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, (1, 2, 3))

    def test_range_y(self):
        """Tests range object for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, range(4))

    def test_inf_y(self):
        """Tests infinity value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, float('inf'))

    def test_nan_y(self):
        """Tests NaN value of y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, float('NaN'))

    def test_negative_y(self):
        """Tests negative value of y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 5, -4)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Defines unittests for testing order of Square attribute"""

    def test_size_first(self):
        """Tests if size is initialized before x and y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size", "x")
            Square("size", 5, "y")
            
    def test_x_before_y(self):
        """Tests x validity before y"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "x", "y")


class TestSquare_area(unittest.TestCase):
    """Defines unittests for testing the area method"""

    def test_area_small(self):
        """Tests small square's area"""
        self.assertEqual(100, Square(10, 0, 0, 9).area())

    def test_area_large(self):
        """Tests large square's area"""
        sq = Square(999999999999999999, 0, 0, 9)
        self.assertEqual(999999999999999998000000000000000001, sq.area())

    def test_area_changed_attributes(self):
        """Tests area() after changing size"""
        sq = Square(10, 0, 0, 9)
        sq.size = 8
        self.assertEqual(64, sq.area())

    def test_area_arg(self):
        """Tests passing a different argument to area()"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaises(TypeError):
            sq.area(10)


class TestSquare_stdout(unittest.TestCase):
    """Defines unittests for testing __str__ and display methods
    of Square class"""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout

        Args:
            sq (Square): The Square ot print to stdout
            method (str): The method to run on sq
        Returns:
            The text printed to stdout by calling method on sq
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return (capture)

    def test_str_method_print_size(self):
        """Tests the output of print(sq)"""
        sq = Square(10)
        capture = TestSquare_stdout.capture_stdout(sq, "print")
        correct = "[Square] ({}) 0/0 - 10\n".format(sq.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        """Tests the output of __str__"""
        sq = Square(10, 5)
        correct = "[Square] ({}) 5/0 - 10".format(sq.id)
        self.assertEqual(correct, sq.__str__())

    def test_str_method_size_x_y(self):
        """Tests the output of str(sq)"""
        sq = Square(10, 5, 4)
        correct = "[Square] ({}) 5/4 - 10".format(sq.id)
        self.assertEqual(correct, str(sq))

    def test_str_method_size_x_y_id(self):
        """Ensures that id is included in string representation when given"""
        sq = Square(10, 5, 4, 9)
        self.assertEqual("[Square] (9) 5/4 - 10", str(sq))

    def test_str_method_changed_attributes(self):
        """Tests strinf representation when attributes change"""
        sq = Square(10, 5, 4, [9])
        sq.size = 8
        sq.x = 4
        sq.y = 3
        self.assertEqual("[Square] ([9]) 4/3 - 8", str(sq))

    def test_str_method_arg(self):
        """Tests when args passed to __str__()"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaises(TypeError):
            sq.__str__(1)

    def test_display_size(self):
        """Test display method for size attribute"""
        sq = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(sq, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        """Test display method for size and x attributes"""
        sq = Square(2, 1, 0, 9)
        capture = TestSquare_stdout.capture_stdout(sq, "display")
        self.assertEqual(" ##\n ##\n", capture.getvalue())

    def test_display_size_y(self):
        """Test display method for size and y attributes"""
        sq = Square(2, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(sq, "display")
        self.assertEqual("\n##\n##\n", capture.getvalue())

    def test_display_size_x_y(self):
        """Test display method for all attributes"""
        sq = Square(2, 1, 1, 9)
        capture = TestSquare_stdout.capture_stdout(sq, "display")
        self.assertEqual("\n ##\n, ##\n", capture.getvalue())

    def test_display_arg(self):
        """Test display method for args passed to display()"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaises(TypeError):
            sq.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    def test_update_args_zero(self):
        """Tests no args passed"""
        sq = Square(10, 5, 4, 9)
        sq.update()
        self.assertEqual("[Square] (9) 5/4 - 10", str(sq))

    def test_update_args_one(self):
        """Tests one arg passed"""
        sq = Square(10, 5, 4, 9)
        sq.update(6)
        self.assertEqual("[Square] (6) 5/4 - 10", str(sq))

    def test_update_args_two(self):
        """Tests two args passed"""
        sq = Square(10, 5, 4, 9)
        sq.update(6, 8)
        self.assertEqual("[Square] (6) 5/4 - 8", str(sq))

    def test_update_args_three(self):
        """Tests 3 args passed"""
        sq = Square(10, 5, 4, 9)
        sq.update(6, 8, 4)
        self.assertEqual("[Square] (6) 4/4 - 8", str(sq))

    def test_update_args_four(self):
        """Test 4 args passed"""
        sq = Square(10, 5, 4, 9)
        sq.update(6, 8, 4, 3)
        self.assertEqual("[Square] (6) 4/3 - 8", str(sq))

    def test_update_args_more_than_four(self):
        """Ensure that only first four args are used"""
        sq = Square(10, 5, 4, 9)
        sq.update(6, 8, 4, 3, 4)
        self.assertEqual("[Square] (6) 4/3 - 8", str(sq))

    def test_update_args_width_setter(self):
        """Tests width setter in update args"""
        sq = Square(10, 5, 4, 9)
        sq.update(6, 8)
        self.assertEqual(8, sq.width)

    def test_update_args_height_setter(self):
        """Tests height setter in update args"""
        sq = Square(10, 5, 4, 9)
        sq.update(6, 8)
        self.assertEqual(8, sq.height)

    def test_update_args_None_id(self):
        """Tests None passed for id"""
        sq = Square(10, 5, 4, 9)
        sq.update(None)
        correct = "[Square] ({}) 5/4 - 10".format(sq.id)
        self.assertEqual(correct, str(sq))

    def test_update_args_invalid_size_type(self):
        """Tests invalid type passed as size"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(6, "size")

    def test_update_args_size_zero(self):
        """Tests zero passed as a side length"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(6, 0)

    def test_update_args_size_negative(self):
        """Tests negative number passed as a side length"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(6, -8)

    def test_update_args_invalid_x(self):
        """Tests non-integer x value"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(6, 8, "x")

    def test_update_args_x_negative(self):
        """Tests negative x value"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(6, 8, -4)

    def test_update_args_invalid_y(self):
        """Tests non-integer y value"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(6, 8, 4, "y")

    def test_update_args_y_negative(self):
        """Tests ngative y value"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(6, 8, 4, -3)

    def test_update_args_size_first(self):
        """Tests that size is set before x and y"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(6, "size", "x")
            sq.update(6, "size", 4, "y")

    def test_update_args_x_before_y(self):
        """Tests that x comes before y in the argument list"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(6, 8, "x", "y")

    def test_update_kwargs_one(self):
        """Test updating a square using one keyword argument"""
        sq = Square(10, 5, 4, 9)
        sq.update(id=6)
        self.assertEqual("[Square] (6) 5/4 - 10", str(sq))

    def test_update_kwargs_two(self):
        """Test updating a square using two keyword arguments"""
        sq = Square(10, 5, 4, 9)
        sq.update(size=8, id=6)
        self.assertEqual("[Square] (6) 5/4 - 8", str(sq))

    def test_update_kwargs_three(self):
        """Test updating a square using three keyword arguments"""
        sq = Square(10, 5, 4, 9)
        sq.update(y=3, size=8, id=6)
        self.assertEqual("[Square] (6) 5/3 - 8", str(sq))

    def test_update_kwargs_four(self):
        """Tests four keywords passed to update()"""
        sq = Square(10, 5, 4, 9)
        sq.update(id=6, x=4, y=3, size=8)
        self.assertEqual("[Square] (6) 4/3 - 8", str(sq))

    def test_update_kwargs_width_setter(self):
        """Ensures width property can also be updated via its setter method"""
        sq = Square(10, 5, 4, 9)
        sq.update(id=6, size=8)
        self.assertEqual(8, sq.width)

    def test_update_kwargs_height_setter(self):
        """Ensure height property can also be updated via its setter method"""
        sq = Square(10, 5, 4, 9)
        sq.update(id=6, size=8)
        self.assertEqual(8, sq.height)

    def test_update_kwargs_None_id(self):
        """Tests None as the value for 'id' in kwargs"""
        sq = Square(10, 5, 4, 9)
        sq.update(id=None)
        correct = "[Square] ({}) 5/4 - 10".format(sq.id)
        self.assertEqual(correct, str(sq))

    def test_update_kwargs_invalid_size(self):
        """Tests invalid input for 'size'"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq.update(size="size")

    def test_update_kwargs_size_zero(self):
        """Tests zero as the value for 'size'"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=0)

    def test_update_kwargs_size_negative(self):
        """Tests negative number as the value for 'size'"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq.update(size=-8)

    def test_update_kwargs_invalid_x(self):
        """Tests non-integer values for x and y"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq.update(x="x")

    def test_update_kwargs_x_negative(self):
        """Tests a negative value for x"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq.update(x=-4)

    def test_update_kwargs_invalid_y(self):
        """Tests invalid y value"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq.update(y="y")

    def test_update_kwargs_y_negative(self):
        """Tests a negative y value"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq.update(y=-3)

    def test_update_args_and_kwargs(self):
        """Makes sure that positional arguments override keyword arguments"""
        sq = Square(10, 5, 4, 9)
        sq.update(6, 8, y=3)
        self.assertEqual("[Square] (6) 5/4 - 8", str(sq))

    def test_update_kwargs_some_wrong_keys(self):
        """Makes sure that only valid keys are used"""
        sq = Square(10, 5, 4, 9)
        sq.update(size=8, id=6, a=1, b=9)
        self.assertEqual("[Square] (6) 5/4 - 8", str(sq))


class TestSquare_to_dictionary(unittest.TestCase):
    """Defines unittests for testing to_dictionary method"""

    def test_to_dictionary_output(self):
        """Tests that the output of to_dictionary is as expected"""
        sq = Square(10, 5, 4, 9)
        correct = {'id': 9, 'x': 5, 'size': 10, 'y': 4}
        self.assertDictEqual(correct, sq.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """Makes sure that calling to_dictionary does not modify the object"""
        sq1 = Square(10, 5, 4, 9)
        sq2 = Square(8, 4, 3)
        sq2.update(**sq1.to_dictionary())
        self.assertNotEqual(sq1, sq2)

    def test_to_dictionary_arg(self):
        """Tests args passed to to_dictionary()"""
        sq = Square(10, 5, 4, 9)
        with self.assertRaises(TypeError):
            sq.to_dictionary(10)

if __name__ == "__main__":
    unittest.main()
