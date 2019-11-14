#!/usr/bin/python3
"""module test for test console"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import datetime
import os


class TestConsole(unittest.TestCase):
    """TestConsole class for testing the console"""
    if os.path.exists("file.json"):
        os.remove("file.json")

    list_class = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                  "Review"]

    def test_help_a(self):
        """test the help command with args"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue(),
                             'stop the command line interpreter\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("   help     quit    ")
            self.assertEqual(f.getvalue(),
                             'stop the command line interpreter\n')

    def test_newline(self):
        """test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
            self.assertEqual(f.getvalue(), '')

    def test_wrong_command(self):
        """test when no command exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("hola")
            self.assertEqual(f.getvalue(), '*** Unknown syntax: hola\n')

    def test_help(self):
        """test when no command exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(f.getvalue(), '\n'
                             'Documented commands (type help <topic>):\n'
                             '========================================\n'
                             'EOF  all  create  destroy  help  quit  show'
                             '  update\n\n')

    def test_quit_EOF(self):
        """test exits options"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), '\n')

    def test_create(self):
        """test when no command create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
                self.assertRegex(f.getvalue(), '^[0-9a-f]{8}-[0-9a-f]{4}-[1-5]'
                                 '[0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                                 '[0-9a-f]{12}$')
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_show(self):
        """test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + class_n)
                self.assertEqual(f.getvalue(), '** instance id missing **\n')
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + class_n + " 23534624535687876")
                self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_show_create(self):
        """test show command with objects"""
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
                id_str = f.getvalue()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + class_n + " " + id_str)
                obj_str = f.getvalue()
                self.assertEqual(obj_str[:(41 + len(class_n))],
                                 '[' + class_n + '] (' + id_str[:-1] + ')')
                dict_obj = eval(obj_str[(41 + len(class_n)):-1])
                self.assertTrue(type(dict_obj) is dict)
                self.assertTrue(type(dict_obj["created_at"])
                                is datetime.datetime)
                self.assertTrue(type(dict_obj["updated_at"])
                                is datetime.datetime)
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_destroy(self):
        """test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy " + class_n)
                self.assertEqual(f.getvalue(), '** instance id missing **\n')
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy " + class_n + " 235346245356878")
                self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_destroy_create(self):
        """test destroy command with objects"""
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
                id_str = f.getvalue()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + class_n + " " + id_str)
                obj_str = f.getvalue()
                self.assertEqual(obj_str[:(41 + len(class_n))],
                                 '[' + class_n + '] (' + id_str[:-1] + ')')
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy " + class_n + " " + id_str)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + class_n + " " + id_str)
                self.assertEqual(f.getvalue(), '** no instance found **\n')
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all")
                self.assertNotEqual(f.getvalue(), "")
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all " + class_n)
                str_list = f.getvalue()
                self.assertNotEqual(str_list, "")
                list_of_str = eval(str_list[:-1])
                self.assertTrue(type(list_of_str) is list)
                for item in list_of_str:
                    self.assertTrue(type(item) is str)
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all MyModel")
                self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_update(self):
        """test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update " + class_n)
                self.assertEqual(f.getvalue(), '** instance id missing **\n')
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update " + class_n + " 2353462453568")
                self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_update_create(self):
        """test update command with objects"""
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
                id_str = f.getvalue()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update " + class_n + " " + id_str)
                self.assertEqual(f.getvalue(),
                                 '** attribute name missing **\n')
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update " + class_n + " " + id_str +
                                     " first_name")
                self.assertEqual(f.getvalue(), '** value missing **\n')
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update " + class_n + " " + id_str +
                                     " first_name \"Betty\"")
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + class_n + " " + id_str)
                obj_str = f.getvalue()
                dict_obj = eval(obj_str[(41 + len(class_n)):-1])
                self.assertTrue(type(dict_obj) is dict)
                self.assertIn("first_name", dict_obj)
                self.assertTrue(type(dict_obj["first_name"]) is str)
                self.assertEqual(dict_obj["first_name"], "Betty")
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_class_all(self):
        """test <class_name>.all() method"""
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".all()")
                str_list = f.getvalue()
                self.assertNotEqual(str_list, "")
                list_of_str = eval(str_list[:-1])
                self.assertTrue(type(list_of_str) is list)
                for item in list_of_str:
                    self.assertTrue(type(item) is str)
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_class_count(self):
        """test <class_name>.count() method"""
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".count()")
                str_list = f.getvalue()
                num1 = int(str_list[:-1])
                self.assertTrue(type(num1) is int)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".count()")
                str_list = f.getvalue()
                num2 = int(str_list[:-1])
                self.assertEqual(num1 + 1, num2)
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_class_show(self):
        """test <class_name>.show() method"""
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".show(\"Holberton\")")
                self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_class_show_create(self):
        """test show command with objects"""
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
                id_str = f.getvalue()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".show(" + id_str[:-1] + ")")
                obj_str = f.getvalue()
                self.assertEqual(obj_str[:(41 + len(class_n))],
                                 '[' + class_n + '] (' + id_str[:-1] + ')')
                dict_obj = eval(obj_str[(41 + len(class_n)):-1])
                self.assertTrue(type(dict_obj) is dict)
                self.assertTrue(type(dict_obj["created_at"])
                                is datetime.datetime)
                self.assertTrue(type(dict_obj["updated_at"])
                                is datetime.datetime)
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_class_destroy(self):
        """test <class_name>.destroy() method"""
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".destroy(\"Holberton\")")
                self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_class_destroy_create(self):
        """test show command with objects"""
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
                id_str = f.getvalue()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".destroy(" + id_str[:-1] + ")")
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".show(" + id_str[:-1] + ")")
                self.assertEqual(f.getvalue(), '** no instance found **\n')
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_class_update(self):
        """test <class_name>.update(<id>, <attribute_name>, <attribute_value>)
        command
        """
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".update(\"46543635156\")")
                self.assertEqual(f.getvalue(),
                                 '** attribute name missing **\n')
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n +
                                     ".update(\"3521541313\", \"k\", \"v\")")
                self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_class_update_create(self):
        """test <class_name>.update(<id>, <attribute_name>, <attribute_value>)
        command
        """
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
                id_str = f.getvalue()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".update(\"" + id_str +
                                     "\", \"first_name\")")
                self.assertEqual(f.getvalue(), '** value missing **\n')
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".update(\"" + id_str +
                                     "\", \"first_name\", \"Betty\")")
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + class_n + " " + id_str)
                obj_str = f.getvalue()
                dict_obj = eval(obj_str[(41 + len(class_n)):-1])
                self.assertTrue(type(dict_obj) is dict)
                self.assertIn("first_name", dict_obj)
                self.assertTrue(type(dict_obj["first_name"]) is str)
                self.assertEqual(dict_obj["first_name"], "Betty")
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_class_update_dict(self):
        """test <class_name>.update(<id>, <dictionary>)
        command
        """
        for class_n in self.list_class:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_n)
                id_str = f.getvalue()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(class_n + ".update(\"" + id_str +
                                     "\", {\'first_name\': \"Betty\","
                                     " \"age\": 89})")
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show " + class_n + " " + id_str)
                obj_str = f.getvalue()
                dict_obj = eval(obj_str[(41 + len(class_n)):-1])
                self.assertTrue(type(dict_obj) is dict)
                self.assertIn("first_name", dict_obj)
                self.assertTrue(type(dict_obj["first_name"]) is str)
                self.assertEqual(dict_obj["first_name"], "Betty")
                self.assertIn("age", dict_obj)
        if os.path.exists("file.json"):
            os.remove("file.json")

if __name__ == '__main__':
    unittest.main()
