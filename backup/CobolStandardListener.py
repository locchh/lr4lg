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
        # Start processing procedure division for control flow
        self.nodes.append({"id": "start", "data": {"label": "start"}})

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionUsingClause.
    def enterProcedureDivisionUsingClause(self, ctx:Cobol85Parser.ProcedureDivisionUsingClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionGivingClause.
    def enterProcedureDivisionGivingClause(self, ctx:Cobol85Parser.ProcedureDivisionGivingClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionUsingParameter.
    def enterProcedureDivisionUsingParameter(self, ctx:Cobol85Parser.ProcedureDivisionUsingParameterContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByReferencePhrase.
    def enterProcedureDivisionByReferencePhrase(self, ctx:Cobol85Parser.ProcedureDivisionByReferencePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByReference.
    def enterProcedureDivisionByReference(self, ctx:Cobol85Parser.ProcedureDivisionByReferenceContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByValuePhrase.
    def enterProcedureDivisionByValuePhrase(self, ctx:Cobol85Parser.ProcedureDivisionByValuePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionByValue.
    def enterProcedureDivisionByValue(self, ctx:Cobol85Parser.ProcedureDivisionByValueContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureDeclaratives.
    def enterProcedureDeclaratives(self, ctx:Cobol85Parser.ProcedureDeclarativesContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureDeclarative.
    def enterProcedureDeclarative(self, ctx:Cobol85Parser.ProcedureDeclarativeContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureSectionHeader.
    def enterProcedureSectionHeader(self, ctx:Cobol85Parser.ProcedureSectionHeaderContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureDivisionBody.
    def enterProcedureDivisionBody(self, ctx:Cobol85Parser.ProcedureDivisionBodyContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureSection.
    def enterProcedureSection(self, ctx:Cobol85Parser.ProcedureSectionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#paragraphs.
    def enterParagraphs(self, ctx:Cobol85Parser.ParagraphsContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#paragraph.
    def enterParagraph(self, ctx:Cobol85Parser.ParagraphContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sentence.
    def enterSentence(self, ctx:Cobol85Parser.SentenceContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#statement.
    def enterStatement(self, ctx:Cobol85Parser.StatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#acceptStatement.
    def enterAcceptStatement(self, ctx:Cobol85Parser.AcceptStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#acceptFromDateStatement.
    def enterAcceptFromDateStatement(self, ctx:Cobol85Parser.AcceptFromDateStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#acceptFromMnemonicStatement.
    def enterAcceptFromMnemonicStatement(self, ctx:Cobol85Parser.AcceptFromMnemonicStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#acceptFromEscapeKeyStatement.
    def enterAcceptFromEscapeKeyStatement(self, ctx:Cobol85Parser.AcceptFromEscapeKeyStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#acceptMessageCountStatement.
    def enterAcceptMessageCountStatement(self, ctx:Cobol85Parser.AcceptMessageCountStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#addStatement.
    def enterAddStatement(self, ctx:Cobol85Parser.AddStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#addToStatement.
    def enterAddToStatement(self, ctx:Cobol85Parser.AddToStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#addToGivingStatement.
    def enterAddToGivingStatement(self, ctx:Cobol85Parser.AddToGivingStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#addCorrespondingStatement.
    def enterAddCorrespondingStatement(self, ctx:Cobol85Parser.AddCorrespondingStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#addFrom.
    def enterAddFrom(self, ctx:Cobol85Parser.AddFromContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#addTo.
    def enterAddTo(self, ctx:Cobol85Parser.AddToContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#addToGiving.
    def enterAddToGiving(self, ctx:Cobol85Parser.AddToGivingContext):
        pass


    # Enter a parse tree produced by Cobol85Parser#addGiving.
    def enterAddGiving(self, ctx:Cobol85Parser.AddGivingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#alteredGoTo.
    def enterAlteredGoTo(self, ctx:Cobol85Parser.AlteredGoToContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#alterStatement.
    def enterAlterStatement(self, ctx:Cobol85Parser.AlterStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#alterProceedTo.
    def enterAlterProceedTo(self, ctx:Cobol85Parser.AlterProceedToContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callStatement.
    def enterCallStatement(self, ctx:Cobol85Parser.CallStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callUsingPhrase.
    def enterCallUsingPhrase(self, ctx:Cobol85Parser.CallUsingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callUsingParameter.
    def enterCallUsingParameter(self, ctx:Cobol85Parser.CallUsingParameterContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callByReferencePhrase.
    def enterCallByReferencePhrase(self, ctx:Cobol85Parser.CallByReferencePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callByReference.
    def enterCallByReference(self, ctx:Cobol85Parser.CallByReferenceContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callByValuePhrase.
    def enterCallByValuePhrase(self, ctx:Cobol85Parser.CallByValuePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callByValue.
    def enterCallByValue(self, ctx:Cobol85Parser.CallByValueContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callByContentPhrase.
    def enterCallByContentPhrase(self, ctx:Cobol85Parser.CallByContentPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callByContent.
    def enterCallByContent(self, ctx:Cobol85Parser.CallByContentContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#callGivingPhrase.
    def enterCallGivingPhrase(self, ctx:Cobol85Parser.CallGivingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#cancelStatement.
    def enterCancelStatement(self, ctx:Cobol85Parser.CancelStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#cancelCall.
    def enterCancelCall(self, ctx:Cobol85Parser.CancelCallContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#closeStatement.
    def enterCloseStatement(self, ctx:Cobol85Parser.CloseStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#closeFile.
    def enterCloseFile(self, ctx:Cobol85Parser.CloseFileContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#closeReelUnitStatement.
    def enterCloseReelUnitStatement(self, ctx:Cobol85Parser.CloseReelUnitStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#closeRelativeStatement.
    def enterCloseRelativeStatement(self, ctx:Cobol85Parser.CloseRelativeStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOStatement.
    def enterClosePortFileIOStatement(self, ctx:Cobol85Parser.ClosePortFileIOStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsing.
    def enterClosePortFileIOUsing(self, ctx:Cobol85Parser.ClosePortFileIOUsingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsingCloseDisposition.
    def enterClosePortFileIOUsingCloseDisposition(self, ctx:Cobol85Parser.ClosePortFileIOUsingCloseDispositionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsingAssociatedData.
    def enterClosePortFileIOUsingAssociatedData(self, ctx:Cobol85Parser.ClosePortFileIOUsingAssociatedDataContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#closePortFileIOUsingAssociatedDataLength.
    def enterClosePortFileIOUsingAssociatedDataLength(self, ctx:Cobol85Parser.ClosePortFileIOUsingAssociatedDataLengthContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#computeStatement.
    def enterComputeStatement(self, ctx:Cobol85Parser.ComputeStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#computeStore.
    def enterComputeStore(self, ctx:Cobol85Parser.ComputeStoreContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#continueStatement.
    def enterContinueStatement(self, ctx:Cobol85Parser.ContinueStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#deleteStatement.
    def enterDeleteStatement(self, ctx:Cobol85Parser.DeleteStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#disableStatement.
    def enterDisableStatement(self, ctx:Cobol85Parser.DisableStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#displayStatement.
    def enterDisplayStatement(self, ctx:Cobol85Parser.DisplayStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#displayOperand.
    def enterDisplayOperand(self, ctx:Cobol85Parser.DisplayOperandContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#displayAt.
    def enterDisplayAt(self, ctx:Cobol85Parser.DisplayAtContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#displayUpon.
    def enterDisplayUpon(self, ctx:Cobol85Parser.DisplayUponContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#displayWith.
    def enterDisplayWith(self, ctx:Cobol85Parser.DisplayWithContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#divideStatement.
    def enterDivideStatement(self, ctx:Cobol85Parser.DivideStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#divideIntoStatement.
    def enterDivideIntoStatement(self, ctx:Cobol85Parser.DivideIntoStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#divideIntoGivingStatement.
    def enterDivideIntoGivingStatement(self, ctx:Cobol85Parser.DivideIntoGivingStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#divideByGivingStatement.
    def enterDivideByGivingStatement(self, ctx:Cobol85Parser.DivideByGivingStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#divideGivingPhrase.
    def enterDivideGivingPhrase(self, ctx:Cobol85Parser.DivideGivingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#divideInto.
    def enterDivideInto(self, ctx:Cobol85Parser.DivideIntoContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#divideGiving.
    def enterDivideGiving(self, ctx:Cobol85Parser.DivideGivingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#divideRemainder.
    def enterDivideRemainder(self, ctx:Cobol85Parser.DivideRemainderContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#enableStatement.
    def enterEnableStatement(self, ctx:Cobol85Parser.EnableStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#entryStatement.
    def enterEntryStatement(self, ctx:Cobol85Parser.EntryStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateStatement.
    def enterEvaluateStatement(self, ctx:Cobol85Parser.EvaluateStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateSelect.
    def enterEvaluateSelect(self, ctx:Cobol85Parser.EvaluateSelectContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateAlsoSelect.
    def enterEvaluateAlsoSelect(self, ctx:Cobol85Parser.EvaluateAlsoSelectContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateWhenPhrase.
    def enterEvaluateWhenPhrase(self, ctx:Cobol85Parser.EvaluateWhenPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateWhen.
    def enterEvaluateWhen(self, ctx:Cobol85Parser.EvaluateWhenContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateCondition.
    def enterEvaluateCondition(self, ctx:Cobol85Parser.EvaluateConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateThrough.
    def enterEvaluateThrough(self, ctx:Cobol85Parser.EvaluateThroughContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateAlsoCondition.
    def enterEvaluateAlsoCondition(self, ctx:Cobol85Parser.EvaluateAlsoConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateWhenOther.
    def enterEvaluateWhenOther(self, ctx:Cobol85Parser.EvaluateWhenOtherContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#evaluateValue.
    def enterEvaluateValue(self, ctx:Cobol85Parser.EvaluateValueContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#execCicsStatement.
    def enterExecCicsStatement(self, ctx:Cobol85Parser.ExecCicsStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#execSqlStatement.
    def enterExecSqlStatement(self, ctx:Cobol85Parser.ExecSqlStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#execSqlImsStatement.
    def enterExecSqlImsStatement(self, ctx:Cobol85Parser.ExecSqlImsStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#exhibitStatement.
    def enterExhibitStatement(self, ctx:Cobol85Parser.ExhibitStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#exhibitOperand.
    def enterExhibitOperand(self, ctx:Cobol85Parser.ExhibitOperandContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#exitStatement.
    def enterExitStatement(self, ctx:Cobol85Parser.ExitStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#generateStatement.
    def enterGenerateStatement(self, ctx:Cobol85Parser.GenerateStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#gobackStatement.
    def enterGobackStatement(self, ctx:Cobol85Parser.GobackStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#goToStatement.
    def enterGoToStatement(self, ctx:Cobol85Parser.GoToStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#goToStatementSimple.
    def enterGoToStatementSimple(self, ctx:Cobol85Parser.GoToStatementSimpleContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#goToDependingOnStatement.
    def enterGoToDependingOnStatement(self, ctx:Cobol85Parser.GoToDependingOnStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#ifStatement.
    def enterIfStatement(self, ctx:Cobol85Parser.IfStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#ifThen.
    def enterIfThen(self, ctx:Cobol85Parser.IfThenContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#ifElse.
    def enterIfElse(self, ctx:Cobol85Parser.IfElseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#initializeStatement.
    def enterInitializeStatement(self, ctx:Cobol85Parser.InitializeStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#initializeReplacingPhrase.
    def enterInitializeReplacingPhrase(self, ctx:Cobol85Parser.InitializeReplacingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#initializeReplacingBy.
    def enterInitializeReplacingBy(self, ctx:Cobol85Parser.InitializeReplacingByContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#initiateStatement.
    def enterInitiateStatement(self, ctx:Cobol85Parser.InitiateStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectStatement.
    def enterInspectStatement(self, ctx:Cobol85Parser.InspectStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectTallyingPhrase.
    def enterInspectTallyingPhrase(self, ctx:Cobol85Parser.InspectTallyingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectReplacingPhrase.
    def enterInspectReplacingPhrase(self, ctx:Cobol85Parser.InspectReplacingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectTallyingReplacingPhrase.
    def enterInspectTallyingReplacingPhrase(self, ctx:Cobol85Parser.InspectTallyingReplacingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectConvertingPhrase.
    def enterInspectConvertingPhrase(self, ctx:Cobol85Parser.InspectConvertingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectFor.
    def enterInspectFor(self, ctx:Cobol85Parser.InspectForContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectCharacters.
    def enterInspectCharacters(self, ctx:Cobol85Parser.InspectCharactersContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectReplacingCharacters.
    def enterInspectReplacingCharacters(self, ctx:Cobol85Parser.InspectReplacingCharactersContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectAllLeadings.
    def enterInspectAllLeadings(self, ctx:Cobol85Parser.InspectAllLeadingsContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectReplacingAllLeadings.
    def enterInspectReplacingAllLeadings(self, ctx:Cobol85Parser.InspectReplacingAllLeadingsContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectAllLeading.
    def enterInspectAllLeading(self, ctx:Cobol85Parser.InspectAllLeadingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectReplacingAllLeading.
    def enterInspectReplacingAllLeading(self, ctx:Cobol85Parser.InspectReplacingAllLeadingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectBy.
    def enterInspectBy(self, ctx:Cobol85Parser.InspectByContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectTo.
    def enterInspectTo(self, ctx:Cobol85Parser.InspectToContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inspectBeforeAfter.
    def enterInspectBeforeAfter(self, ctx:Cobol85Parser.InspectBeforeAfterContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeStatement.
    def enterMergeStatement(self, ctx:Cobol85Parser.MergeStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeOnKeyClause.
    def enterMergeOnKeyClause(self, ctx:Cobol85Parser.MergeOnKeyClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeCollatingSequencePhrase.
    def enterMergeCollatingSequencePhrase(self, ctx:Cobol85Parser.MergeCollatingSequencePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeCollatingAlphanumeric.
    def enterMergeCollatingAlphanumeric(self, ctx:Cobol85Parser.MergeCollatingAlphanumericContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeCollatingNational.
    def enterMergeCollatingNational(self, ctx:Cobol85Parser.MergeCollatingNationalContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeUsing.
    def enterMergeUsing(self, ctx:Cobol85Parser.MergeUsingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeOutputProcedurePhrase.
    def enterMergeOutputProcedurePhrase(self, ctx:Cobol85Parser.MergeOutputProcedurePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeOutputThrough.
    def enterMergeOutputThrough(self, ctx:Cobol85Parser.MergeOutputThroughContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeGivingPhrase.
    def enterMergeGivingPhrase(self, ctx:Cobol85Parser.MergeGivingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mergeGiving.
    def enterMergeGiving(self, ctx:Cobol85Parser.MergeGivingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#moveStatement.
    def enterMoveStatement(self, ctx:Cobol85Parser.MoveStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#moveToStatement.
    def enterMoveToStatement(self, ctx:Cobol85Parser.MoveToStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#moveToSendingArea.
    def enterMoveToSendingArea(self, ctx:Cobol85Parser.MoveToSendingAreaContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#moveCorrespondingToStatement.
    def enterMoveCorrespondingToStatement(self, ctx:Cobol85Parser.MoveCorrespondingToStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#moveCorrespondingToSendingArea.
    def enterMoveCorrespondingToSendingArea(self, ctx:Cobol85Parser.MoveCorrespondingToSendingAreaContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#multiplyStatement.
    def enterMultiplyStatement(self, ctx:Cobol85Parser.MultiplyStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#multiplyRegular.
    def enterMultiplyRegular(self, ctx:Cobol85Parser.MultiplyRegularContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#multiplyRegularOperand.
    def enterMultiplyRegularOperand(self, ctx:Cobol85Parser.MultiplyRegularOperandContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#multiplyGiving.
    def enterMultiplyGiving(self, ctx:Cobol85Parser.MultiplyGivingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#multiplyGivingOperand.
    def enterMultiplyGivingOperand(self, ctx:Cobol85Parser.MultiplyGivingOperandContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#multiplyGivingResult.
    def enterMultiplyGivingResult(self, ctx:Cobol85Parser.MultiplyGivingResultContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#openStatement.
    def enterOpenStatement(self, ctx:Cobol85Parser.OpenStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#openInputStatement.
    def enterOpenInputStatement(self, ctx:Cobol85Parser.OpenInputStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#openInput.
    def enterOpenInput(self, ctx:Cobol85Parser.OpenInputContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#openOutputStatement.
    def enterOpenOutputStatement(self, ctx:Cobol85Parser.OpenOutputStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#openOutput.
    def enterOpenOutput(self, ctx:Cobol85Parser.OpenOutputContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#openIOStatement.
    def enterOpenIOStatement(self, ctx:Cobol85Parser.OpenIOStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#openExtendStatement.
    def enterOpenExtendStatement(self, ctx:Cobol85Parser.OpenExtendStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performStatement.
    def enterPerformStatement(self, ctx:Cobol85Parser.PerformStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performInlineStatement.
    def enterPerformInlineStatement(self, ctx:Cobol85Parser.PerformInlineStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performProcedureStatement.
    def enterPerformProcedureStatement(self, ctx:Cobol85Parser.PerformProcedureStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performType.
    def enterPerformType(self, ctx:Cobol85Parser.PerformTypeContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performTimes.
    def enterPerformTimes(self, ctx:Cobol85Parser.PerformTimesContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performUntil.
    def enterPerformUntil(self, ctx:Cobol85Parser.PerformUntilContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performVarying.
    def enterPerformVarying(self, ctx:Cobol85Parser.PerformVaryingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performVaryingClause.
    def enterPerformVaryingClause(self, ctx:Cobol85Parser.PerformVaryingClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performVaryingPhrase.
    def enterPerformVaryingPhrase(self, ctx:Cobol85Parser.PerformVaryingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performAfter.
    def enterPerformAfter(self, ctx:Cobol85Parser.PerformAfterContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performFrom.
    def enterPerformFrom(self, ctx:Cobol85Parser.PerformFromContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performBy.
    def enterPerformBy(self, ctx:Cobol85Parser.PerformByContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#performTestClause.
    def enterPerformTestClause(self, ctx:Cobol85Parser.PerformTestClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#purgeStatement.
    def enterPurgeStatement(self, ctx:Cobol85Parser.PurgeStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#readStatement.
    def enterReadStatement(self, ctx:Cobol85Parser.ReadStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#readInto.
    def enterReadInto(self, ctx:Cobol85Parser.ReadIntoContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#readWith.
    def enterReadWith(self, ctx:Cobol85Parser.ReadWithContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#readKey.
    def enterReadKey(self, ctx:Cobol85Parser.ReadKeyContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveStatement.
    def enterReceiveStatement(self, ctx:Cobol85Parser.ReceiveStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveFromStatement.
    def enterReceiveFromStatement(self, ctx:Cobol85Parser.ReceiveFromStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveFrom.
    def enterReceiveFrom(self, ctx:Cobol85Parser.ReceiveFromContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveIntoStatement.
    def enterReceiveIntoStatement(self, ctx:Cobol85Parser.ReceiveIntoStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveNoData.
    def enterReceiveNoData(self, ctx:Cobol85Parser.ReceiveNoDataContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveWithData.
    def enterReceiveWithData(self, ctx:Cobol85Parser.ReceiveWithDataContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveBefore.
    def enterReceiveBefore(self, ctx:Cobol85Parser.ReceiveBeforeContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveWith.
    def enterReceiveWith(self, ctx:Cobol85Parser.ReceiveWithContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveThread.
    def enterReceiveThread(self, ctx:Cobol85Parser.ReceiveThreadContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveSize.
    def enterReceiveSize(self, ctx:Cobol85Parser.ReceiveSizeContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#receiveStatus.
    def enterReceiveStatus(self, ctx:Cobol85Parser.ReceiveStatusContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#releaseStatement.
    def enterReleaseStatement(self, ctx:Cobol85Parser.ReleaseStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#returnStatement.
    def enterReturnStatement(self, ctx:Cobol85Parser.ReturnStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#returnInto.
    def enterReturnInto(self, ctx:Cobol85Parser.ReturnIntoContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#rewriteStatement.
    def enterRewriteStatement(self, ctx:Cobol85Parser.RewriteStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#rewriteFrom.
    def enterRewriteFrom(self, ctx:Cobol85Parser.RewriteFromContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#searchStatement.
    def enterSearchStatement(self, ctx:Cobol85Parser.SearchStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#searchVarying.
    def enterSearchVarying(self, ctx:Cobol85Parser.SearchVaryingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#searchWhen.
    def enterSearchWhen(self, ctx:Cobol85Parser.SearchWhenContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendStatement.
    def enterSendStatement(self, ctx:Cobol85Parser.SendStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendStatementSync.
    def enterSendStatementSync(self, ctx:Cobol85Parser.SendStatementSyncContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendStatementAsync.
    def enterSendStatementAsync(self, ctx:Cobol85Parser.SendStatementAsyncContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendFromPhrase.
    def enterSendFromPhrase(self, ctx:Cobol85Parser.SendFromPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendWithPhrase.
    def enterSendWithPhrase(self, ctx:Cobol85Parser.SendWithPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendReplacingPhrase.
    def enterSendReplacingPhrase(self, ctx:Cobol85Parser.SendReplacingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendAdvancingPhrase.
    def enterSendAdvancingPhrase(self, ctx:Cobol85Parser.SendAdvancingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendAdvancingPage.
    def enterSendAdvancingPage(self, ctx:Cobol85Parser.SendAdvancingPageContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendAdvancingLines.
    def enterSendAdvancingLines(self, ctx:Cobol85Parser.SendAdvancingLinesContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sendAdvancingMnemonic.
    def enterSendAdvancingMnemonic(self, ctx:Cobol85Parser.SendAdvancingMnemonicContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#setStatement.
    def enterSetStatement(self, ctx:Cobol85Parser.SetStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#setToStatement.
    def enterSetToStatement(self, ctx:Cobol85Parser.SetToStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#setUpDownByStatement.
    def enterSetUpDownByStatement(self, ctx:Cobol85Parser.SetUpDownByStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#setTo.
    def enterSetTo(self, ctx:Cobol85Parser.SetToContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#setToValue.
    def enterSetToValue(self, ctx:Cobol85Parser.SetToValueContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#setByValue.
    def enterSetByValue(self, ctx:Cobol85Parser.SetByValueContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortStatement.
    def enterSortStatement(self, ctx:Cobol85Parser.SortStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortOnKeyClause.
    def enterSortOnKeyClause(self, ctx:Cobol85Parser.SortOnKeyClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortDuplicatesPhrase.
    def enterSortDuplicatesPhrase(self, ctx:Cobol85Parser.SortDuplicatesPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortCollatingSequencePhrase.
    def enterSortCollatingSequencePhrase(self, ctx:Cobol85Parser.SortCollatingSequencePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortCollatingAlphanumeric.
    def enterSortCollatingAlphanumeric(self, ctx:Cobol85Parser.SortCollatingAlphanumericContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortCollatingNational.
    def enterSortCollatingNational(self, ctx:Cobol85Parser.SortCollatingNationalContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortInputProcedurePhrase.
    def enterSortInputProcedurePhrase(self, ctx:Cobol85Parser.SortInputProcedurePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortInputThrough.
    def enterSortInputThrough(self, ctx:Cobol85Parser.SortInputThroughContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortUsing.
    def enterSortUsing(self, ctx:Cobol85Parser.SortUsingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortOutputProcedurePhrase.
    def enterSortOutputProcedurePhrase(self, ctx:Cobol85Parser.SortOutputProcedurePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortOutputThrough.
    def enterSortOutputThrough(self, ctx:Cobol85Parser.SortOutputThroughContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortGivingPhrase.
    def enterSortGivingPhrase(self, ctx:Cobol85Parser.SortGivingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sortGiving.
    def enterSortGiving(self, ctx:Cobol85Parser.SortGivingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#startStatement.
    def enterStartStatement(self, ctx:Cobol85Parser.StartStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#startKey.
    def enterStartKey(self, ctx:Cobol85Parser.StartKeyContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#stopStatement.
    def enterStopStatement(self, ctx:Cobol85Parser.StopStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#stringStatement.
    def enterStringStatement(self, ctx:Cobol85Parser.StringStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#stringSendingPhrase.
    def enterStringSendingPhrase(self, ctx:Cobol85Parser.StringSendingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#stringSending.
    def enterStringSending(self, ctx:Cobol85Parser.StringSendingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#stringDelimitedByPhrase.
    def enterStringDelimitedByPhrase(self, ctx:Cobol85Parser.StringDelimitedByPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#stringForPhrase.
    def enterStringForPhrase(self, ctx:Cobol85Parser.StringForPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#stringIntoPhrase.
    def enterStringIntoPhrase(self, ctx:Cobol85Parser.StringIntoPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#stringWithPointerPhrase.
    def enterStringWithPointerPhrase(self, ctx:Cobol85Parser.StringWithPointerPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subtractStatement.
    def enterSubtractStatement(self, ctx:Cobol85Parser.SubtractStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subtractFromStatement.
    def enterSubtractFromStatement(self, ctx:Cobol85Parser.SubtractFromStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subtractFromGivingStatement.
    def enterSubtractFromGivingStatement(self, ctx:Cobol85Parser.SubtractFromGivingStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subtractCorrespondingStatement.
    def enterSubtractCorrespondingStatement(self, ctx:Cobol85Parser.SubtractCorrespondingStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subtractSubtrahend.
    def enterSubtractSubtrahend(self, ctx:Cobol85Parser.SubtractSubtrahendContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subtractMinuend.
    def enterSubtractMinuend(self, ctx:Cobol85Parser.SubtractMinuendContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subtractMinuendGiving.
    def enterSubtractMinuendGiving(self, ctx:Cobol85Parser.SubtractMinuendGivingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subtractGiving.
    def enterSubtractGiving(self, ctx:Cobol85Parser.SubtractGivingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subtractMinuendCorresponding.
    def enterSubtractMinuendCorresponding(self, ctx:Cobol85Parser.SubtractMinuendCorrespondingContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#terminateStatement.
    def enterTerminateStatement(self, ctx:Cobol85Parser.TerminateStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringStatement.
    def enterUnstringStatement(self, ctx:Cobol85Parser.UnstringStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringSendingPhrase.
    def enterUnstringSendingPhrase(self, ctx:Cobol85Parser.UnstringSendingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringDelimitedByPhrase.
    def enterUnstringDelimitedByPhrase(self, ctx:Cobol85Parser.UnstringDelimitedByPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringOrAllPhrase.
    def enterUnstringOrAllPhrase(self, ctx:Cobol85Parser.UnstringOrAllPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringIntoPhrase.
    def enterUnstringIntoPhrase(self, ctx:Cobol85Parser.UnstringIntoPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringInto.
    def enterUnstringInto(self, ctx:Cobol85Parser.UnstringIntoContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringDelimiterIn.
    def enterUnstringDelimiterIn(self, ctx:Cobol85Parser.UnstringDelimiterInContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringCountIn.
    def enterUnstringCountIn(self, ctx:Cobol85Parser.UnstringCountInContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringWithPointerPhrase.
    def enterUnstringWithPointerPhrase(self, ctx:Cobol85Parser.UnstringWithPointerPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#unstringTallyingPhrase.
    def enterUnstringTallyingPhrase(self, ctx:Cobol85Parser.UnstringTallyingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#useStatement.
    def enterUseStatement(self, ctx:Cobol85Parser.UseStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#useAfterClause.
    def enterUseAfterClause(self, ctx:Cobol85Parser.UseAfterClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#useAfterOn.
    def enterUseAfterOn(self, ctx:Cobol85Parser.UseAfterOnContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#useDebugClause.
    def enterUseDebugClause(self, ctx:Cobol85Parser.UseDebugClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#useDebugOn.
    def enterUseDebugOn(self, ctx:Cobol85Parser.UseDebugOnContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#writeStatement.
    def enterWriteStatement(self, ctx:Cobol85Parser.WriteStatementContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#writeFromPhrase.
    def enterWriteFromPhrase(self, ctx:Cobol85Parser.WriteFromPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#writeAdvancingPhrase.
    def enterWriteAdvancingPhrase(self, ctx:Cobol85Parser.WriteAdvancingPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#writeAdvancingPage.
    def enterWriteAdvancingPage(self, ctx:Cobol85Parser.WriteAdvancingPageContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#writeAdvancingLines.
    def enterWriteAdvancingLines(self, ctx:Cobol85Parser.WriteAdvancingLinesContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#writeAdvancingMnemonic.
    def enterWriteAdvancingMnemonic(self, ctx:Cobol85Parser.WriteAdvancingMnemonicContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#writeAtEndOfPagePhrase.
    def enterWriteAtEndOfPagePhrase(self, ctx:Cobol85Parser.WriteAtEndOfPagePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#writeNotAtEndOfPagePhrase.
    def enterWriteNotAtEndOfPagePhrase(self, ctx:Cobol85Parser.WriteNotAtEndOfPagePhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#atEndPhrase.
    def enterAtEndPhrase(self, ctx:Cobol85Parser.AtEndPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#notAtEndPhrase.
    def enterNotAtEndPhrase(self, ctx:Cobol85Parser.NotAtEndPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#invalidKeyPhrase.
    def enterInvalidKeyPhrase(self, ctx:Cobol85Parser.InvalidKeyPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#notInvalidKeyPhrase.
    def enterNotInvalidKeyPhrase(self, ctx:Cobol85Parser.NotInvalidKeyPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#onOverflowPhrase.
    def enterOnOverflowPhrase(self, ctx:Cobol85Parser.OnOverflowPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#notOnOverflowPhrase.
    def enterNotOnOverflowPhrase(self, ctx:Cobol85Parser.NotOnOverflowPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#onSizeErrorPhrase.
    def enterOnSizeErrorPhrase(self, ctx:Cobol85Parser.OnSizeErrorPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#notOnSizeErrorPhrase.
    def enterNotOnSizeErrorPhrase(self, ctx:Cobol85Parser.NotOnSizeErrorPhraseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#onExceptionClause.
    def enterOnExceptionClause(self, ctx:Cobol85Parser.OnExceptionClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#notOnExceptionClause.
    def enterNotOnExceptionClause(self, ctx:Cobol85Parser.NotOnExceptionClauseContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:Cobol85Parser.ArithmeticExpressionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#plusMinus.
    def enterPlusMinus(self, ctx:Cobol85Parser.PlusMinusContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#multDivs.
    def enterMultDivs(self, ctx:Cobol85Parser.MultDivsContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#multDiv.
    def enterMultDiv(self, ctx:Cobol85Parser.MultDivContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#powers.
    def enterPowers(self, ctx:Cobol85Parser.PowersContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#power.
    def enterPower(self, ctx:Cobol85Parser.PowerContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#basis.
    def enterBasis(self, ctx:Cobol85Parser.BasisContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#condition.
    def enterCondition(self, ctx:Cobol85Parser.ConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#andOrCondition.
    def enterAndOrCondition(self, ctx:Cobol85Parser.AndOrConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#combinableCondition.
    def enterCombinableCondition(self, ctx:Cobol85Parser.CombinableConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#simpleCondition.
    def enterSimpleCondition(self, ctx:Cobol85Parser.SimpleConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#classCondition.
    def enterClassCondition(self, ctx:Cobol85Parser.ClassConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#conditionNameReference.
    def enterConditionNameReference(self, ctx:Cobol85Parser.ConditionNameReferenceContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#conditionNameSubscriptReference.
    def enterConditionNameSubscriptReference(self, ctx:Cobol85Parser.ConditionNameSubscriptReferenceContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#relationCondition.
    def enterRelationCondition(self, ctx:Cobol85Parser.RelationConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#relationSignCondition.
    def enterRelationSignCondition(self, ctx:Cobol85Parser.RelationSignConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#relationArithmeticComparison.
    def enterRelationArithmeticComparison(self, ctx:Cobol85Parser.RelationArithmeticComparisonContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#relationCombinedComparison.
    def enterRelationCombinedComparison(self, ctx:Cobol85Parser.RelationCombinedComparisonContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#relationCombinedCondition.
    def enterRelationCombinedCondition(self, ctx:Cobol85Parser.RelationCombinedConditionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#relationalOperator.
    def enterRelationalOperator(self, ctx:Cobol85Parser.RelationalOperatorContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#abbreviation.
    def enterAbbreviation(self, ctx:Cobol85Parser.AbbreviationContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#identifier.
    def enterIdentifier(self, ctx:Cobol85Parser.IdentifierContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#tableCall.
    def enterTableCall(self, ctx:Cobol85Parser.TableCallContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#functionCall.
    def enterFunctionCall(self, ctx:Cobol85Parser.FunctionCallContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#referenceModifier.
    def enterReferenceModifier(self, ctx:Cobol85Parser.ReferenceModifierContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#characterPosition.
    def enterCharacterPosition(self, ctx:Cobol85Parser.CharacterPositionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#length.
    def enterLength(self, ctx:Cobol85Parser.LengthContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#subscript_.
    def enterSubscript_(self, ctx:Cobol85Parser.Subscript_Context):
        pass

    # Enter a parse tree produced by Cobol85Parser#argument.
    def enterArgument(self, ctx:Cobol85Parser.ArgumentContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataName.
    def enterQualifiedDataName(self, ctx:Cobol85Parser.QualifiedDataNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat1.
    def enterQualifiedDataNameFormat1(self, ctx:Cobol85Parser.QualifiedDataNameFormat1Context):
        pass

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat2.
    def enterQualifiedDataNameFormat2(self, ctx:Cobol85Parser.QualifiedDataNameFormat2Context):
        pass

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat3.
    def enterQualifiedDataNameFormat3(self, ctx:Cobol85Parser.QualifiedDataNameFormat3Context):
        pass

    # Enter a parse tree produced by Cobol85Parser#qualifiedDataNameFormat4.
    def enterQualifiedDataNameFormat4(self, ctx:Cobol85Parser.QualifiedDataNameFormat4Context):
        pass

    # Enter a parse tree produced by Cobol85Parser#qualifiedInData.
    def enterQualifiedInData(self, ctx:Cobol85Parser.QualifiedInDataContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inData.
    def enterInData(self, ctx:Cobol85Parser.InDataContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inFile.
    def enterInFile(self, ctx:Cobol85Parser.InFileContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inMnemonic.
    def enterInMnemonic(self, ctx:Cobol85Parser.InMnemonicContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inSection.
    def enterInSection(self, ctx:Cobol85Parser.InSectionContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inLibrary.
    def enterInLibrary(self, ctx:Cobol85Parser.InLibraryContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#inTable.
    def enterInTable(self, ctx:Cobol85Parser.InTableContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#alphabetName.
    def enterAlphabetName(self, ctx:Cobol85Parser.AlphabetNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#assignmentName.
    def enterAssignmentName(self, ctx:Cobol85Parser.AssignmentNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#basisName.
    def enterBasisName(self, ctx:Cobol85Parser.BasisNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#cdName.
    def enterCdName(self, ctx:Cobol85Parser.CdNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#className.
    def enterClassName(self, ctx:Cobol85Parser.ClassNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#computerName.
    def enterComputerName(self, ctx:Cobol85Parser.ComputerNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#conditionName.
    def enterConditionName(self, ctx:Cobol85Parser.ConditionNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#dataName.
    def enterDataName(self, ctx:Cobol85Parser.DataNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#dataDescName.
    def enterDataDescName(self, ctx:Cobol85Parser.DataDescNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#environmentName.
    def enterEnvironmentName(self, ctx:Cobol85Parser.EnvironmentNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#fileName.
    def enterFileName(self, ctx:Cobol85Parser.FileNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#functionName.
    def enterFunctionName(self, ctx:Cobol85Parser.FunctionNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#indexName.
    def enterIndexName(self, ctx:Cobol85Parser.IndexNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#languageName.
    def enterLanguageName(self, ctx:Cobol85Parser.LanguageNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#libraryName.
    def enterLibraryName(self, ctx:Cobol85Parser.LibraryNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#localName.
    def enterLocalName(self, ctx:Cobol85Parser.LocalNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#mnemonicName.
    def enterMnemonicName(self, ctx:Cobol85Parser.MnemonicNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#paragraphName.
    def enterParagraphName(self, ctx:Cobol85Parser.ParagraphNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#procedureName.
    def enterProcedureName(self, ctx:Cobol85Parser.ProcedureNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#programName.
    def enterProgramName(self, ctx:Cobol85Parser.ProgramNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#recordName.
    def enterRecordName(self, ctx:Cobol85Parser.RecordNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#reportName.
    def enterReportName(self, ctx:Cobol85Parser.ReportNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#routineName.
    def enterRoutineName(self, ctx:Cobol85Parser.RoutineNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#screenName.
    def enterScreenName(self, ctx:Cobol85Parser.ScreenNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#sectionName.
    def enterSectionName(self, ctx:Cobol85Parser.SectionNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#systemName.
    def enterSystemName(self, ctx:Cobol85Parser.SystemNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#symbolicCharacter.
    def enterSymbolicCharacter(self, ctx:Cobol85Parser.SymbolicCharacterContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#textName.
    def enterTextName(self, ctx:Cobol85Parser.TextNameContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#cobolWord.
    def enterCobolWord(self, ctx:Cobol85Parser.CobolWordContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#literal.
    def enterLiteral(self, ctx:Cobol85Parser.LiteralContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:Cobol85Parser.BooleanLiteralContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#numericLiteral.
    def enterNumericLiteral(self, ctx:Cobol85Parser.NumericLiteralContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#integerLiteral.
    def enterIntegerLiteral(self, ctx:Cobol85Parser.IntegerLiteralContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#cicsDfhRespLiteral.
    def enterCicsDfhRespLiteral(self, ctx:Cobol85Parser.CicsDfhRespLiteralContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#cicsDfhValueLiteral.
    def enterCicsDfhValueLiteral(self, ctx:Cobol85Parser.CicsDfhValueLiteralContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#figurativeConstant.
    def enterFigurativeConstant(self, ctx:Cobol85Parser.FigurativeConstantContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#specialRegister.
    def enterSpecialRegister(self, ctx:Cobol85Parser.SpecialRegisterContext):
        pass

    # Enter a parse tree produced by Cobol85Parser#commentEntry.
    def enterCommentEntry(self, ctx:Cobol85Parser.CommentEntryContext):
        pass