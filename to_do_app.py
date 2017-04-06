import sys
#import database.txt

class Controller():

    def __init__(self):
        pass

    def arg_reader(self):
        self.list_argv = []
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

        if len(self.list_argv) == 0:
            view.print_usage()
        else:
            pass
    	# if( arguments[0] == '-l' ):
    	# 	print('Addolunk ilyet', arguments[1])

class Model():
    pass


class View():
    def __init__(self):
        pass

    def print_usage(self):
        print("Python Todo application\n"
            "=======================\n\n"

            "Command line arguments:\n"
             "-l   Lists all the tasks\n"
             "-a   Adds a new task\n"
             "-r   Removes an task\n"
             "-c   Completes an task")

controller = Controller()
view = View()

controller.arg_reader()
#view.print_usage()
