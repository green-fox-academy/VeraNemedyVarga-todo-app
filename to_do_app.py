import sys
#import database.txt

class Controller():

    def __init__(self):
        pass

    # def arg_reader():
    # 	if len(sys.argv) == 1:
    # 		return []
    # 	else:
    # 		return sys.argv[1:]
    # # arguments = arg_reader()
    #
    # if len(arguments) == 0:
    # 	print('help text')
    # else:
    # 	if( arguments[0] == '-l' ):
    # 		print('Addolunk ilyet', arguments[1])

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

welcome = View()
welcome.print_usage()
