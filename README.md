# Dawg: Python for thugs[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
For thugs that like to code.

<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Description</a></li>
<li><a href="#sec-2">2. Using Dawg</a>
<ul>
<li><a href="#sec-2-1">2.1. Run Dawg program</a></li>
<li><a href="#sec-2-2">2.2. Run or Convert Dawg program with Debug mode</a></li>
<li><a href="#sec-2-3">2.3. Convert Dawg program to Python equivalent</a></li>
<li><a href="#sec-2-4">2.4. Convert multiple Dawg programs to Python equivalent</a></li>
</ul>
</li>
<li><a href="#sec-3">3. Syntax</a></li>
<li><a href="#sec-4">4. Examples</a></li>
<li><a href="#sec-5">5. Grammar</a></li>
<li><a href="#sec-6">6. Implementation</a></li>
<li><a href="#sec-7">7. Notes</a></li>
</ul>
</div>
</div>

# Description<a id="sec-1" name="sec-1"></a>

Aye, holda! You didnt choose the thug life but the thug life chose you? You also like to code?
 
Look no mo' you made it.
Dawg is your fella, an implementation of a Python dialect that feels you and follows your orders.

Some would even say dats a dime, I wouldnt disagree.

# Using Dawg<a id="sec-2" name="sec-2"></a>

Dawg is a Python3 program.

Install dependencies: 

```
pip3 install -r requirements.txt
```

## Run Dawg program<a id="sec-2-1" name="sec-2-1"></a>

```
$ ./dawg example.dawg
SUP?
```

## Run or Convert Dawg program with Debug mode<a id="sec-2-2" name="sec-2-2"></a>

Use (-d or &#x2013;debug) flag for enabling debug mode.
```
$ ./dawg -d example.dawg

[DEBUG]
argv: {'--argument': [],
 '--convert': False,
 '--debug': True,
 '--help': False,
 '--interact': False,
 '--version': False,
 '<filename>': ['example.dawg']}

[DEBUG]
Process LexToken(COMMENT,'CHILL DUMMY EXAMPLE',1,0)
at_line_start
Process LexToken(NEWLINE,'\n',1,19)
at_line_start
must_indent
Process LexToken(RESERVED,'print',2,20)
at_line_start
must_indent
Process LexToken(OP,'(',2,32)
must_indent
Process LexToken(STRING,'SUP?',2,37)
must_indent
Process LexToken(CLOSE,')',2,44)
must_indent
Process LexToken(NEWLINE,'\n',2,46)
must_indent

[DEBUG] Converted code:

import sys as _sys
#LL DUMMY EXAMPLE
print ( 'SUP?' )


SUP?
```

## Convert Dawg program to Python equivalent<a id="sec-2-3" name="sec-2-3"></a>

Use (-c or &#x2013;convert) flag for conversion of Dawg code to the equivalent Python code
the resulting Python code will be available in converted folder.

```$ ./dawg -c example.dawg```

## Convert multiple Dawg programs to Python equivalent<a id="sec-2-4" name="sec-2-4"></a>

Use (-c or &#x2013;convert) flag for conversion of Dawg code to the equivalent Python code
the resulting Python code will be available in converted folder.

```$ ./dawg --convert example1.dawg example2.dawg```

# Syntax<a id="sec-3" name="sec-3"></a>

Most of Python is supported by Dawg but not everything, it should be enough to get your feet wet bro, check Grammar and Implementation sections fo mo details.
Most of da syntax is spelling mistake proof to a certain degree, for instance character repetition is supported.

**Variable assignment:**

```FINGERS BEE LIIKE TEN```

-> Python equivalent:

```FINGERS = 10```

**Print message onto the screen:**

```BLING BLING THIS "SUP" YO```

-> Python equivalent:

```print("SUP")```

**Read from user:**

```TYRONE BE LIKE GIMME 'WHOS IN DA CLUB? ' YO```

-> Python equivalent:

```TYRONE = input('WHOS IN DA CLUB? ')```


**Function definition:**


```
OPERASHYON GREETINGS READY LIKE
    BLING BLING THIS "AYE SUP" YO
    HIT DEM HOMIE
```

-> Python equivalent:

```
def GREETINGS(): 
    print("AYE SUP?")
    return
```

**Arithmetic operations:**

```
DOUBLEG BE LIKE SIKS BRO
DOUBLEG GANGBUMPIN DOUBLEG BRO
DOUBLEH BE LIKE TWO
DOUBLEH GANGBANG DOUBLEH HOMIE
S COOL DOUBLEG STEADY LIKE 36
S COOL DOUBLEH STEADY LIKE NOTHIN
```


-> Python equivalent:

```
DOUBLEG = 6
DOUBLEG \*= DOUBLEG
DOUBLEH = 2
DOUBLEH -= DOUBLEH
assert DOUBLEG `= 36
assert DOUBLEH =` 0
```

**Iterations:**

```
NUMBZ BE LIKE BANCH O X LOOK ALL DIZ MOFOS X IN NUMBAHZ FITTY YOO
BLING BLING THESE NUMBZ YO
```

-> Python equivalent:

```
NUMBZ = [ X for X in range(50 )]
print ( NUMBZ )
```
**Fillers:**

For your entertainment, filler words that serves nothing, use them anywhere you please.

```LIL BOI SAM BE LIKE 'EYY YO ' HOMIE PIMPIN 'WHAT UP?' YOU KNOW WHAT AM SAYINNN```

-> Python equivalent:

```SAM = 'EYY YO ' + 'WHAT UP?'```

# Examples<a id="sec-4" name="sec-4"></a>

**Fibonacci number generator (examples/fib.dawg):**

```
$ ./dawg examples/fib.dawg --argument 1000
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
```

**Math operations (examples/meth.dawg):

```
$ ./dawg examples/meth.dawg
('PI BE LIKE', 3.141592653589793) ('EULA IS HELLA', 2.718281828459045)
300
DOUBLEG LEVELD UP ATE TIMES YO 308
```

**Python division brought from the future:**

```
$ ./dawg examples/future.dawg
50.0
```

an mo examples in examples foldah.

# Grammar<a id="sec-5" name="sec-5"></a>
todo

# Implementation<a id="sec-6" name="sec-6"></a>
todo

# Notes<a id="sec-7" name="sec-7"></a>
todo
