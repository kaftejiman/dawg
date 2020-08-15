#!/usr/bin/env python3

from core.Tokens import *
import core.Config


def string_escape(s, encoding='utf-8'):
    return (s.encode('latin1')
             .decode('unicode-escape')
             .encode('latin1')
             .decode(encoding))

def t_ASSIGN(t):
    r'B+E*[ ]*L+I+K+E+[ ]*A*\b'
    return OP(t, "=")


def t_SINGLE_QUOTE_STRING(t):
    r"'([^\\']+|\\'|\\\\)*'"
    t.type = "STRING"
    t.value = string_escape(t.value[1:-1])
    return t


def t_DOUBLE_QUOTE_STRING(t):
    r'"([^\\"]+|\\"|\\\\)*"'
    t.type = "STRING"
    t.value = string_escape(t.value[1:-1])
    return t


def t_MULTILINE_COMMENT(t):
    r"L+(I+|Y+)K+E+[ ]*((?!N+D*S+H+I+T+).|\n)*[ ]*(N+D*S+H+I+T+)\b"
    t.type = "MULTILINECOMMENT"
    t.value = t.value[4:-5].strip(" ")
    return t


def t_LSQUARE(t):
    r"(O+F+|F+R+O+M+|B+(A+|U+)N+C+H+[ ]*O*)"
    t.lexer.paren_stack.append(']')
    return OP(t, "[")


def t_LPAREN(t):
    r"((D+(O+|E+|I+)(Z+E*|S+)|T+H+O*(S+|Z+)E*|T+H+I+S+|T+H+E*(S+|Z+)E*)|A+S+|A+Z+|A+L+O+N+G+|U+(S+|Z+)I*N+G*)"
    t.lexer.paren_stack.append(')')
    return OP(t, "(")


def t_LBRACE(t):
    r"(?:(B+A+G+|J+O*N+X+|G+U+N+(S+|Z+)))[ ]*O*\b"
    t.lexer.paren_stack.append('}')
    return OP(t, '{')


def t_CLOSE(t):
    r"(?:Y+O+)\b"
    stack = t.lexer.paren_stack
    num_closes = t.value.count('O')
    if len(stack) < num_closes:
        raise AssertionError("not enough opens on the stack: line %d"
                             % (t.lineno,))
    t.value = "".join(stack[-num_closes:][::-1])
    del stack[-num_closes:]
    return t


def t_EQ(t):
    r"S+T+E+A*D+(Y+|I+)[ ]+(L+I+K+E+)*\b"
    return OP(t, "==")


def t_NE(t):
    r"(A+I+N+(O+|T+))\b"
    return OP(t, "!=")


def t_GT(t):
    r"T+H+I+(C+|K+)(A*(?:H+)*|(?:ER+)*)*\b"
    return OP(t, ">")


def t_LT(t):
    r"TIGHT(?:A+(?:H+)*|(?:ER+))*|THIGHT(A*(?:H+)*|(?:ER+)*)*\b"
    return OP(t, "<")


def t_GTE(t):
    r"(I+(S+|Z+))*[ ]*B+I+G+[ ]*A+(S+|Z+)\b"
    return OP(t, ">=")


def t_LTE(t):
    r"(TIGHT(?:A+(?:H+)*|(?:ER+))*|THIGHT(A*(?:H+)*|(?:ER+)*)*)[ ]+LIKE\b"
    return OP(t, "<=")


def t_RETURN(t):
    r"(H+I*T+)[ ]*((D+|T+H+)*E*M+)*\b"
    return RESERVED(t, "return")


def t_yield(t):
    r"S+P+I+T+([ ]*(D+(O+|E+|I+)(Z+E*|S+)|THOSE|THESE|THIS)|)*\b"
    return RESERVED(t, "yield")


def t_IF(t):
    r"(((W+H+A+T+)[ ]*I+F+)|S+P+O+(S+|Z+)E*|W+H+A+T+[ ]*(T+H+E+|D+(E+|A+))[ ]*D+I+L+Y+[ ]*(YO)*)\b"
    return RESERVED(t, "if")


def t_ELIF(t):
    r"T+H+O+(U*G+H+)*[ ]+\b"
    return RESERVED(t, "elif")


def t_ELSE(t):
    r"D+A+(Y+U*)*M+[ ]*(S+(O+|U+)N+)*\b"
    return RESERVED(t, "else")


def t_COLON(t):
    r"((T+O+[ ]+T+H+(A+|E+))|(T*I+L+)|H+O+L+D+A*(\?+|[ ]+\?+)|L+I+K+E*|(F+O+R*R*E+A*L+|R+E+A+L+[ ]*T+A+L+K+)[ ]*(L+I+K+E*)*)|D+O+\b"
    t.value = ":"
    return t


def t_FROM(t):
    r"G+R+A*B+[ ]+((D+|T+H+)*E*M+)*\b"
    return RESERVED(t, "from")


def t_EXCEPT(t):
    r"S+H+E*I*T+\b"
    return RESERVED(t, "except")


def t_PLUS(t):
    r"P+I+M+P+(I+N+G*)*\b"
    return OP(t, "+")


def t_MINUS(t):
    r"B+A+N+G+(I+N+G*)*\b"
    return OP(t, "-")


def t_PLUS_EQUAL(t):
    r"(G+A+N+G+)[ ]*P+I+M+P+(I+N+G*)*\b"
    return OP(t, "+=")


def t_MINUS_EQUAL(t):
    r"(G+A+N+G+)[ ]*B+A+N+G+(I+N+G*)*\b"
    return OP(t, "-=")


def t_DIV(t):
    r"J+A+H*C*K+\b"
    return OP(t, "/")


def t_EMPTYSET(t):
    r"(R+E*A*D+(Y+|I+)|G+O+)\b"
    return INLINE(t, "()")


def t_DIV_EQUAL(t):
    r"(G+A+N+G+)[ ]*J+A+H*C*K+\b"
    return OP(t, "/=")


def t_TRUEDIV(t):
    r"N+(E+A+|I+)T+[ ]*J+A+H*C*K+\b"
    return OP(t, "//")


def t_MUL(t):
    r"B+U*M+P+(I*N*G*)*\b"
    return OP(t, "*")


def t_MUL_EQUAL(t):
    r"(G+A+N+G+)[ ]*B+U*M+P+(I*N*G*)*\b"
    return OP(t, "*=")


def t_POW(t):
    r"R+A*I+(S|Z)+E*\b"
    return OP(t, "**")


def t_IN(t):
    r"(I+N+|A(S|Z)[ ]*O+N+E+[ ]*O+F*[ ]*(D+(O+|E+|I+)(Z+E*|S+)))\b"
    return OP(t, "in")


def t_del(t):
    r"D+I+S+I+N+G*\b"
    return RESERVED(t, "del")


def t_and(t):
    r"W+I+F+\b"
    return RESERVED(t, "and")


def t_or(t):
    r"O+R+\b"
    return RESERVED(t, "or")


def t_pass(t):
    r"B+U+L+S+H+(I+|E+)T\b"
    return RESERVED(t, "pass")


def t_forever(t):
    r"F+O+R*G+(O+|U+)D+([ ]*)*\b"
    return INLINE(t, "while 1")


def t_def(t):
    r"(F+I+T+I+N+G*[ ]*((D+(O+|E+|I+)(Z+E*|S+)|THOSE|THESE|THIS|((D+|T+H+)*E*M+)))|O+P+E+R+A+(T+I+|S+H+(Y+|I+)*)O+N+)\b"
    return RESERVED(t, "def")


def t_class(t):
    r"L+E*V+E*L+\b"
    return RESERVED(t, "class")


def t_future(t):
    r"F+U+T+U+R+E*([ ]+W*I*F*)*\b"
    t.type = "FUTURE"
    return t


def t_assert(t):
    r"S+[ ]*C+O+L+\b"
    return RESERVED(t, "assert")


def t_assert_not(t):
    r"A+I+N+T*[ ]*C+O+L+\b"
    return INLINE(t, "assert not ")


def t_for(t):
    r"A+L+[ ]*(D+(O+|E+|I+)(Z+E*|S+)|THOSE|THESE|THIS)[ ]*M+O+F+O+S*[ ]*\b"
    return RESERVED(t, "for")


def t_list(t):
    r"T+U+P+L+E+\b"
    return AUTOCALL(t, "tuple")


def t_print(t):
    r"(B+L+I*N+G*[ ]*B+L+I*N+G*|S+H+O+W*T+I+M+E*|(S+H+O+W*(O+F+)*))\b"
    return RESERVED(t, "print")


def t_print_empty_line(t):
    r"A+H*[ ]*B+E*[ ]*B+A+D+"
    return INLINE(t, "print('\\n') ")

#def t_read(t):
#    r"(G+I+M+E+[ ]*(D+(O+|E+|I+)(Z+E*|S+)|THOSE|THESE))\b"
#    return AUTOCALL(t, "raw_input")


RESERVED_VALUES = {
    "NONE": ("NAME", "None"),
    "NOTHIN": ("NUMBER", "0"),
    "THEONE": ("NUMBER", "1"),
    "FITTY": ("NUMBER", "50"),
    "ONE": ("NUMBER", "1"),
    "TWO": ("NUMBER", "2"),
    "TWICE": ("NUMBER", "2"),
    "THREE": ("NUMBER", "3"),
    "TREE": ("NUMBER", "3"),
    "FOUR": ("NUMBER", "4"),
    "FOR": ("NUMBER", "4"),
    "FIVE": ("NUMBER", "5"),
    "SIKS": ("NUMBER", "6"),
    "SEVEN": ("NUMBER", "7"),
    "ATE": ("NUMBER", "8"),
    "NINE": ("NUMBER", "9"),
    "TEN": ("NUMBER", "10"),
    "FITTY": ("NUMBER", "50"),
    "SIXSIXSIX": ("NUMBER", "666"),
    "HELLNO": ("NAME", "False"),
    "HELLYEAH": ("NAME", "True"),
    "ND": ("OP", ","),
    "TWIST": ("OP", "-"),
    "BRING": ("RESERVED", "import"),
    "AS": ("RESERVED", "as"),
    "OWN": ("OP", "."),
    "LEMME": ("RESERVED", "try"),
    "DAFUQ": ("RESERVED", "raise"),
    "WHATEVER": ("RESERVED", "finally"),
    "HOLDA": ("RESERVED", "except"),
    "AIGHT": ("RESERVED", "continue"),
    "FUCKDAT": ("RESERVED", "break"),
    "OVER": ("OP", "/"),
    "BAIL": ("RESERVED", "not"),
    "MASELF": ("RESERVED", "self"),
    "STRING": ("AUTOCALL", "str"),
    "NUMBAH": ("AUTOCALL", "int"),
    "SIZE": ("AUTOCALL", "len"),
    "NUMBAHZ": ("AUTOCALL", "range"),
    "GLUE": ("AUTOCALL", ".append"),
    "EVERY": ("AUTOCALL", "iter"),
    "OPTIONS": ("INLINE", "argv_"),
    "MY": ("INLINE", "self."),
    "POINT": ("INLINE", "."),
    "MYSELF": ("INLINE", "(self)"),
    "EVEN": ("INLINE", "% 2 == 0"),
    "ODD": ("INLINE", "% 2 == 1"),
    "LEVELUP": ("INLINE", "+= 1"),
    "BEHUMBLE": ("INLINE", "-= 1"),
    "WITHNEWLINE": ("INLINE", "+ \'\\n\'"),
    "NEWLINE": ("INLINE", "\'\\n\'"),
    "WITH": ("RESERVED", "with"),
    "IS": ("RESERVED", "is"),
    "GIMME": ("AUTOCALL", "input"),
}


def t_FLOAT(t):
    r"""(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]? \d+)?"""
    t.value = t.value
    t.type = "NUMBER"
    return t


def t_INT(t):
    r"\d+"
    t.type = "NUMBER"
    return t


def t_COMMENT(t):
    r"(?:C+H+I+L+[ ]*(A+H+)*|M+A+R+I+N+A+T+E+)[^\n]*"
    return t


def t_FILLERS(t):
    r"(L+I+L+)*[ ]*(B+O+(I+|Y+)|P+U+S+(Y+|I+)|H+O+M+(I+|Y+)E*|M+(Y+|A+)[ ]*M+(A+|E+)N+|(Y*O*U+)*[ ]*K*N+O+W*[ ]*(W+H*A+T+)[ ]*I*[ ]*A*M+[ ]*S+(A+|E+)Y+I+N+G*|(Y*O*U+)*[ ]*F+E+L+I+N+G*[ ]*M+E+)|L+O+K|B+R+O+|D+(E+|A+)\b"
    if core.Config.DEBUG:
        print("\n[DEBUG] Skipping filler", repr(t.value[0]))
    t.type = "FILLER"
    return t


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in RESERVED_VALUES:
        type, value = RESERVED_VALUES[t.value]
        t.type = type
        t.value = value
        if t.type == "AUTOCALL":
            t.lexer.paren_stack.append(")")
    return t


def t_WS(t):
    r'([ ]+|\t)'
    if t.lexer.at_line_start and not t.lexer.paren_stack:
        return t


def t_newline(t):
    r'(\n+)'
    t.lexer.lineno += len(t.value)
    t.type = "NEWLINE"
    if not t.lexer.paren_stack:
        return t


def t_error(t):
    raise SyntaxError("Unknown symbol %r" % (t.value[0],))
    print("Skipping", repr(t.value[0]))
    t.lexer.skip(1)

