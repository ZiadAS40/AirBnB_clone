#!/usr/bin/python3
import cmd
""" the entry point for the command interpreter """


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quite(self, arg):
        """quite the program"""
        return True

    def do_EOF(self, line):
        """activate the end of file signal"""
        return True

    def emptyline(self):
        """when an empty line entered nothing will happen"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
