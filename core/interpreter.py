#!/usr/bin/env python3
# This package depends on PLY -- http://www.dabeaz.com/ply/


import os
from ply import *
import core.Config
from core.Mappings import *
from core.Lexer import *
from core.IndentWriter import *
from core.Converter import *


def main(argv):
    if argv['--debug']:
        core.Config.DEBUG = True
    if core.Config.DEBUG:
        print("\n[DEBUG]")
        print("argv: "+str(argv))
    if argv['<filename>']:
        filename = argv['<filename>']
        if argv['--convert']:
            convert(filename)
            return
    else:
        execfile(sys.stdin)
        return

    execfile(filename, argv['--argument'], "__main__")


if __name__ == "__main__":
    main(sys.argv)
