#coding=utf-8
from types import *
import string
green = '\033[92m'
white = '\033[37m'
print white + "Hello i'm Python!",
print " What is your name?"
name = raw_input(">")
tokens = name.split()
tokens_len = len(tokens)
if tokens_len > 1:
    tokens = name.split()
    print "Ahhmm i'm confused which one of: ",
    for t in tokens:
        print green + t + " ",
    print white + "is your name?"
    arg = raw_input(">")
    if not arg.startswith(string.ascii_letters, 0, 2):
        print "so your name is: ", tokens[int(arg)], "?"
        answer = raw_input("Y/N: ")
        if answer == 'Y':
            name = tokens[int(arg)]
            print 'Hi ' + name + '!',
        else:
            print "I'm still confused because you haven't told you your name :-/ See ya"
            exit(0)
    name = arg
print 'Hello ' + name + "!"


