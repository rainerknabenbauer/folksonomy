import sys


# To run this script, you have to call it from Terminal like so:
# python3 command-line-parameters.py hello


def run():
    if application_started_from_terminal():
        print_arguments()


# This is the core of the application.
# sys.argv gives you an array with all command line parameters.
# sys.argv[0] is ALWAYS the filename (or file path)
# sys.argv[1] to sys.argv[..] contains every parameter separated by space!
def print_arguments():
    print("On startup I received " + sys.argv.__len__().__str__() + " number of command line arguments:")
    i = 1  # Declare and initialize a counter that starts at 1
    for argument in sys.argv:
        print("Argument " + i.__str__() + ": " + argument)
        i += 1  # Increment the counter, short for: i = i + 1


def print_welcome():
    print("To test this program, please call it directly from the Terminal.")
    print("Usage: python3 command-line-parameters.py {add-your-own-parameters}")
    print("")


# Here I'm just making sure you don't start it from PyCharm - you can skip this part.
# If you start it from PyCharm,
# 1. your path will look something like /Users/.../.../.../command-line-parameters.py
# 2. you will not pass in any arguments (except for the path to the script - it's also a command line argument :) )
def application_started_from_terminal():
    file_name_length = len("command-line-parameters.py")
    if sys.argv[0].__len__() > file_name_length:
        print("!! Please use Terminal to call the script and add command line parameters !!")
        print("")
        print("I see that your path is:")
        print(sys.argv[0])
        print("That means you have not used Terminal OR you are not in the same folder.")
        print("Please navigate to the same folder your script is in and execute the script with:")
        print("python3 command-line-parameters.py {add-your-own-parameters}")
        return False
    return True


if __name__ == '__main__':
    print_welcome()
    run()
