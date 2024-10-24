# Generated from parser/Cobol/Cobol.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,21,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,1,
        1,1,1,2,1,2,1,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,16,0,8,1,0,0,0,2,13,
        1,0,0,0,4,15,1,0,0,0,6,18,1,0,0,0,8,9,3,6,3,0,9,10,5,1,0,0,10,11,
        3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,3,4,2,0,14,3,1,0,0,0,15,
        16,5,2,0,0,16,17,5,3,0,0,17,5,1,0,0,0,18,19,5,4,0,0,19,7,1,0,0,0,
        0
    ]

class CobolParser ( Parser ):

    grammarFileName = "Cobol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'IS'", "'DISPLAY'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "STRING_LITERAL", 
                      "ID", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_displayStatement = 2
    RULE_identifier = 3

    ruleNames =  [ "program", "statement", "displayStatement", "identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    STRING_LITERAL=3
    ID=4
    COMMENT=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CobolParser.IdentifierContext,0)


        def statement(self):
            return self.getTypedRuleContext(CobolParser.StatementContext,0)


        def EOF(self):
            return self.getToken(CobolParser.EOF, 0)

        def getRuleIndex(self):
            return CobolParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CobolParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.identifier()
            self.state = 9
            self.match(CobolParser.T__0)
            self.state = 10
            self.statement()
            self.state = 11
            self.match(CobolParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def displayStatement(self):
            return self.getTypedRuleContext(CobolParser.DisplayStatementContext,0)


        def getRuleIndex(self):
            return CobolParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CobolParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.displayStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(CobolParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return CobolParser.RULE_displayStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayStatement" ):
                listener.enterDisplayStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayStatement" ):
                listener.exitDisplayStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayStatement" ):
                return visitor.visitDisplayStatement(self)
            else:
                return visitor.visitChildren(self)




    def displayStatement(self):

        localctx = CobolParser.DisplayStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_displayStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(CobolParser.T__1)
            self.state = 16
            self.match(CobolParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CobolParser.ID, 0)

        def getRuleIndex(self):
            return CobolParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = CobolParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(CobolParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





