grammar Cobol;

program
    : identifier 'IS' statement EOF
    ;

statement
    : displayStatement
    ;

displayStatement
    : 'DISPLAY' STRING_LITERAL
    ;

identifier
    : ID
    ;

STRING_LITERAL
    : '"' (~["])* '"'
    ;

ID
    : [a-zA-Z] [a-zA-Z0-9]*
    ;

COMMENT
    : '|' ~[\r\n]* -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
