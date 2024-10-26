# Generated from parser/cobol85/Cobol85.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Cobol85Parser import Cobol85Parser
else:
    from Cobol85Parser import Cobol85Parser

# This class defines a complete listener for a parse tree produced by Cobol85Parser.
class CobolListener(ParseTreeListener):

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.business_rules = {}

    # Enter a parse tree produced by Cobol85Parser#procedureDivision.
    def enterProcedureDivision(self, ctx:Cobol85Parser.ProcedureDivisionContext):
        ctx_id =str( id(ctx))
        self.nodes.append({"id": "start", "data": {"label": "start"}})

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionUsingClause.
    def enterProcedureDivisionUsingClause(self, ctx:Cobol85Parser.ProcedureDivisionUsingClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionGivingClause.
    def enterProcedureDivisionGivingClause(self, ctx:Cobol85Parser.ProcedureDivisionGivingClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionUsingParameter.
    def enterProcedureDivisionUsingParameter(self, ctx:Cobol85Parser.ProcedureDivisionUsingParameterContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByReferencePhrase.
    def enterProcedureDivisionByReferencePhrase(self, ctx:Cobol85Parser.ProcedureDivisionByReferencePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByReference.
    def enterProcedureDivisionByReference(self, ctx:Cobol85Parser.ProcedureDivisionByReferenceContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByValuePhrase.
    def enterProcedureDivisionByValuePhrase(self, ctx:Cobol85Parser.ProcedureDivisionByValuePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByValue.
    def enterProcedureDivisionByValue(self, ctx:Cobol85Parser.ProcedureDivisionByValueContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureDeclaratives.
    def enterProcedureDeclaratives(self, ctx:Cobol85Parser.ProcedureDeclarativesContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureDeclarative.
    def enterProcedureDeclarative(self, ctx:Cobol85Parser.ProcedureDeclarativeContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureSectionHeader.
    def enterProcedureSectionHeader(self, ctx:Cobol85Parser.ProcedureSectionHeaderContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionBody.
    def enterProcedureDivisionBody(self, ctx:Cobol85Parser.ProcedureDivisionBodyContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureSection.
    def enterProcedureSection(self, ctx:Cobol85Parser.ProcedureSectionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#paragraphs.
    def enterParagraphs(self, ctx:Cobol85Parser.ParagraphsContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#paragraph.
    def enterParagraph(self, ctx:Cobol85Parser.ParagraphContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sentence.
    def enterSentence(self, ctx:Cobol85Parser.SentenceContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#statement.
    def enterStatement(self, ctx:Cobol85Parser.StatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#acceptStatement.
    def enterAcceptStatement(self, ctx:Cobol85Parser.AcceptStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#acceptFromDateStatement.
    def enterAcceptFromDateStatement(self, ctx:Cobol85Parser.AcceptFromDateStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#acceptFromMnemonicStatement.
    def enterAcceptFromMnemonicStatement(self, ctx:Cobol85Parser.AcceptFromMnemonicStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#acceptFromEscapeKeyStatement.
    def enterAcceptFromEscapeKeyStatement(self, ctx:Cobol85Parser.AcceptFromEscapeKeyStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#acceptMessageCountStatement.
    def enterAcceptMessageCountStatement(self, ctx:Cobol85Parser.AcceptMessageCountStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#addStatement.
    def enterAddStatement(self, ctx:Cobol85Parser.AddStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#addToStatement.
    def enterAddToStatement(self, ctx:Cobol85Parser.AddToStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#addToGivingStatement.
    def enterAddToGivingStatement(self, ctx:Cobol85Parser.AddToGivingStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#addCorrespondingStatement.
    def enterAddCorrespondingStatement(self, ctx:Cobol85Parser.AddCorrespondingStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#addFrom.
    def enterAddFrom(self, ctx:Cobol85Parser.AddFromContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#addTo.
    def enterAddTo(self, ctx:Cobol85Parser.AddToContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#addToGiving.
    def enterAddToGiving(self, ctx:Cobol85Parser.AddToGivingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})


    # Enter a parse tree produced by Cobol85Parser#addGiving.
    def enterAddGiving(self, ctx:Cobol85Parser.AddGivingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#alteredGoTo.
    def enterAlteredGoTo(self, ctx:Cobol85Parser.AlteredGoToContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#alterStatement.
    def enterAlterStatement(self, ctx:Cobol85Parser.AlterStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#alterProceedTo.
    def enterAlterProceedTo(self, ctx:Cobol85Parser.AlterProceedToContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callStatement.
    def enterCallStatement(self, ctx:Cobol85Parser.CallStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callUsingPhrase.
    def enterCallUsingPhrase(self, ctx:Cobol85Parser.CallUsingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callUsingParameter.
    def enterCallUsingParameter(self, ctx:Cobol85Parser.CallUsingParameterContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callByReferencePhrase.
    def enterCallByReferencePhrase(self, ctx:Cobol85Parser.CallByReferencePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callByReference.
    def enterCallByReference(self, ctx:Cobol85Parser.CallByReferenceContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callByValuePhrase.
    def enterCallByValuePhrase(self, ctx:Cobol85Parser.CallByValuePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callByValue.
    def enterCallByValue(self, ctx:Cobol85Parser.CallByValueContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callByContentPhrase.
    def enterCallByContentPhrase(self, ctx:Cobol85Parser.CallByContentPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callByContent.
    def enterCallByContent(self, ctx:Cobol85Parser.CallByContentContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#callGivingPhrase.
    def enterCallGivingPhrase(self, ctx:Cobol85Parser.CallGivingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#cancelStatement.
    def enterCancelStatement(self, ctx:Cobol85Parser.CancelStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#cancelCall.
    def enterCancelCall(self, ctx:Cobol85Parser.CancelCallContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#closeStatement.
    def enterCloseStatement(self, ctx:Cobol85Parser.CloseStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#closeFile.
    def enterCloseFile(self, ctx:Cobol85Parser.CloseFileContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#closeReelUnitStatement.
    def enterCloseReelUnitStatement(self, ctx:Cobol85Parser.CloseReelUnitStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#closeRelativeStatement.
    def enterCloseRelativeStatement(self, ctx:Cobol85Parser.CloseRelativeStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOStatement.
    def enterClosePortFileIOStatement(self, ctx:Cobol85Parser.ClosePortFileIOStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsing.
    def enterClosePortFileIOUsing(self, ctx:Cobol85Parser.ClosePortFileIOUsingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsingCloseDisposition.
    def enterClosePortFileIOUsingCloseDisposition(self, ctx:Cobol85Parser.ClosePortFileIOUsingCloseDispositionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsingAssociatedData.
    def enterClosePortFileIOUsingAssociatedData(self, ctx:Cobol85Parser.ClosePortFileIOUsingAssociatedDataContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsingAssociatedDataLength.
    def enterClosePortFileIOUsingAssociatedDataLength(self, ctx:Cobol85Parser.ClosePortFileIOUsingAssociatedDataLengthContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#computeStatement.
    def enterComputeStatement(self, ctx:Cobol85Parser.ComputeStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#computeStore.
    def enterComputeStore(self, ctx:Cobol85Parser.ComputeStoreContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#continueStatement.
    def enterContinueStatement(self, ctx:Cobol85Parser.ContinueStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#deleteStatement.
    def enterDeleteStatement(self, ctx:Cobol85Parser.DeleteStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#disableStatement.
    def enterDisableStatement(self, ctx:Cobol85Parser.DisableStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#displayStatement.
    def enterDisplayStatement(self, ctx:Cobol85Parser.DisplayStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#displayOperand.
    def enterDisplayOperand(self, ctx:Cobol85Parser.DisplayOperandContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#displayAt.
    def enterDisplayAt(self, ctx:Cobol85Parser.DisplayAtContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#displayUpon.
    def enterDisplayUpon(self, ctx:Cobol85Parser.DisplayUponContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#displayWith.
    def enterDisplayWith(self, ctx:Cobol85Parser.DisplayWithContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#divideStatement.
    def enterDivideStatement(self, ctx:Cobol85Parser.DivideStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#divideIntoStatement.
    def enterDivideIntoStatement(self, ctx:Cobol85Parser.DivideIntoStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#divideIntoGivingStatement.
    def enterDivideIntoGivingStatement(self, ctx:Cobol85Parser.DivideIntoGivingStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#divideByGivingStatement.
    def enterDivideByGivingStatement(self, ctx:Cobol85Parser.DivideByGivingStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#divideGivingPhrase.
    def enterDivideGivingPhrase(self, ctx:Cobol85Parser.DivideGivingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#divideInto.
    def enterDivideInto(self, ctx:Cobol85Parser.DivideIntoContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#divideGiving.
    def enterDivideGiving(self, ctx:Cobol85Parser.DivideGivingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#divideRemainder.
    def enterDivideRemainder(self, ctx:Cobol85Parser.DivideRemainderContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#enableStatement.
    def enterEnableStatement(self, ctx:Cobol85Parser.EnableStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#entryStatement.
    def enterEntryStatement(self, ctx:Cobol85Parser.EntryStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateStatement.
    def enterEvaluateStatement(self, ctx:Cobol85Parser.EvaluateStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateSelect.
    def enterEvaluateSelect(self, ctx:Cobol85Parser.EvaluateSelectContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateAlsoSelect.
    def enterEvaluateAlsoSelect(self, ctx:Cobol85Parser.EvaluateAlsoSelectContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateWhenPhrase.
    def enterEvaluateWhenPhrase(self, ctx:Cobol85Parser.EvaluateWhenPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateWhen.
    def enterEvaluateWhen(self, ctx:Cobol85Parser.EvaluateWhenContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateCondition.
    def enterEvaluateCondition(self, ctx:Cobol85Parser.EvaluateConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateThrough.
    def enterEvaluateThrough(self, ctx:Cobol85Parser.EvaluateThroughContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateAlsoCondition.
    def enterEvaluateAlsoCondition(self, ctx:Cobol85Parser.EvaluateAlsoConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateWhenOther.
    def enterEvaluateWhenOther(self, ctx:Cobol85Parser.EvaluateWhenOtherContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#evaluateValue.
    def enterEvaluateValue(self, ctx:Cobol85Parser.EvaluateValueContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#execCicsStatement.
    def enterExecCicsStatement(self, ctx:Cobol85Parser.ExecCicsStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#execSqlStatement.
    def enterExecSqlStatement(self, ctx:Cobol85Parser.ExecSqlStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#execSqlImsStatement.
    def enterExecSqlImsStatement(self, ctx:Cobol85Parser.ExecSqlImsStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#exhibitStatement.
    def enterExhibitStatement(self, ctx:Cobol85Parser.ExhibitStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#exhibitOperand.
    def enterExhibitOperand(self, ctx:Cobol85Parser.ExhibitOperandContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#exitStatement.
    def enterExitStatement(self, ctx:Cobol85Parser.ExitStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#generateStatement.
    def enterGenerateStatement(self, ctx:Cobol85Parser.GenerateStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#gobackStatement.
    def enterGobackStatement(self, ctx:Cobol85Parser.GobackStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#goToStatement.
    def enterGoToStatement(self, ctx:Cobol85Parser.GoToStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#goToStatementSimple.
    def enterGoToStatementSimple(self, ctx:Cobol85Parser.GoToStatementSimpleContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#goToDependingOnStatement.
    def enterGoToDependingOnStatement(self, ctx:Cobol85Parser.GoToDependingOnStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#ifStatement.
    def enterIfStatement(self, ctx:Cobol85Parser.IfStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#ifThen.
    def enterIfThen(self, ctx:Cobol85Parser.IfThenContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#ifElse.
    def enterIfElse(self, ctx:Cobol85Parser.IfElseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#initializeStatement.
    def enterInitializeStatement(self, ctx:Cobol85Parser.InitializeStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#initializeReplacingPhrase.
    def enterInitializeReplacingPhrase(self, ctx:Cobol85Parser.InitializeReplacingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#initializeReplacingBy.
    def enterInitializeReplacingBy(self, ctx:Cobol85Parser.InitializeReplacingByContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#initiateStatement.
    def enterInitiateStatement(self, ctx:Cobol85Parser.InitiateStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectStatement.
    def enterInspectStatement(self, ctx:Cobol85Parser.InspectStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectTallyingPhrase.
    def enterInspectTallyingPhrase(self, ctx:Cobol85Parser.InspectTallyingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectReplacingPhrase.
    def enterInspectReplacingPhrase(self, ctx:Cobol85Parser.InspectReplacingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectTallyingReplacingPhrase.
    def enterInspectTallyingReplacingPhrase(self, ctx:Cobol85Parser.InspectTallyingReplacingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectConvertingPhrase.
    def enterInspectConvertingPhrase(self, ctx:Cobol85Parser.InspectConvertingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectFor.
    def enterInspectFor(self, ctx:Cobol85Parser.InspectForContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectCharacters.
    def enterInspectCharacters(self, ctx:Cobol85Parser.InspectCharactersContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectReplacingCharacters.
    def enterInspectReplacingCharacters(self, ctx:Cobol85Parser.InspectReplacingCharactersContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectAllLeadings.
    def enterInspectAllLeadings(self, ctx:Cobol85Parser.InspectAllLeadingsContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectReplacingAllLeadings.
    def enterInspectReplacingAllLeadings(self, ctx:Cobol85Parser.InspectReplacingAllLeadingsContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectAllLeading.
    def enterInspectAllLeading(self, ctx:Cobol85Parser.InspectAllLeadingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectReplacingAllLeading.
    def enterInspectReplacingAllLeading(self, ctx:Cobol85Parser.InspectReplacingAllLeadingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectBy.
    def enterInspectBy(self, ctx:Cobol85Parser.InspectByContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectTo.
    def enterInspectTo(self, ctx:Cobol85Parser.InspectToContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inspectBeforeAfter.
    def enterInspectBeforeAfter(self, ctx:Cobol85Parser.InspectBeforeAfterContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeStatement.
    def enterMergeStatement(self, ctx:Cobol85Parser.MergeStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeOnKeyClause.
    def enterMergeOnKeyClause(self, ctx:Cobol85Parser.MergeOnKeyClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeCollatingSequencePhrase.
    def enterMergeCollatingSequencePhrase(self, ctx:Cobol85Parser.MergeCollatingSequencePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeCollatingAlphanumeric.
    def enterMergeCollatingAlphanumeric(self, ctx:Cobol85Parser.MergeCollatingAlphanumericContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeCollatingNational.
    def enterMergeCollatingNational(self, ctx:Cobol85Parser.MergeCollatingNationalContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeUsing.
    def enterMergeUsing(self, ctx:Cobol85Parser.MergeUsingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeOutputProcedurePhrase.
    def enterMergeOutputProcedurePhrase(self, ctx:Cobol85Parser.MergeOutputProcedurePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeOutputThrough.
    def enterMergeOutputThrough(self, ctx:Cobol85Parser.MergeOutputThroughContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeGivingPhrase.
    def enterMergeGivingPhrase(self, ctx:Cobol85Parser.MergeGivingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mergeGiving.
    def enterMergeGiving(self, ctx:Cobol85Parser.MergeGivingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#moveStatement.
    def enterMoveStatement(self, ctx:Cobol85Parser.MoveStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#moveToStatement.
    def enterMoveToStatement(self, ctx:Cobol85Parser.MoveToStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#moveToSendingArea.
    def enterMoveToSendingArea(self, ctx:Cobol85Parser.MoveToSendingAreaContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#moveCorrespondingToStatement.
    def enterMoveCorrespondingToStatement(self, ctx:Cobol85Parser.MoveCorrespondingToStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#moveCorrespondingToSendingArea.
    def enterMoveCorrespondingToSendingArea(self, ctx:Cobol85Parser.MoveCorrespondingToSendingAreaContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#multiplyStatement.
    def enterMultiplyStatement(self, ctx:Cobol85Parser.MultiplyStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#multiplyRegular.
    def enterMultiplyRegular(self, ctx:Cobol85Parser.MultiplyRegularContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#multiplyRegularOperand.
    def enterMultiplyRegularOperand(self, ctx:Cobol85Parser.MultiplyRegularOperandContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#multiplyGiving.
    def enterMultiplyGiving(self, ctx:Cobol85Parser.MultiplyGivingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#multiplyGivingOperand.
    def enterMultiplyGivingOperand(self, ctx:Cobol85Parser.MultiplyGivingOperandContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#multiplyGivingResult.
    def enterMultiplyGivingResult(self, ctx:Cobol85Parser.MultiplyGivingResultContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#openStatement.
    def enterOpenStatement(self, ctx:Cobol85Parser.OpenStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#openInputStatement.
    def enterOpenInputStatement(self, ctx:Cobol85Parser.OpenInputStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#openInput.
    def enterOpenInput(self, ctx:Cobol85Parser.OpenInputContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#openOutputStatement.
    def enterOpenOutputStatement(self, ctx:Cobol85Parser.OpenOutputStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#openOutput.
    def enterOpenOutput(self, ctx:Cobol85Parser.OpenOutputContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#openIOStatement.
    def enterOpenIOStatement(self, ctx:Cobol85Parser.OpenIOStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#openExtendStatement.
    def enterOpenExtendStatement(self, ctx:Cobol85Parser.OpenExtendStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performStatement.
    def enterPerformStatement(self, ctx:Cobol85Parser.PerformStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performInlineStatement.
    def enterPerformInlineStatement(self, ctx:Cobol85Parser.PerformInlineStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performProcedureStatement.
    def enterPerformProcedureStatement(self, ctx:Cobol85Parser.PerformProcedureStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performType.
    def enterPerformType(self, ctx:Cobol85Parser.PerformTypeContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performTimes.
    def enterPerformTimes(self, ctx:Cobol85Parser.PerformTimesContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performUntil.
    def enterPerformUntil(self, ctx:Cobol85Parser.PerformUntilContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performVarying.
    def enterPerformVarying(self, ctx:Cobol85Parser.PerformVaryingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performVaryingClause.
    def enterPerformVaryingClause(self, ctx:Cobol85Parser.PerformVaryingClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performVaryingPhrase.
    def enterPerformVaryingPhrase(self, ctx:Cobol85Parser.PerformVaryingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performAfter.
    def enterPerformAfter(self, ctx:Cobol85Parser.PerformAfterContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performFrom.
    def enterPerformFrom(self, ctx:Cobol85Parser.PerformFromContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performBy.
    def enterPerformBy(self, ctx:Cobol85Parser.PerformByContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#performTestClause.
    def enterPerformTestClause(self, ctx:Cobol85Parser.PerformTestClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#purgeStatement.
    def enterPurgeStatement(self, ctx:Cobol85Parser.PurgeStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#readStatement.
    def enterReadStatement(self, ctx:Cobol85Parser.ReadStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#readInto.
    def enterReadInto(self, ctx:Cobol85Parser.ReadIntoContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#readWith.
    def enterReadWith(self, ctx:Cobol85Parser.ReadWithContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#readKey.
    def enterReadKey(self, ctx:Cobol85Parser.ReadKeyContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveStatement.
    def enterReceiveStatement(self, ctx:Cobol85Parser.ReceiveStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveFromStatement.
    def enterReceiveFromStatement(self, ctx:Cobol85Parser.ReceiveFromStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveFrom.
    def enterReceiveFrom(self, ctx:Cobol85Parser.ReceiveFromContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveIntoStatement.
    def enterReceiveIntoStatement(self, ctx:Cobol85Parser.ReceiveIntoStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveNoData.
    def enterReceiveNoData(self, ctx:Cobol85Parser.ReceiveNoDataContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveWithData.
    def enterReceiveWithData(self, ctx:Cobol85Parser.ReceiveWithDataContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveBefore.
    def enterReceiveBefore(self, ctx:Cobol85Parser.ReceiveBeforeContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveWith.
    def enterReceiveWith(self, ctx:Cobol85Parser.ReceiveWithContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveThread.
    def enterReceiveThread(self, ctx:Cobol85Parser.ReceiveThreadContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveSize.
    def enterReceiveSize(self, ctx:Cobol85Parser.ReceiveSizeContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#receiveStatus.
    def enterReceiveStatus(self, ctx:Cobol85Parser.ReceiveStatusContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#releaseStatement.
    def enterReleaseStatement(self, ctx:Cobol85Parser.ReleaseStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#returnStatement.
    def enterReturnStatement(self, ctx:Cobol85Parser.ReturnStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#returnInto.
    def enterReturnInto(self, ctx:Cobol85Parser.ReturnIntoContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#rewriteStatement.
    def enterRewriteStatement(self, ctx:Cobol85Parser.RewriteStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#rewriteFrom.
    def enterRewriteFrom(self, ctx:Cobol85Parser.RewriteFromContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#searchStatement.
    def enterSearchStatement(self, ctx:Cobol85Parser.SearchStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#searchVarying.
    def enterSearchVarying(self, ctx:Cobol85Parser.SearchVaryingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#searchWhen.
    def enterSearchWhen(self, ctx:Cobol85Parser.SearchWhenContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendStatement.
    def enterSendStatement(self, ctx:Cobol85Parser.SendStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendStatementSync.
    def enterSendStatementSync(self, ctx:Cobol85Parser.SendStatementSyncContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendStatementAsync.
    def enterSendStatementAsync(self, ctx:Cobol85Parser.SendStatementAsyncContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendFromPhrase.
    def enterSendFromPhrase(self, ctx:Cobol85Parser.SendFromPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendWithPhrase.
    def enterSendWithPhrase(self, ctx:Cobol85Parser.SendWithPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendReplacingPhrase.
    def enterSendReplacingPhrase(self, ctx:Cobol85Parser.SendReplacingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendAdvancingPhrase.
    def enterSendAdvancingPhrase(self, ctx:Cobol85Parser.SendAdvancingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendAdvancingPage.
    def enterSendAdvancingPage(self, ctx:Cobol85Parser.SendAdvancingPageContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendAdvancingLines.
    def enterSendAdvancingLines(self, ctx:Cobol85Parser.SendAdvancingLinesContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sendAdvancingMnemonic.
    def enterSendAdvancingMnemonic(self, ctx:Cobol85Parser.SendAdvancingMnemonicContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#setStatement.
    def enterSetStatement(self, ctx:Cobol85Parser.SetStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#setToStatement.
    def enterSetToStatement(self, ctx:Cobol85Parser.SetToStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#setUpDownByStatement.
    def enterSetUpDownByStatement(self, ctx:Cobol85Parser.SetUpDownByStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#setTo.
    def enterSetTo(self, ctx:Cobol85Parser.SetToContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#setToValue.
    def enterSetToValue(self, ctx:Cobol85Parser.SetToValueContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#setByValue.
    def enterSetByValue(self, ctx:Cobol85Parser.SetByValueContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortStatement.
    def enterSortStatement(self, ctx:Cobol85Parser.SortStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortOnKeyClause.
    def enterSortOnKeyClause(self, ctx:Cobol85Parser.SortOnKeyClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortDuplicatesPhrase.
    def enterSortDuplicatesPhrase(self, ctx:Cobol85Parser.SortDuplicatesPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortCollatingSequencePhrase.
    def enterSortCollatingSequencePhrase(self, ctx:Cobol85Parser.SortCollatingSequencePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortCollatingAlphanumeric.
    def enterSortCollatingAlphanumeric(self, ctx:Cobol85Parser.SortCollatingAlphanumericContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortCollatingNational.
    def enterSortCollatingNational(self, ctx:Cobol85Parser.SortCollatingNationalContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortInputProcedurePhrase.
    def enterSortInputProcedurePhrase(self, ctx:Cobol85Parser.SortInputProcedurePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortInputThrough.
    def enterSortInputThrough(self, ctx:Cobol85Parser.SortInputThroughContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortUsing.
    def enterSortUsing(self, ctx:Cobol85Parser.SortUsingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortOutputProcedurePhrase.
    def enterSortOutputProcedurePhrase(self, ctx:Cobol85Parser.SortOutputProcedurePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortOutputThrough.
    def enterSortOutputThrough(self, ctx:Cobol85Parser.SortOutputThroughContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortGivingPhrase.
    def enterSortGivingPhrase(self, ctx:Cobol85Parser.SortGivingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sortGiving.
    def enterSortGiving(self, ctx:Cobol85Parser.SortGivingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#startStatement.
    def enterStartStatement(self, ctx:Cobol85Parser.StartStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#startKey.
    def enterStartKey(self, ctx:Cobol85Parser.StartKeyContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#stopStatement.
    def enterStopStatement(self, ctx:Cobol85Parser.StopStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#stringStatement.
    def enterStringStatement(self, ctx:Cobol85Parser.StringStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#stringSendingPhrase.
    def enterStringSendingPhrase(self, ctx:Cobol85Parser.StringSendingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#stringSending.
    def enterStringSending(self, ctx:Cobol85Parser.StringSendingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#stringDelimitedByPhrase.
    def enterStringDelimitedByPhrase(self, ctx:Cobol85Parser.StringDelimitedByPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#stringForPhrase.
    def enterStringForPhrase(self, ctx:Cobol85Parser.StringForPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#stringIntoPhrase.
    def enterStringIntoPhrase(self, ctx:Cobol85Parser.StringIntoPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#stringWithPointerPhrase.
    def enterStringWithPointerPhrase(self, ctx:Cobol85Parser.StringWithPointerPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subtractStatement.
    def enterSubtractStatement(self, ctx:Cobol85Parser.SubtractStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subtractFromStatement.
    def enterSubtractFromStatement(self, ctx:Cobol85Parser.SubtractFromStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subtractFromGivingStatement.
    def enterSubtractFromGivingStatement(self, ctx:Cobol85Parser.SubtractFromGivingStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subtractCorrespondingStatement.
    def enterSubtractCorrespondingStatement(self, ctx:Cobol85Parser.SubtractCorrespondingStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subtractSubtrahend.
    def enterSubtractSubtrahend(self, ctx:Cobol85Parser.SubtractSubtrahendContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subtractMinuend.
    def enterSubtractMinuend(self, ctx:Cobol85Parser.SubtractMinuendContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subtractMinuendGiving.
    def enterSubtractMinuendGiving(self, ctx:Cobol85Parser.SubtractMinuendGivingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subtractGiving.
    def enterSubtractGiving(self, ctx:Cobol85Parser.SubtractGivingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subtractMinuendCorresponding.
    def enterSubtractMinuendCorresponding(self, ctx:Cobol85Parser.SubtractMinuendCorrespondingContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#terminateStatement.
    def enterTerminateStatement(self, ctx:Cobol85Parser.TerminateStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringStatement.
    def enterUnstringStatement(self, ctx:Cobol85Parser.UnstringStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringSendingPhrase.
    def enterUnstringSendingPhrase(self, ctx:Cobol85Parser.UnstringSendingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringDelimitedByPhrase.
    def enterUnstringDelimitedByPhrase(self, ctx:Cobol85Parser.UnstringDelimitedByPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringOrAllPhrase.
    def enterUnstringOrAllPhrase(self, ctx:Cobol85Parser.UnstringOrAllPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringIntoPhrase.
    def enterUnstringIntoPhrase(self, ctx:Cobol85Parser.UnstringIntoPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringInto.
    def enterUnstringInto(self, ctx:Cobol85Parser.UnstringIntoContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringDelimiterIn.
    def enterUnstringDelimiterIn(self, ctx:Cobol85Parser.UnstringDelimiterInContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringCountIn.
    def enterUnstringCountIn(self, ctx:Cobol85Parser.UnstringCountInContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringWithPointerPhrase.
    def enterUnstringWithPointerPhrase(self, ctx:Cobol85Parser.UnstringWithPointerPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#unstringTallyingPhrase.
    def enterUnstringTallyingPhrase(self, ctx:Cobol85Parser.UnstringTallyingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#useStatement.
    def enterUseStatement(self, ctx:Cobol85Parser.UseStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#useAfterClause.
    def enterUseAfterClause(self, ctx:Cobol85Parser.UseAfterClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#useAfterOn.
    def enterUseAfterOn(self, ctx:Cobol85Parser.UseAfterOnContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#useDebugClause.
    def enterUseDebugClause(self, ctx:Cobol85Parser.UseDebugClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#useDebugOn.
    def enterUseDebugOn(self, ctx:Cobol85Parser.UseDebugOnContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#writeStatement.
    def enterWriteStatement(self, ctx:Cobol85Parser.WriteStatementContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#writeFromPhrase.
    def enterWriteFromPhrase(self, ctx:Cobol85Parser.WriteFromPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#writeAdvancingPhrase.
    def enterWriteAdvancingPhrase(self, ctx:Cobol85Parser.WriteAdvancingPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#writeAdvancingPage.
    def enterWriteAdvancingPage(self, ctx:Cobol85Parser.WriteAdvancingPageContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#writeAdvancingLines.
    def enterWriteAdvancingLines(self, ctx:Cobol85Parser.WriteAdvancingLinesContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#writeAdvancingMnemonic.
    def enterWriteAdvancingMnemonic(self, ctx:Cobol85Parser.WriteAdvancingMnemonicContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#writeAtEndOfPagePhrase.
    def enterWriteAtEndOfPagePhrase(self, ctx:Cobol85Parser.WriteAtEndOfPagePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#writeNotAtEndOfPagePhrase.
    def enterWriteNotAtEndOfPagePhrase(self, ctx:Cobol85Parser.WriteNotAtEndOfPagePhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#atEndPhrase.
    def enterAtEndPhrase(self, ctx:Cobol85Parser.AtEndPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#notAtEndPhrase.
    def enterNotAtEndPhrase(self, ctx:Cobol85Parser.NotAtEndPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#invalidKeyPhrase.
    def enterInvalidKeyPhrase(self, ctx:Cobol85Parser.InvalidKeyPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#notInvalidKeyPhrase.
    def enterNotInvalidKeyPhrase(self, ctx:Cobol85Parser.NotInvalidKeyPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#onOverflowPhrase.
    def enterOnOverflowPhrase(self, ctx:Cobol85Parser.OnOverflowPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#notOnOverflowPhrase.
    def enterNotOnOverflowPhrase(self, ctx:Cobol85Parser.NotOnOverflowPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#onSizeErrorPhrase.
    def enterOnSizeErrorPhrase(self, ctx:Cobol85Parser.OnSizeErrorPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#notOnSizeErrorPhrase.
    def enterNotOnSizeErrorPhrase(self, ctx:Cobol85Parser.NotOnSizeErrorPhraseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#onExceptionClause.
    def enterOnExceptionClause(self, ctx:Cobol85Parser.OnExceptionClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#notOnExceptionClause.
    def enterNotOnExceptionClause(self, ctx:Cobol85Parser.NotOnExceptionClauseContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:Cobol85Parser.ArithmeticExpressionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#plusMinus.
    def enterPlusMinus(self, ctx:Cobol85Parser.PlusMinusContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#multDivs.
    def enterMultDivs(self, ctx:Cobol85Parser.MultDivsContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#multDiv.
    def enterMultDiv(self, ctx:Cobol85Parser.MultDivContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#powers.
    def enterPowers(self, ctx:Cobol85Parser.PowersContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#power.
    def enterPower(self, ctx:Cobol85Parser.PowerContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#basis.
    def enterBasis(self, ctx:Cobol85Parser.BasisContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#condition.
    def enterCondition(self, ctx:Cobol85Parser.ConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#andOrCondition.
    def enterAndOrCondition(self, ctx:Cobol85Parser.AndOrConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#combinableCondition.
    def enterCombinableCondition(self, ctx:Cobol85Parser.CombinableConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#simpleCondition.
    def enterSimpleCondition(self, ctx:Cobol85Parser.SimpleConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#classCondition.
    def enterClassCondition(self, ctx:Cobol85Parser.ClassConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#conditionNameReference.
    def enterConditionNameReference(self, ctx:Cobol85Parser.ConditionNameReferenceContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#conditionNameSubscriptReference.
    def enterConditionNameSubscriptReference(self, ctx:Cobol85Parser.ConditionNameSubscriptReferenceContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#relationCondition.
    def enterRelationCondition(self, ctx:Cobol85Parser.RelationConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#relationSignCondition.
    def enterRelationSignCondition(self, ctx:Cobol85Parser.RelationSignConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#relationArithmeticComparison.
    def enterRelationArithmeticComparison(self, ctx:Cobol85Parser.RelationArithmeticComparisonContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#relationCombinedComparison.
    def enterRelationCombinedComparison(self, ctx:Cobol85Parser.RelationCombinedComparisonContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#relationCombinedCondition.
    def enterRelationCombinedCondition(self, ctx:Cobol85Parser.RelationCombinedConditionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#relationalOperator.
    def enterRelationalOperator(self, ctx:Cobol85Parser.RelationalOperatorContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#abbreviation.
    def enterAbbreviation(self, ctx:Cobol85Parser.AbbreviationContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#identifier.
    def enterIdentifier(self, ctx:Cobol85Parser.IdentifierContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#tableCall.
    def enterTableCall(self, ctx:Cobol85Parser.TableCallContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#functionCall.
    def enterFunctionCall(self, ctx:Cobol85Parser.FunctionCallContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#referenceModifier.
    def enterReferenceModifier(self, ctx:Cobol85Parser.ReferenceModifierContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#characterPosition.
    def enterCharacterPosition(self, ctx:Cobol85Parser.CharacterPositionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#length.
    def enterLength(self, ctx:Cobol85Parser.LengthContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#subscript_.
    def enterSubscript_(self, ctx:Cobol85Parser.Subscript_Context):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#argument.
    def enterArgument(self, ctx:Cobol85Parser.ArgumentContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataName.
    def enterQualifiedDataName(self, ctx:Cobol85Parser.QualifiedDataNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat1.
    def enterQualifiedDataNameFormat1(self, ctx:Cobol85Parser.QualifiedDataNameFormat1Context):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat2.
    def enterQualifiedDataNameFormat2(self, ctx:Cobol85Parser.QualifiedDataNameFormat2Context):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat3.
    def enterQualifiedDataNameFormat3(self, ctx:Cobol85Parser.QualifiedDataNameFormat3Context):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat4.
    def enterQualifiedDataNameFormat4(self, ctx:Cobol85Parser.QualifiedDataNameFormat4Context):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#qualifiedInData.
    def enterQualifiedInData(self, ctx:Cobol85Parser.QualifiedInDataContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inData.
    def enterInData(self, ctx:Cobol85Parser.InDataContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inFile.
    def enterInFile(self, ctx:Cobol85Parser.InFileContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inMnemonic.
    def enterInMnemonic(self, ctx:Cobol85Parser.InMnemonicContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inSection.
    def enterInSection(self, ctx:Cobol85Parser.InSectionContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inLibrary.
    def enterInLibrary(self, ctx:Cobol85Parser.InLibraryContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#inTable.
    def enterInTable(self, ctx:Cobol85Parser.InTableContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#alphabetName.
    def enterAlphabetName(self, ctx:Cobol85Parser.AlphabetNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#assignmentName.
    def enterAssignmentName(self, ctx:Cobol85Parser.AssignmentNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#basisName.
    def enterBasisName(self, ctx:Cobol85Parser.BasisNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#cdName.
    def enterCdName(self, ctx:Cobol85Parser.CdNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#className.
    def enterClassName(self, ctx:Cobol85Parser.ClassNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#computerName.
    def enterComputerName(self, ctx:Cobol85Parser.ComputerNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#conditionName.
    def enterConditionName(self, ctx:Cobol85Parser.ConditionNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#dataName.
    def enterDataName(self, ctx:Cobol85Parser.DataNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#dataDescName.
    def enterDataDescName(self, ctx:Cobol85Parser.DataDescNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#environmentName.
    def enterEnvironmentName(self, ctx:Cobol85Parser.EnvironmentNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#fileName.
    def enterFileName(self, ctx:Cobol85Parser.FileNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#functionName.
    def enterFunctionName(self, ctx:Cobol85Parser.FunctionNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#indexName.
    def enterIndexName(self, ctx:Cobol85Parser.IndexNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#languageName.
    def enterLanguageName(self, ctx:Cobol85Parser.LanguageNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#libraryName.
    def enterLibraryName(self, ctx:Cobol85Parser.LibraryNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#localName.
    def enterLocalName(self, ctx:Cobol85Parser.LocalNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#mnemonicName.
    def enterMnemonicName(self, ctx:Cobol85Parser.MnemonicNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#paragraphName.
    def enterParagraphName(self, ctx:Cobol85Parser.ParagraphNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#procedureName.
    def enterProcedureName(self, ctx:Cobol85Parser.ProcedureNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#programName.
    def enterProgramName(self, ctx:Cobol85Parser.ProgramNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#recordName.
    def enterRecordName(self, ctx:Cobol85Parser.RecordNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#reportName.
    def enterReportName(self, ctx:Cobol85Parser.ReportNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#routineName.
    def enterRoutineName(self, ctx:Cobol85Parser.RoutineNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#screenName.
    def enterScreenName(self, ctx:Cobol85Parser.ScreenNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#sectionName.
    def enterSectionName(self, ctx:Cobol85Parser.SectionNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#systemName.
    def enterSystemName(self, ctx:Cobol85Parser.SystemNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#symbolicCharacter.
    def enterSymbolicCharacter(self, ctx:Cobol85Parser.SymbolicCharacterContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#textName.
    def enterTextName(self, ctx:Cobol85Parser.TextNameContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#cobolWord.
    def enterCobolWord(self, ctx:Cobol85Parser.CobolWordContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#literal.
    def enterLiteral(self, ctx:Cobol85Parser.LiteralContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:Cobol85Parser.BooleanLiteralContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#numericLiteral.
    def enterNumericLiteral(self, ctx:Cobol85Parser.NumericLiteralContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#integerLiteral.
    def enterIntegerLiteral(self, ctx:Cobol85Parser.IntegerLiteralContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#cicsDfhRespLiteral.
    def enterCicsDfhRespLiteral(self, ctx:Cobol85Parser.CicsDfhRespLiteralContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#cicsDfhValueLiteral.
    def enterCicsDfhValueLiteral(self, ctx:Cobol85Parser.CicsDfhValueLiteralContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#figurativeConstant.
    def enterFigurativeConstant(self, ctx:Cobol85Parser.FigurativeConstantContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#specialRegister.
    def enterSpecialRegister(self, ctx:Cobol85Parser.SpecialRegisterContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})

    # Enter a parse tree produced by Cobol85Parser#commentEntry.
    def enterCommentEntry(self, ctx:Cobol85Parser.CommentEntryContext):
        ctx_id =str( id(ctx))
        parent = ctx.parentCtx
        parent_id = str(id(parent))
        accept_node = {"id": ctx_id, "data": {"label": type(ctx).__name__,"text":ctx.getText()}}
        self.nodes.append(accept_node)
        self.edges.append({"id": ctx_id, "source": parent_id, "target": ctx_id, "label": ""})