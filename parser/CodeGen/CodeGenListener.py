# Generated from CodeGen.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CodeGenParser import CodeGenParser
else:
    from CodeGenParser import CodeGenParser

# This class defines a complete listener for a parse tree produced by CodeGenParser.
class CodeGenListener(ParseTreeListener):

    # Enter a parse tree produced by CodeGenParser#codeSpec.
    def enterCodeSpec(self, ctx:CodeGenParser.CodeSpecContext):
        pass

    # Exit a parse tree produced by CodeGenParser#codeSpec.
    def exitCodeSpec(self, ctx:CodeGenParser.CodeSpecContext):
        pass


    # Enter a parse tree produced by CodeGenParser#functionName.
    def enterFunctionName(self, ctx:CodeGenParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by CodeGenParser#functionName.
    def exitFunctionName(self, ctx:CodeGenParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by CodeGenParser#paramList.
    def enterParamList(self, ctx:CodeGenParser.ParamListContext):
        pass

    # Exit a parse tree produced by CodeGenParser#paramList.
    def exitParamList(self, ctx:CodeGenParser.ParamListContext):
        pass


    # Enter a parse tree produced by CodeGenParser#param.
    def enterParam(self, ctx:CodeGenParser.ParamContext):
        pass

    # Exit a parse tree produced by CodeGenParser#param.
    def exitParam(self, ctx:CodeGenParser.ParamContext):
        pass


    # Enter a parse tree produced by CodeGenParser#functionPurpose.
    def enterFunctionPurpose(self, ctx:CodeGenParser.FunctionPurposeContext):
        pass

    # Exit a parse tree produced by CodeGenParser#functionPurpose.
    def exitFunctionPurpose(self, ctx:CodeGenParser.FunctionPurposeContext):
        pass



del CodeGenParser