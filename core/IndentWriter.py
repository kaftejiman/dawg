#!/usr/bin/env python3

import core.Config

class IndentWriter(object):
    def __init__(self, outfile):
        self.outfile = outfile
        self.at_first_column = True
        self.indent = 0

    def write(self, text):
        if self.at_first_column:
            self.outfile.write(u'    '*self.indent)
            self.at_first_column = False
        self.outfile.write(text)
