#!/usr/bin/python3
"""Module console that contains the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand command interpreter"""
    prompt = '(hbnb) '
    com_list = ["BaseModel"]

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id. Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg in self.com_list:
            new_inst = BaseModel()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id
        """
        if not line:
            print("** class name missing **")
        else:
            list_arg = line.split()
            if list_arg[0] not in self.com_list:
                print("** class doesn't exist **")
            elif len(list_arg) < 2:
                print("** instance id missing **")
            else:
                key = list_arg[0] + "." + list_arg[1]
                all_objs = storage.all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    print(all_objs[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file)
        """
        if not line:
            print("** class name missing **")
        else:
            list_arg = line.split()
            if list_arg[0] not in self.com_list:
                print("** class doesn't exist **")
            elif len(list_arg) < 2:
                print("** instance id missing **")
            else:
                key = list_arg[0] + "." + list_arg[1]
                all_objs = storage.all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    del all_objs[key]
                    storage.save()

    def do_quit(self, arg):
        """stop the command line interpreter"""
        return True

    def do_EOF(self, arg):
        """stop the command line interpreter"""
        print()
        return True

    def emptyline(self):
         pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
