# Generated from parser/Cobol/Cobol.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,56,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,27,8,2,10,
        2,12,2,30,9,2,1,2,1,2,1,3,1,3,5,3,36,8,3,10,3,12,3,39,9,3,1,4,1,
        4,5,4,43,8,4,10,4,12,4,46,9,4,1,4,1,4,1,5,4,5,51,8,5,11,5,12,5,52,
        1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,5,1,0,34,34,2,0,65,90,
        97,122,3,0,48,57,65,90,97,122,2,0,10,10,13,13,3,0,9,10,13,13,32,
        32,59,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,1,13,1,0,0,0,3,16,1,0,0,0,5,24,1,0,0,0,7,33,1,0,0,
        0,9,40,1,0,0,0,11,50,1,0,0,0,13,14,5,73,0,0,14,15,5,83,0,0,15,2,
        1,0,0,0,16,17,5,68,0,0,17,18,5,73,0,0,18,19,5,83,0,0,19,20,5,80,
        0,0,20,21,5,76,0,0,21,22,5,65,0,0,22,23,5,89,0,0,23,4,1,0,0,0,24,
        28,5,34,0,0,25,27,8,0,0,0,26,25,1,0,0,0,27,30,1,0,0,0,28,26,1,0,
        0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,28,1,0,0,0,31,32,5,34,0,0,32,
        6,1,0,0,0,33,37,7,1,0,0,34,36,7,2,0,0,35,34,1,0,0,0,36,39,1,0,0,
        0,37,35,1,0,0,0,37,38,1,0,0,0,38,8,1,0,0,0,39,37,1,0,0,0,40,44,5,
        124,0,0,41,43,8,3,0,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,
        44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,6,4,0,0,48,10,1,
        0,0,0,49,51,7,4,0,0,50,49,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,
        53,1,0,0,0,53,54,1,0,0,0,54,55,6,5,0,0,55,12,1,0,0,0,5,0,28,37,44,
        52,1,6,0,0
    ]

class CobolLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    STRING_LITERAL = 3
    ID = 4
    COMMENT = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'IS'", "'DISPLAY'" ]

    symbolicNames = [ "<INVALID>",
            "STRING_LITERAL", "ID", "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "STRING_LITERAL", "ID", "COMMENT", "WS" ]

    grammarFileName = "Cobol.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


