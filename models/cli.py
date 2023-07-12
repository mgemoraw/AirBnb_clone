
from user import User

import sys
import cmd
import os


class CommandLine(cmd.Cmd):
    def do_user(self, arg):
        user = User()
        user.id = 2

        print(user.id)


    def help_user(self, arg):
        print("Help of user")

    def do_exit(self, arg):
        """ >>> exit to exit"""
        sys.exit()

    def do_quit(self, arg):
        """ >>> quit to exit"""
        sys.exit()

if __name__ == "__main__":
    CommandLine().cmdloop()