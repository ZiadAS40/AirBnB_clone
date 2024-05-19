#!/usr/bin/env python3


""" the entry point for the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """the command iterpreter for the console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit the program"""
        return True

    def do_EOF(self, line):
        """activate the end of file signal"""
        return True

    def emptyline(self):
        """when an empty line entered nothing will happen"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
