#!/usr/bin/env python3
"""Console for Airbnb"""
import cmd
import os
import json
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "
    last_output = ""

    __class_list = [
            "BaseModel", "User",
            "Place", "State",
            "City", "Amenity", "Review"]

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
            if line == "BaseModel":
                base_instance = BaseModel()
            elif line == "User":
                base_instance = User()
            # elif line
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

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        E.g: `destroy {id}`
        """
        obj_storage = storage.all()
        if not line:
            print("** class name missing **")
        else:
            line_list = line.split(" ")
            if line_list[0] not in HBNBCommand.__class_list:
                print("** class doesn't exist **")
            elif len(line_list) != 2:
                print("** instance id missing **")
            else:
                obj_rep = {}
                found_instance = False
                for key, value in obj_storage.items():
                    obj_dict = value.to_dict()
                    if line_list[1] == obj_dict["id"]:
                        found_instance = True
                        continue
                    else:
                        obj_rep[key] = obj_dict

                if found_instance == True:
                    with open("file.json", mode="w", encoding="utf-8") as file:
                        json.dump(obj_rep, file, indent=4, sort_keys=True)
                    storage.reload()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string rep of all instance or
        of a specific instance
        E.G: `all` or `all {modelName}`
        """

        obj_storage = storage.all()
        obj_lists = []
        if not line:
            for value in obj_storage.values():
                obj_lists.append(str(value))
            print(obj_lists)
        else:
            line_list = line.split(" ")

            if line_list[0] not in HBNBCommand.__class_list:
                print("** class doesn't exist **")
            else:
                for value in obj_storage.values():
                    obj_dict = value.to_dict()
                    if obj_dict["__class__"] == line_list[0]:
                        obj_lists.append(str(value))
                print(obj_lists)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """
        obj_storage = storage.all()
        obj_ids = []
        obj_rep = {}
        if not line:
            print("** class name missing **")
        else:
            line_list = line.split(" ")

            for key, value in obj_storage.items():
                obj_dict = value.to_dict()
                obj_ids.append(obj_dict["id"])

            if line_list[0] not in HBNBCommand.__class_list:
                print("** class doesn't exist **")
            elif len(line_list) < 2:
                print("** instance id missing **")
            elif line_list[1] not in obj_ids:
                print("** no instance found **")
            elif len(line_list) < 3:
                print("** attribute name missing **")
            elif len(line_list) < 4:
                print("** value missing **")
            else:
                for key, value in obj_storage.items():
                    obj_dict = value.to_dict()

                    if obj_dict["id"] == line_list[1]:
                        obj_dict[line_list[2]] = f"{line_list[3]}"
                    obj_rep[key] = obj_dict
                with open("file.json", mode="w", encoding="utf-8") as file:
                    json.dump(obj_rep, file, indent=4, sort_keys=True)
                storage.reload()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
