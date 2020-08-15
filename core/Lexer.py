#!/usr/bin/env python3

from ply import *
from core.Tokens import *
from core.Mappings import *
import core.Config
import logging

class Lexer(object):
    def __init__(self, debug=0, reflags=0):
        self.lexer = lex.lex(debug=debug, reflags=reflags)
        self.token_stream = None

    def input(self, s, add_endmarker=True):
        self.lexer.paren_stack = []
        self.lexer.input(s)
        self.token_stream = token_filter(self.lexer, add_endmarker)

    def token(self):
        try:
            return self.token_stream.next()
        except StopIteration:
            return None

def token_filter(lexer, add_endmarker=True):
    token = None
    tokens = iter(lexer.token, None)
    tokens = track_tokens_filter(lexer, tokens)
    for token in indentation_filter(tokens):
        yield token

    if add_endmarker:
        lineno = 1
        if token is not None:
            lineno = token.lineno
        yield _new_token("ENDMARKER", lineno)


NO_INDENT = 0
MAY_INDENT = 1
MUST_INDENT = 2


def track_tokens_filter(lexer, tokens):
    lexer.at_line_start = at_line_start = True
    indent = NO_INDENT
    for token in tokens:
        token.at_line_start = at_line_start

        if token.type == "COLON":
            at_line_start = False
            indent = MAY_INDENT
            token.must_indent = False

        elif token.type == "NEWLINE":
            at_line_start = True
            if indent == MAY_INDENT:
                indent = MUST_INDENT
            token.must_indent = False

        elif token.type == "WS":
            assert token.at_line_start == True
            at_line_start = True
            token.must_indent = False

        elif token.type == "COMMENT":
            pass

        else:
            if indent == MUST_INDENT:
                token.must_indent = True
            else:
                token.must_indent = False
            at_line_start = False

            indent = NO_INDENT

        yield token
        lexer.at_line_start = at_line_start

def DEDENT(lineno):
    return _new_token("DEDENT", lineno)


def INDENT(lineno):
    return _new_token("INDENT", lineno)


def indentation_filter(tokens):
    levels = [0]
    token = None
    depth = 0
    prev_was_ws = False
    if core.Config.DEBUG:
        print("\n[DEBUG]")
    for token in tokens:
        if core.Config.DEBUG:
            print("Process", token)
            if token.at_line_start:
                print("at_line_start")
            if hasattr(token,'must_indent'):
                print("must_indent")
            print
        if token.type == "WS":
            assert depth == 0
            depth = len(token.value)
            prev_was_ws = True
            continue

        if token.type == "NEWLINE":
            depth = 0
            if prev_was_ws or token.at_line_start:
                continue
            yield token
            continue

        if token.type == "COMMENT":
            yield token
            continue

        prev_was_ws = False
        if token.must_indent:
            if not (depth > levels[-1]):
                raise IndentationError("expected an indented block")

            levels.append(depth)
            yield INDENT(token.lineno)

        elif token.at_line_start:
            if depth == levels[-1]:
                pass
            elif depth > levels[-1]:
                print(depth)
                print(levels[-1])
                raise IndentationError(
                    "indentation increase but not in new block")
            else:
                try:
                    i = levels.index(depth)
                except ValueError:
                    raise IndentationError("inconsistent indentation")
                for _ in range(i+1, len(levels)):
                    yield DEDENT(token.lineno)
                    levels.pop()

        yield token

    if len(levels) > 1:
        assert token is not None
        for _ in range(1, len(levels)):
            yield DEDENT(token.lineno)

def _new_token(type, lineno):
    tok = lex.LexToken()
    tok.type = type
    tok.value = None
    tok.lineno = lineno
    tok.lexpos = -1
    return tok

