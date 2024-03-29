#!/usr/bin/python3
"""Unittest for base.py

Unittest classes:
    TestBase_instantiation - line 19
    TestBase_to_json_string - line 104
    TestBase_save_to_file - line 244
    TestBase_from_json_string - line 
    TestBase_create - line 
    TestBase_load_from_file - line """
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Define unittests for Base class instantiation"""

    def test_no_arg(self):
        """Test if an object can be created without passing any argument
        and id will still be unique for each object 2 objs"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        """Test if an object can be created without passing any argument
        and id will still be unique for each object 3 objs"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_None_id(self):
        """Test `None` as an argument"""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_unique_id(self):
        """Test id assignment"""
        self.assertEqual(10, Base(10).id)

    def test_id_public(self):
        """Test id is public (not private)"""
        b = Base(5)
        b.id = 10
        self.assertEqual(10, b.id)

    def test_nb_objects_private(self):
        """Test __nb_objects is private"""
        with self.assertRaises(AttributeError):
            print(Base(10).__nb_objects)

    def test_str_id(self):
        """Test id as string representation"""
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        """Test id as float"""
        self.assertEqual(10.5, Base(10.5).id)

    def test_bool_id(self):
        """Test id as boolean"""
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """Test id as list"""
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict_id(self):
        """Test id as dictionary"""
        self.assertEqual({"a": 5, "b": 6}, Base({"a": 5, "b": 6}).id)

    def test_tuple_id(self):
        """Test id as tuple"""
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        """Test id as set"""
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_range_id(self):
        """Test id generated from range function"""
        self.assertEqual(range(5), Base(range(5)).id)

    def test_inf_id(self):
        """Test infinity value in id"""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """Test NaN (Not a Number) value in id"""
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        """Test two arguments"""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Define unittests for Base class to_json_string method"""

    def test_to_json_string_rectangle_type(self):
        """Test if rectangle type is correctly converted to json string"""
        rect = Rectangle(8, 4, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        """Test if one rectangle object is correctly converted to json string"""
        rect = Rectangle(8, 4, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 52)

    def test_to_json_string_rectangle_two_dicts(self):
        """Test if multiple rectangle objects are correctly converted to json string"""
        rect1 = Rectangle(8, 4, 2, 8, 6)
        rect2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 105)

    def test_to_json_string_square_type(self):
        """Test if square type is correctly converted to json string"""
        sq = Square(8, 2, 2, 4)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        """Test if one square object is correctly converted to json string"""
        sq = Square(8, 2, 2, 4)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 38)

    def test_to_json_string_square_two_dicts(self):
        """Test if multiple square objects are correctly converted to json string"""
        sq1 = Square(8, 2, 2, 4)
        sq2 = Square(9, 3, 6, 3)
        list_dicts = [sq1.to_dictionary(), sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 76)

    def test_to_json_string_empty_list(self):
        """Test an empty list pased as an argument"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        """Test None passed as an argument"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """Test no arguments passed"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        """Test more than one argument passed"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Define unittests for Base class save_to_file method"""

    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        """Test saving one Rectangle object to a file"""
        rect = Rectangle(10, 5, 2, 6, 2)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        """Test saving two Rectangle objects to the same file"""
        rect1 = Rectangle(10, 5, 2, 6, 2)
        rect2 = Rectangle(9, 3, 2, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        """Test saving one Square object to a file"""
        sq = Square(10, 2, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        """Test saving two Square objects to the same file"""
        sq1 = Square(10, 2, 2, 8)
        sq2 = Square(5, 3, 3, 7)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        """Test that class name is used for filename if no argument given"""
        sq = Square(10, 2, 2, 8)
        Base.save_to_file([sq])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        """Test overwriting an existing file"""
        sq = Square(5, 3, 3, 7)
        Square.save_to_file([sq])
        sq = Square(10, 2, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        """Test passing None to save_to_file"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        """Test passing empty list to save_to_file"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        """Test calling save_to_file without any arguments"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        """Test calling save_to_file with more than one argument"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Define unittests for Base class fom_json_string method"""

    def test_from_json_string_type(self):
        """Test that from_json_string returns a Base object when given a string"""
        list_input = [{"id": 9, "width": 5, "height": 10}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        """Test single rectangle in the input"""
        list_input = [{"id": 9, "width": 5, "height": 10, "x": 2}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        """Test multiple rectangles in the input"""
        list_input = [
            {"id": 9, "width": 5, "height": 10, "x": 2, "y": 4},
            {"id": 8, "width": 10, "height": 5, "x": 6, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        """Test single square in the input"""
        list_input = [{"id": 9, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        """Test multiple squares in the input"""
        list_input = [
            {"id": 9, "size": 10, "height": 4},
            {"id": 8, "size": 5, "height": 3}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        """Test None as an argument"""
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        """Test empty list as an argument"""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """Test no arguments passed to from_json_string()"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """Test too many arguments passed to from_json_string()"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Define unittests for Base class create method"""

    def test_create_rectangle_original(self):
        """Create a rectangle and check its attributes"""
        rect1 = Rectangle(8, 4, 2, 8, 6)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (6) 2/8 - 8/4", str(rect1))

    def test_create_rectangle_new(self):
        """Create a new rectangle using create()"""
        rect1 = Rectangle(9, 3, 4, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (7) 4/2 - 9/3", str(rect2))

    def test_create_rectangle_is(self):
        """Check that the created object is different obj"""
        rect1 = Rectangle(9, 3, 4, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertIsNot(rect1, rect2)

    def test_create_rectangle_equals(self):
        """Compare two objects made by create()"""
        rect1 = Rectangle(9, 3, 4, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertNotEqual(rect1, rect2)

    def test_create_square_original(self):
        """Create a square and check its attributes"""
        sq1 = Square(4, 2, 3, 8)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (8) 2/3 - 4", str(sq1))

    def test_create_square_new(self):
        """Create a new square using create()"""
        sq1 = Square(4, 2, 3, 8)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (8) 2/3 - 4", str(sq2))

    def test_create_square_is(self):
        """Check that the created object is different obj"""
        s1 = Square(4, 2, 3, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        """Compare two objects made by create()"""
        s1 = Square(4, 2, 3, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Define unittests for Base class load_from_file method"""

    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        """Load first Rectangle from file and check its attributes"""
        rect1 = Rectangle(10, 5, 2, 6, 2)
        rect2 = Rectangle(9, 3, 2, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        """Load second Rectangle from file and check it's in the list"""
        rect1 = Rectangle(10, 5, 2, 6, 2)
        rect2 = Rectangle(9, 3, 2, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        """Check that only Rectangle types are loaded"""
        rect1 = Rectangle(10, 5, 2, 6, 2)
        rect2 = Rectangle(9, 3, 2, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        """Load first Square from file and check its attributes"""
        sq1 = Square(10, 2, 2, 8)
        sq2 = Square(5, 3, 3, 7)
        Square.save_to_file([sq1, sq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        """Load second Square from file and check it's in the list"""
        sq1 = Square(10, 2, 2, 8)
        sq2 = Square(5, 3, 3, 7)
        Square.save_to_file([sq1, sq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        """Check that only Square types are loaded"""
        sq1 = Square(10, 2, 2, 8)
        sq2 = Square(5, 3, 3, 7)
        Square.save_to_file([sq1, sq2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        """Try to load a file without creating one should return an empty list"""
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        """Test if function raises error when more than one argument is passed"""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

if __name__ == "__main__":
    unittest.main()
