import sys
import os

class Controller():

    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.controller()
        self.model = model

    def arg_reader(self):
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

    def controller(self):
        if len(self.list_argv) == 0:
            view.print_usage()
        elif len(self.list_argv) >= 1:
            if self.list_argv[0] == "-l": #itt először a model-ben hívjon meg egy külön methodot - mondjuk a file opener funkciót; meg az ez után következőknél is
                view.print_list()
            elif self.list_argv[0] == "-a" and self.list_argv[1:]:
                model.add_new_task(self.list_argv)
            elif self.list_argv[0] == "-a":
                print("Unable to add: no task provided")

class Model():

    def add_new_task(self, list_argv):
        self.list_argv = list_argv
        self.content = open("database.txt", "a")
        self.appended = self.content.write(str(self.list_argv[1]) + "\n")
        self.content.close()
        view.print_list()

    # refactor print_listlogic to here
    # def listing(self):
    #     if os.stat("database.txt").st_size == 0:
    #         print("No todos today!")
    #     else:
    #         for i in range(0, len(self.read_content)):
    #             result = ""
    #             result += str(i+1) + " - " + self.read_content[i].__str__()
    #             print(result)
    #     view.print_list


    # def open_file(self):
    #     self.content = open("database.txt", "r")
    #     self.read_content = self.content.readlines()

class View():
    # def __init__(self):
    #     pass

    def print_usage(self):
        self.content = open("usage.txt", "r")
        self.read_content = self.content.read()
        print(self.read_content)
        self.content.close()

    def print_list(self):
        self.content = open("database.txt", "r")
        self.read_content = self.content.readlines()
        if os.stat("database.txt").st_size == 0:
            print("No todos today!")
        else:
            for i in range(0, len(self.read_content)):
                result = ""
                result += str(i+1) + " - " + self.read_content[i].__str__()
                print(result)
        self.content.close()


view = View()
model = Model()
controller = Controller()
