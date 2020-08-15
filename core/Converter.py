#!/usr/bin/env python3

import os
import io
import keyword
import types
import sys

from core.Lexer import *
from core.IndentWriter import *
import core.Config

HEADER = u''''''
BODY = u'''
import sys as _sys
'''

def to_python(s):
    "Convert dawg code to Python code"
    L = Lexer()
    L.input(s)
    header = io.StringIO()
    header.write(HEADER)
    header_output = IndentWriter(header)

    body = io.StringIO()
    body.write(BODY)
    body_output = IndentWriter(body)

    write = body_output.write
    output = body_output

    for t in iter(L.token_stream):
        if t.type == "NAME":
            name = t.value.rstrip("_")
            if name in keyword.kwlist:
                write(t.value + "_ ")
            else:
                write(t.value + " ")

        elif t.type in ("RESERVED", "OP", "NUMBER", "CLOSE"):
            write(t.value+" ")

        elif t.type == "STRING":
            write(repr(t.value) + " ")

        elif t.type == "COMMENT":
            write("#" + t.value[3:]+"\n")
            output.at_first_column = True
        elif t.type == "MULTILINECOMMENT":
            write("\'\'\'" + t.value + "\'\'\'")
        elif t.type == "COLON":
            write(":")

        elif t.type == "INDENT":
            output.indent += 1
            pass
        elif t.type == "DEDENT":
            output.indent -= 1
            pass
        elif t.type == "FILLER":
            pass
        elif t.type == "NEWLINE":
            write(t.value)
            output.at_first_column = True
            output = body_output
            write = output.write
        elif t.type == "PRINT":
            if t.value == "stdout":
                write("print ")
            else:
                raise AssertionError(t.value)
        elif t.type == "AUTOCALL":
            write(t.value + "(")
        elif t.type == "INLINE":
            write(t.value)
        elif t.type == "ENDMARKER":
            write("\n")
        elif t.type == "WS":
            output.leading_ws = t.value
        elif t.type == "FUTURE":
            output = header_output
            write = output.write
            write("from __future__ import ")

        else:
            raise AssertionError(t.type)

    return header.getvalue() + body.getvalue()


def execfile(infile, args, module_name="__dawg__"):
    "file, module_name -- exec the dawg file in a newly created module"
    infile = ''.join(infile)
    try:
        if not hasattr(infile, "read"):
            s = open(infile).read()
        else:
            s = infile.read()
    except IOError:
        print("[Error] Cant read file '{}', check if it exists and reachable".format(infile)) 
        return
    return execstring(s, args, module_name)


def execstring(s, args,  module_name="__dawg__"):
    "s, module_name -- exec the dawg string in a newly created module"
    python_s = to_python(s)
    m = types.ModuleType(module_name)
    sys.modules[module_name] = m
    if core.Config.DEBUG:
        print("\n[DEBUG] Converted code:")
        print(python_s)
    if args:
        exec(python_s, {'argv_': args})
    else:
        exec(python_s)
    return m


def convert_file(infile, outfile):
    "read dawg code from infile, write converted Python code to outfile"
    if not hasattr(outfile, "write"):
        outfile = open(outfile, "w")
    outfile.write(to_python(infile.read()))


def convert(filenames):
    "convert Dawg '.dawg' files into Python '.py' files"
    if not filenames:
        convert_file(sys.stdin, sys.stdout)
    else:
        if core.Config.DEBUG:
            print("\n[DEBUG]")
            print("convert filenames: "+str(filenames))
        for filename in filenames:
            try:
                base, ext = os.path.splitext(filename)
                base = ''.join(base.split('/')[-1:])
                convert_file(open(filename), open("converted/"+base+".py", "w+"))
            except IOError:
                print("[Error] Cant read file \'{}\', check if it exists and reachable".format(filename))
                continue
