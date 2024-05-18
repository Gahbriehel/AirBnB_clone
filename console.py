#!/usr/bin/env python3
import cmd
import os
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "
    last_output = ""

    __class_list = ["BaseModel"]

    def do_shell(self, line):
        """Run a shell command"""
        print("running shell command:", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output

    def do_EOF(self, line):
        """End of File command: Ctrl + d"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty Line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel
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
        """Prints the string representation of an
        instance based on the class name and id"""
        obj_storage = storage.all()
        if not line:
            print("** class name missing **")
        else:
            line_list = line.split(" ")
            obj_ids = {}
            for value in obj_storage.values():
                obj_tem = value.to_dict()
                key = obj_tem["id"]
                obj_ids[key] = value
            if line_list[0] not in HBNBCommand.__class_list:
                print("** class doesn't exist **")
            elif len(line_list) != 2:
                print("** instance id missing **")
            elif line_list[1] not in obj_ids:
                print("** no instance found **")
            else:
                print(obj_ids[line_list[1]])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
