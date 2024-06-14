#!/usr/bin/env python3


""" the entry point for the command interpreter """

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.base_model import storage


class SkipCommand(Exception):
    pass


class HBNBCommand(cmd.Cmd):
    """the command iterpreter for the console"""
    prompt = "(hbnb) "
    objs = ["BaseModel"]

    def do_quit(self, arg):
        """quit the program"""
        return True

    def do_create(self, obj):
        """create an instance of the obj class"""
        if obj is not None:
            if obj in self.objs:
                l_obj = eval(obj + "()")
                l_obj.save()
                print(l_obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """show the string representation of an instance"""
        storage.reload()
        parts = line.split()
        if len(line.split()) < 1:
            print("** class name missing **")
            self.cmdloop(intro='')
        elif len(line.split()) < 2:
            print("** instance id missing **")
            self.cmdloop(intro='')

        obj, obj_id = parts
        flagO = 0
        flag = 0

        for key, value in storage._FileStorage__objects.items():
            keyW = key.split('.')
            if keyW[0] == obj:
                flagO = 1
                if keyW[1] == obj_id:
                    print(value)
                    flag = 1
        if flagO == 0:
            print("** class doesn't exist **")
        if flag == 0:
            print("** no instance found **")

    def do_destroy(self, line):
        """delete an instance based on name and id"""
        storage.reload()
        parts = line.split()
        if len(line.split()) < 1:
            print("** class name missing **")
            self.cmdloop(intro='')
        if len(line.split()) < 2:
            print("** instance id missing **")
            self.cmdloop(intro='')

        obj, obj_id = parts
        flagO = 0
        flag = 0

        for key, value in storage._FileStorage__objects.items():
            keyW = key.split('.')
            if keyW[0] == obj:
                flagO = 1
                if keyW[1] == obj_id:
                    flag = 1
        if flag == 0:
            print("** no instance found **")
        if flagO == 0:
            print("** class doesn't exist **")

        if flagO == 1 and flag == 1:
            del storage._FileStorage__objects[obj + '.' + obj_id]
        storage.save()

    def do_all(self, line):
        """show all the instances"""
        storage.reload()
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
        if len(line.split()) < 1:
            print("** class name missing **")
            self.cmdloop(intro='')
        if len(line.split()) < 2:
            print("** instance id missing **")
            self.cmdloop(intro='')
        if len(line.split()) < 3:
            print("** attribute name missing **")
            self.cmdloop(intro='')
        if len(line.split()) < 4:
            print("** value missing **")
            self.cmdloop(intro='')

        ob, ob_id, attr, valueA = parts
        flagO = 0
        flag = 0

        for key, value in storage._FileStorage__objects.items():
            keyW = key.split('.')
            if keyW[0] == ob:
                flagO = 1
                if keyW[1] == ob_id:
                    flag = 1
        if flag == 0:
            print("** no instance found **")
        if flagO == 0:
            print("** class doesn't exist **")
        tType = type(attr)
        vlueB = tType(valueA)
        if flagO == 1 and flag == 1:
            mydict = storage._FileStorage__objects[ob + '.' + ob_id].to_dict()
            mydict[attr] = vlueB
            del storage._FileStorage__objects[ob + '.' + ob_id]
            cls = eval(ob + "(**mydict)")
            storage.new(cls)
        storage.save()

    def do_EOF(self, line):
        """activate the end of file signal"""
        return True

    def emptyline(self):
        """when an empty line entered nothing will happen"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
