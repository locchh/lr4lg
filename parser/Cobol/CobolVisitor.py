# Generated from parser/Cobol/Cobol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CobolParser import CobolParser
else:
    from CobolParser import CobolParser

# This class defines a complete generic visitor for a parse tree produced by CobolParser.

class CobolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CobolParser#program.
    def visitProgram(self, ctx:CobolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#statement.
    def visitStatement(self, ctx:CobolParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#displayStatement.
    def visitDisplayStatement(self, ctx:CobolParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#identifier.
    def visitIdentifier(self, ctx:CobolParser.IdentifierContext):
        return self.visitChildren(ctx)



del CobolParser