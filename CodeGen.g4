// CodeGen.g4
grammar CodeGen;

// Entry rule for parsing the high-level description
codeSpec : 'Create a function' functionName 'with parameters' paramList 'that' functionPurpose;

// Function name rule
functionName : ID;

// Parameters list rule (comma-separated)
paramList : param (',' param)*;

// Single parameter rule
param : ID;

// Function purpose rule (a string describing what the function does)
functionPurpose : STRING;

// Lexer rules
ID : [a-zA-Z_][a-zA-Z_0-9]*;
STRING : '"' (~["])* '"';
WS : [ \t\r\n]+ -> skip;