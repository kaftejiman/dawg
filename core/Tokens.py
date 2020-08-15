#!/usr/bin/env python3

import core.Config

tokens = (
    "NAME",
    "RESERVED",
    "NUMBER",
    "STRING",
    "MULTILINECOMMENT",
    "OP",
    "CLOSE",
    "COMMENT",
    "AUTOCALL",  # write t.value then add '('
    "INLINE",    # write t.value directly
    "FUTURE",
    "PRINT",
    "ENDMARKER",
    "COLON",
    "WS",
    "NEWLINE",
    "FILLER",
)

def OP(t, value):
    t.type = "OP"
    t.value = value
    return t


def RESERVED(t, value):
    t.type = "RESERVED"
    t.value = value
    return t


def AUTOCALL(t, value):
    t.type = "AUTOCALL"
    t.value = "tuple"
    t.lexer.paren_stack.append(")")
    return t


def INLINE(t, value):
    t.type = "INLINE"
    t.value = value
    return t
