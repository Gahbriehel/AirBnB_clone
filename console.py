#!/usr/bin/env python3
import cmd
import os


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
    last_output = ''

    def do_shell(self, line):
        """Run a shell command"""
        print("running shell command:", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output


    def do_EOF(self, line):
        """
        End of File: Ctrl + d
        """
        return True

    def do_quit(self, line):
        """End of File
        Use: Ctrl + d
        """
        return True

    def emptyline(self):
        """Empty Line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
