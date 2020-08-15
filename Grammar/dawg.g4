grammar dawg;

program
   : 'YO LISTEN TO MA FLOW' code_block 'WORD.'?
   ;

code_block
   : statement+
   ;

statement
   : loop
   | declaration
   | comment
   | print_block
   | if_block
   | input_block
   | func_decl
   | assignment
   | expression
   ;

loop
   : 'ALL DIS MOFOS BE LIKE YO' LABEL 'SO AM LIKE' expression code_block 'WE GOIN YO' LABEL
   ;

declaration
   : 'DEM' LABEL
   | 'DEM' LABEL 'BE LIKE' < value >
   ;

comment
   : 'YA KNOW LIKE' STRING
   | 'HE COME TELLIN ME YO' STRING 'CHILLAX HO'
   ;

print_block
   : 'BLING BLING' expression* ?
   ;

if_block
   : 'WHAT THE DILLY YO?' 'STRAIGHT' code_block 'WORD UP'
   | 'WHAT THE DILLY YO?' 'STRAIGHT' code_block else_if_block 'WORD UP'
   ;

else_if_block
   : 'THO' expression code_block else_if_block
   | 'DAYUM' code_block
   | 'THO' expression code_block
   ;

input_block
   : 'LOOKIN FO DEM' LABEL
   ;

func_decl
   : 'FITTIN' LABEL (('BE LIKE' LABEL) ('N EM' LABEL)*)? code_block 'OFF THA HOOK YO'
   ;

assignment
   : LABEL 'BE LIKE' expression
   ;

expression
   : equals
   | both
   | not_equals
   | greater
   | less
   | add
   | sub
   | mul
   | div
   | mod
   | cast
   | either
   | all
   | any
   | not
   | func
   | LABEL
   | ATOM
   ;

equals
   : 'STEADY' expression 'N' expression
   ;

not_equals
   : 'AIN NO' expression 'N' expression
   ;

both
   : 'REAL ONES' expression 'N' expression
   ;

either
   : 'HIP' expression 'N' expression
   ;

greater
   : 'HELLA THICK THO' expression 'N' expression
   ;

less
   : 'HELLA TIGHT THO' expression 'N' expression
   ;

add
   : 'PIMPIN' expression 'N' expression
   ;

sub
   : 'BANGIN' expression 'N' expression
   ;

mul
   : 'BALLER' expression 'N' expression
   ;

div
   : 'JACK' expression 'N' expression
   ;

mod
   : 'METH' expression 'N' expression
   ;

cast
   : 'BUSTA MOVE' expression 'BE' < type >
   ;

all
   : 'DEADASS' expression ('N' expression)* 'LIT?'
   ;

any
   : 'AYE' expression ('N' expression)* 'LIT?'
   ;

not
   : 'BAIL' expression
   ;

func
   : LABEL expression+ 'FOO'
   ;

LABEL
   : ('a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_')+
   ;

ATOM
   : 'S COOL'
   | 'YOU TRIPPIN BOY'
   | 'DATS HOOCHIE'
   | ('0' .. '9')+
   | ('0' .. '9')* '.' ('0' .. '9')*
   | STRING
   ;

STRING
   : '"' ('\'"' | ~ '"')* '"'
   ;

WS
   : [ \r\n] -> skip
   | 'YO'
   | 'HOMIE'
   | 'LIL BOY'
   | 'LIL PUSSY'
   | 'YOU FEELIN ME'
   | 'YOU FOLLO ME'
   | 'YOU KNOW WHAT AM SAYIN'
   | 'MOFO'
   | 'AH BE BAAAD'
   | 'BOI'
   | 'NAHMSAYIN'
   ;

