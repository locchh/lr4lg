# Generated from CodeGen.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CodeGenParser import CodeGenParser
else:
    from CodeGenParser import CodeGenParser

# This class defines a complete generic visitor for a parse tree produced by CodeGenParser.

class CodeGenVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CodeGenParser#codeSpec.
    def visitCodeSpec(self, ctx:CodeGenParser.CodeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeGenParser#functionName.
    def visitFunctionName(self, ctx:CodeGenParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeGenParser#paramList.
    def visitParamList(self, ctx:CodeGenParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeGenParser#param.
    def visitParam(self, ctx:CodeGenParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CodeGenParser#functionPurpose.
    def visitFunctionPurpose(self, ctx:CodeGenParser.FunctionPurposeContext):
        return self.visitChildren(ctx)



del CodeGenParser