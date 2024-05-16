#!/usr/bin/env python3
import cmd
import os
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Simple command processor example. """
    prompt = '(hbnb) '
    last_output = ''

    __class_list = ["BaseModel"]

    def do_shell(self, line):
        """ Run a shell command """
        print("running shell command:", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output


    def do_EOF(self, line):
        """ End of File command: Ctrl + d """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """Empty Line"""
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel
        + saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.__class_list:
            print("** class doesn't exist **")
        else:
            base_instance = BaseModel()
            base_instance.save()
            print(base_instance.id)

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class name and id """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.__class_list:
            print("** class doesn't exist **")
        else:
            print("")



    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
