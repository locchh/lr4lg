# Generated from CodeGen.g4 by ANTLR 4.13.2
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
        4,1,7,32,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,9,2,1,3,
        1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,27,0,10,1,0,0,0,2,17,1,0,0,0,
        4,19,1,0,0,0,6,27,1,0,0,0,8,29,1,0,0,0,10,11,5,1,0,0,11,12,3,2,1,
        0,12,13,5,2,0,0,13,14,3,4,2,0,14,15,5,3,0,0,15,16,3,8,4,0,16,1,1,
        0,0,0,17,18,5,5,0,0,18,3,1,0,0,0,19,24,3,6,3,0,20,21,5,4,0,0,21,
        23,3,6,3,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,
        0,25,5,1,0,0,0,26,24,1,0,0,0,27,28,5,5,0,0,28,7,1,0,0,0,29,30,5,
        6,0,0,30,9,1,0,0,0,1,24
    ]

class CodeGenParser ( Parser ):

    grammarFileName = "CodeGen.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Create a function'", "'with parameters'", 
                     "'that'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "STRING", "WS" ]

    RULE_codeSpec = 0
    RULE_functionName = 1
    RULE_paramList = 2
    RULE_param = 3
    RULE_functionPurpose = 4

    ruleNames =  [ "codeSpec", "functionName", "paramList", "param", "functionPurpose" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ID=5
    STRING=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CodeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionName(self):
            return self.getTypedRuleContext(CodeGenParser.FunctionNameContext,0)


        def paramList(self):
            return self.getTypedRuleContext(CodeGenParser.ParamListContext,0)


        def functionPurpose(self):
            return self.getTypedRuleContext(CodeGenParser.FunctionPurposeContext,0)


        def getRuleIndex(self):
            return CodeGenParser.RULE_codeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeSpec" ):
                listener.enterCodeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeSpec" ):
                listener.exitCodeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCodeSpec" ):
                return visitor.visitCodeSpec(self)
            else:
                return visitor.visitChildren(self)




    def codeSpec(self):

        localctx = CodeGenParser.CodeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_codeSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(CodeGenParser.T__0)
            self.state = 11
            self.functionName()
            self.state = 12
            self.match(CodeGenParser.T__1)
            self.state = 13
            self.paramList()
            self.state = 14
            self.match(CodeGenParser.T__2)
            self.state = 15
            self.functionPurpose()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CodeGenParser.ID, 0)

        def getRuleIndex(self):
            return CodeGenParser.RULE_functionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionName" ):
                listener.enterFunctionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionName" ):
                listener.exitFunctionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionName" ):
                return visitor.visitFunctionName(self)
            else:
                return visitor.visitChildren(self)




    def functionName(self):

        localctx = CodeGenParser.FunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(CodeGenParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CodeGenParser.ParamContext)
            else:
                return self.getTypedRuleContext(CodeGenParser.ParamContext,i)


        def getRuleIndex(self):
            return CodeGenParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = CodeGenParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.param()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 20
                self.match(CodeGenParser.T__3)
                self.state = 21
                self.param()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CodeGenParser.ID, 0)

        def getRuleIndex(self):
            return CodeGenParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CodeGenParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(CodeGenParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionPurposeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CodeGenParser.STRING, 0)

        def getRuleIndex(self):
            return CodeGenParser.RULE_functionPurpose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionPurpose" ):
                listener.enterFunctionPurpose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionPurpose" ):
                listener.exitFunctionPurpose(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionPurpose" ):
                return visitor.visitFunctionPurpose(self)
            else:
                return visitor.visitChildren(self)




    def functionPurpose(self):

        localctx = CodeGenParser.FunctionPurposeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionPurpose)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(CodeGenParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





