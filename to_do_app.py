import sys

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
        self.openedfile = model.file_opener("database.txt")
        if len(self.list_argv) == 0:
            view.print_usage()
        elif len(self.list_argv) >= 1:
            if self.list_argv[0] == "-l":
                view.print_list(self.openedfile)
            elif self.list_argv[0] == "-a" and self.list_argv[1:]:
                model.add_new_task(self.list_argv, self.openedfile)
            elif self.list_argv[0] == "-a":
                print("Unable to add: no task provided")

class Model():

    def add_new_task(self, list_argv, file_to_use):
        self.file_to_use = file_to_use
        self.list_argv = list_argv
        self.write_to_file(self.list_argv[1] + '\n')


    def file_opener(self, thefile):
        self.thefile = thefile
        self.content = open(thefile, 'r')
        self.content_read = self.content.readlines()
        list_file = []
        for lines in self.content_read:
            list_file.append(lines)
        self.content.close()
        return list_file


    def write_to_file(self, newcontent):
        self.newcontent = newcontent
        #self.file_to_write = file_to_write
        self.file_to_write=open("database.txt", 'a')
        for task in self.newcontent:
            self.file_to_write.write(task)
        self.file_to_write.close()
        self.final_content = open("database.txt", 'r')
        self.line_read_final_content = self.final_content.readlines()
        self.file_to_write.close()

    def remove_task(self, which):
        pass

class View():

    def print_usage(self):
        model.file_opener("usage.txt")

    def print_list(self, content):
        self.content = content
        self.newcontent = []
        if len(self.content) == 0:
            print("No todos today!")
        else:
            for i in range(0, len(self.content)):
                self.result = ""
                self.result += str(i+1) + " - " + self.content[i].__str__()
                self.newcontent.append(self.result)
                print(self.result)

view = View()
model = Model()
controller = Controller()
