# Generated from parser/Cobol/Cobol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CobolParser import CobolParser
else:
    from CobolParser import CobolParser

# This class defines a complete listener for a parse tree produced by CobolParser.
class CobolListener(ParseTreeListener):

    # Enter a parse tree produced by CobolParser#program.
    def enterProgram(self, ctx:CobolParser.ProgramContext):
        pass

    # Exit a parse tree produced by CobolParser#program.
    def exitProgram(self, ctx:CobolParser.ProgramContext):
        pass


    # Enter a parse tree produced by CobolParser#statement.
    def enterStatement(self, ctx:CobolParser.StatementContext):
        pass

    # Exit a parse tree produced by CobolParser#statement.
    def exitStatement(self, ctx:CobolParser.StatementContext):
        pass


    # Enter a parse tree produced by CobolParser#displayStatement.
    def enterDisplayStatement(self, ctx:CobolParser.DisplayStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#displayStatement.
    def exitDisplayStatement(self, ctx:CobolParser.DisplayStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#identifier.
    def enterIdentifier(self, ctx:CobolParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CobolParser#identifier.
    def exitIdentifier(self, ctx:CobolParser.IdentifierContext):
        pass



del CobolParser