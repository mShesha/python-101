##
# hello_world.py
# Takes input of your name from STDIN and prints the first name.
##

import sys
import string

def hello(name):
    print("Hello, %s" % (name))

if __name__ == "__main__":
    hello(sys.argv[1])