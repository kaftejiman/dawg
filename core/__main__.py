#!/usr/bin/env python3

"""Interpreter of Dawg code written in Python

Usage: 
    dawg [-hvdci] <filename>... [-a=<arg>...]
    dawg <filename>

Options:
    -h, --help                                                    Show this help message and exit
    -v, --version                                                 Show version and exit
    -d, --debug    <filename>... [-a=<arg>...]                    Enable debug mode
    -c, --convert  <filename>... [-a=<arg>...]                    Convert a Dawg program to the corresponding Python program
    -a, --argument=<arg>...                                       Provide argument to Dawg program
    -i, --interact                                                Open an interactive Dawg session
"""

from docopt import docopt
from core import VERSION


def run():
    args = docopt(__doc__, version=VERSION)
    if args['--interact']:
        print('todo')
    else:
        import core.interpreter as interpreter
        interpreter.main(args)
