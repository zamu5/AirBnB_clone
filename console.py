#!/usr/bin/python3
"""Module console that contains the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand command interpreter"""
    prompt = '(hbnb) '
    com_list = {"BaseModel": BaseModel, "User": User, "Place": Place,
                "State": State, "City": City, "Amenity": Amenity,
                "Review": Review}

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id. Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg in self.com_list:
            new_inst = HBNBCommand.com_list[arg]()
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

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        list_arg = line.split()
        if len(list_arg) == 0:
            print("** class name missing **")
        elif not list_arg[0] in self.com_list:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(list_arg[0],
                            list_arg[1])not in storage.all().keys():
            print("** no instance found **")
        elif len(list_arg) == 2:
            print("** attribute name missing ** ")
        elif len(list_arg) == 3:
            print("** value missing **")
        else:
            all_objs = storage.all()
            key_aux = "{}.{}".format(list_arg[0], list_arg[1])
            if key_aux in all_objs:
                a = getattr(all_objs[key_aux], list_arg[2])
                setattr(all_objs[key_aux], list_arg[2], type(a)(list_arg[3]))
                all_objs[key_aux].save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the
        class name. Ex: $ all BaseModel or $ all
        """
        if not line:
            all_objs = storage.all()
            list_obj = []
            for objs in all_objs:
                list_obj.append(str(all_objs[objs]))
            print(list_obj)
        else:
            list_arg = line.split()
            for arg in list_arg:
                if arg not in self.com_list:
                    print("** class doesn't exist **")
                else:
                    all_objs = storage.all()
                    list_obj = []
                    for key_obj in all_objs:
                        k = key_obj.split(".")
                        if k[0] == arg:
                            list_obj.append(str(all_objs[key_obj]))
                    print(list_obj)

    def default(self, line):
        """Method for dinamic class methods"""
        command = line.split(".")
        if len(command) == 2:
            class_n = command[0]
            method = command[1]

            if method == "all()":
                self.do_all(class_n)
            elif method == "count()":
                all_objs = storage.all()
                count = 0
                for each_obj in all_objs:
                    k = each_obj.split(".")
                    if k[0] == class_n:
                        count += 1
                print(count)
            elif method[:5] == "show(" and method[-1] == ")":
                id_str = method[5:-1]
                id_num = shlex.split(id_str)
                key = class_n + "." + id_num[0]
                all_objs = storage.all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    print(all_objs[key])
            elif method[:8] == "destroy(" and method[-1] == ")":
                id_str = method[8:-1]
                id_num = shlex.split(id_str)
                key = class_n + "." + id_num[0]
                all_objs = storage.all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    del all_objs[key]
                    storage.save()
            elif method[:7] == "update(" and method[-1] == ")":
                met_str = method[7:-1]
                met_arg = met_str.split(", ")
                if len(met_arg) == 0:
                    print("** instance id missing **")
                elif len(met_arg) == 1:
                    print("** attribute name missing ** ")
                elif len(met_arg) > 1 and met_arg[1][0] == "{":
                    dict_str = ""
                    id_num = shlex.split(met_arg[0])[0]
                    for args in met_arg[1:]:
                        dict_str += args + ", "
                    new_dict = eval(dict_str[:-2])
                    for k, v in new_dict.items():
                        self.do_update("{} {} {} {}".format(class_n, id_num,
                                                        k, v))
                elif len(met_arg) == 2:
                    print("** value missing **")
                elif len(met_arg) == 3:
                    id_num = shlex.split(met_arg[0])[0]
                    attr_k = shlex.split(met_arg[1])[0]
                    attr_v = shlex.split(met_arg[2])[0]
                    self.do_update("{} {} {} {}".format(class_n, id_num,
                                                        attr_k, attr_v))
        else:
            return cmd.Cmd.default(self, line)

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
