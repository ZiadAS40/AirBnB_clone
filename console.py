#!/usr/bin/env python3


""" the entry point for the command interpreter """

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.base_model import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """the command iterpreter for the console"""
    prompt = "(hbnb) "
    objs = ["BaseModel", "User", "State", "City", "Place", "Review", "Amenity"]

    def do_quit(self, arg):
        """quit the program"""
        return True

    def do_create(self, line):
        """create an instance of the obj class"""
        if len(line.split()) == 0:
            print("** class name missing **")
        else:
            if line in self.objs:
                l_obj = eval(line + "()")
                l_obj.save()
                print(l_obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """show the string representation of an instance"""
        parts = line.split()
        if len(parts) == 0:
            print("** class name missing **")
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        else:
            parts = line.split(' ')
            ssr = parts[0] + '.' + parts[1]
            if parts[0] in self.objs:
                if ssr in storage._FileStorage__objects:
                    print(storage._FileStorage__objects[ssr])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """delete an instance based on name and id"""
        if len(line.split()) == 0:
            print("** class name missing **")
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        else:
            parts = line.split(' ')
            ssr = parts[0] + '.' + parts[1]
            if parts[0] in self.objs:
                if ssr in storage._FileStorage__objects:
                    del storage._FileStorage__objects[ssr]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """show all the instances"""
        parts = line.split()
        flag = 0
        if len(line.split()) == 0:
            for key, value in storage._FileStorage__objects.items():
                print(value)
        else:
            for key, value in storage._FileStorage__objects.items():
                keyW = key.split('.')
                if keyW[0] == parts[0]:
                    print(value)
                    flag = 1
            if flag == 0:
                print("** class doesn't exist **")

    def do_update(self, line):
        """update an attribute for instance"""
        parts = line.split()
        if len(parts) < 1:
            print("** class name missing **")
        elif len(parts) < 2:
            print("** instance id missing **")
        elif len(parts) < 3:
            print("** attribute name missing **")
        elif len(parts) < 4:
            print("** value missing **")
        else:
            ob, ob_id, attr, valueA = parts
            if ob in self.objs:
                ssr = ob + '.' + ob_id
                if ssr in storage._FileStorage__objects:
                    tType = type(attr)
                    vlueB = tType(valueA)
                    mydict = (storage._FileStorage__objects[ob + '.' + ob_id].
                              to_dict())
                    mydict[attr] = vlueB
                    del storage._FileStorage__objects[ob + '.' + ob_id]
                    cls = eval(ob + "(**mydict)")
                    storage.new(cls)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_EOF(self, line):
        """activate the end of file signal"""
        print()
        return True

    def emptyline(self):
        """when an empty line entered nothing will happen"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
