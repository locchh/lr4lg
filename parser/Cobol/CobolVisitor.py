# Generated from parser/Cobol/Cobol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CobolParser import CobolParser
else:
    from CobolParser import CobolParser

# This class defines a complete generic visitor for a parse tree produced by CobolParser.

class CobolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CobolParser#startRule.
    def visitStartRule(self, ctx:CobolParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#compilationUnit.
    def visitCompilationUnit(self, ctx:CobolParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#programUnit.
    def visitProgramUnit(self, ctx:CobolParser.ProgramUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#endProgramStatement.
    def visitEndProgramStatement(self, ctx:CobolParser.EndProgramStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#identificationDivision.
    def visitIdentificationDivision(self, ctx:CobolParser.IdentificationDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#identificationDivisionBody.
    def visitIdentificationDivisionBody(self, ctx:CobolParser.IdentificationDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#programIdParagraph.
    def visitProgramIdParagraph(self, ctx:CobolParser.ProgramIdParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#authorParagraph.
    def visitAuthorParagraph(self, ctx:CobolParser.AuthorParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#installationParagraph.
    def visitInstallationParagraph(self, ctx:CobolParser.InstallationParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dateWrittenParagraph.
    def visitDateWrittenParagraph(self, ctx:CobolParser.DateWrittenParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dateCompiledParagraph.
    def visitDateCompiledParagraph(self, ctx:CobolParser.DateCompiledParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#securityParagraph.
    def visitSecurityParagraph(self, ctx:CobolParser.SecurityParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#remarksParagraph.
    def visitRemarksParagraph(self, ctx:CobolParser.RemarksParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#environmentDivision.
    def visitEnvironmentDivision(self, ctx:CobolParser.EnvironmentDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#environmentDivisionBody.
    def visitEnvironmentDivisionBody(self, ctx:CobolParser.EnvironmentDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#configurationSection.
    def visitConfigurationSection(self, ctx:CobolParser.ConfigurationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#configurationSectionParagraph.
    def visitConfigurationSectionParagraph(self, ctx:CobolParser.ConfigurationSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sourceComputerParagraph.
    def visitSourceComputerParagraph(self, ctx:CobolParser.SourceComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#objectComputerParagraph.
    def visitObjectComputerParagraph(self, ctx:CobolParser.ObjectComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#objectComputerClause.
    def visitObjectComputerClause(self, ctx:CobolParser.ObjectComputerClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#memorySizeClause.
    def visitMemorySizeClause(self, ctx:CobolParser.MemorySizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#diskSizeClause.
    def visitDiskSizeClause(self, ctx:CobolParser.DiskSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#collatingSequenceClause.
    def visitCollatingSequenceClause(self, ctx:CobolParser.CollatingSequenceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#collatingSequenceClauseAlphanumeric.
    def visitCollatingSequenceClauseAlphanumeric(self, ctx:CobolParser.CollatingSequenceClauseAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#collatingSequenceClauseNational.
    def visitCollatingSequenceClauseNational(self, ctx:CobolParser.CollatingSequenceClauseNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#segmentLimitClause.
    def visitSegmentLimitClause(self, ctx:CobolParser.SegmentLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#characterSetClause.
    def visitCharacterSetClause(self, ctx:CobolParser.CharacterSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#specialNamesParagraph.
    def visitSpecialNamesParagraph(self, ctx:CobolParser.SpecialNamesParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#specialNameClause.
    def visitSpecialNameClause(self, ctx:CobolParser.SpecialNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alphabetClause.
    def visitAlphabetClause(self, ctx:CobolParser.AlphabetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alphabetClauseFormat1.
    def visitAlphabetClauseFormat1(self, ctx:CobolParser.AlphabetClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alphabetLiterals.
    def visitAlphabetLiterals(self, ctx:CobolParser.AlphabetLiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alphabetThrough.
    def visitAlphabetThrough(self, ctx:CobolParser.AlphabetThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alphabetAlso.
    def visitAlphabetAlso(self, ctx:CobolParser.AlphabetAlsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alphabetClauseFormat2.
    def visitAlphabetClauseFormat2(self, ctx:CobolParser.AlphabetClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#channelClause.
    def visitChannelClause(self, ctx:CobolParser.ChannelClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#classClause.
    def visitClassClause(self, ctx:CobolParser.ClassClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#classClauseThrough.
    def visitClassClauseThrough(self, ctx:CobolParser.ClassClauseThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#classClauseFrom.
    def visitClassClauseFrom(self, ctx:CobolParser.ClassClauseFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#classClauseTo.
    def visitClassClauseTo(self, ctx:CobolParser.ClassClauseToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#currencySignClause.
    def visitCurrencySignClause(self, ctx:CobolParser.CurrencySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#decimalPointClause.
    def visitDecimalPointClause(self, ctx:CobolParser.DecimalPointClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#defaultComputationalSignClause.
    def visitDefaultComputationalSignClause(self, ctx:CobolParser.DefaultComputationalSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#defaultDisplaySignClause.
    def visitDefaultDisplaySignClause(self, ctx:CobolParser.DefaultDisplaySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#environmentSwitchNameClause.
    def visitEnvironmentSwitchNameClause(self, ctx:CobolParser.EnvironmentSwitchNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def visitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CobolParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#odtClause.
    def visitOdtClause(self, ctx:CobolParser.OdtClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reserveNetworkClause.
    def visitReserveNetworkClause(self, ctx:CobolParser.ReserveNetworkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#symbolicCharactersClause.
    def visitSymbolicCharactersClause(self, ctx:CobolParser.SymbolicCharactersClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#symbolicCharacters.
    def visitSymbolicCharacters(self, ctx:CobolParser.SymbolicCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inputOutputSection.
    def visitInputOutputSection(self, ctx:CobolParser.InputOutputSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inputOutputSectionParagraph.
    def visitInputOutputSectionParagraph(self, ctx:CobolParser.InputOutputSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileControlParagraph.
    def visitFileControlParagraph(self, ctx:CobolParser.FileControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileControlEntry.
    def visitFileControlEntry(self, ctx:CobolParser.FileControlEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#selectClause.
    def visitSelectClause(self, ctx:CobolParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileControlClause.
    def visitFileControlClause(self, ctx:CobolParser.FileControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#assignClause.
    def visitAssignClause(self, ctx:CobolParser.AssignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reserveClause.
    def visitReserveClause(self, ctx:CobolParser.ReserveClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#organizationClause.
    def visitOrganizationClause(self, ctx:CobolParser.OrganizationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#paddingCharacterClause.
    def visitPaddingCharacterClause(self, ctx:CobolParser.PaddingCharacterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#recordDelimiterClause.
    def visitRecordDelimiterClause(self, ctx:CobolParser.RecordDelimiterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#accessModeClause.
    def visitAccessModeClause(self, ctx:CobolParser.AccessModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#recordKeyClause.
    def visitRecordKeyClause(self, ctx:CobolParser.RecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alternateRecordKeyClause.
    def visitAlternateRecordKeyClause(self, ctx:CobolParser.AlternateRecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#passwordClause.
    def visitPasswordClause(self, ctx:CobolParser.PasswordClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileStatusClause.
    def visitFileStatusClause(self, ctx:CobolParser.FileStatusClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#relativeKeyClause.
    def visitRelativeKeyClause(self, ctx:CobolParser.RelativeKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#ioControlParagraph.
    def visitIoControlParagraph(self, ctx:CobolParser.IoControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#ioControlClause.
    def visitIoControlClause(self, ctx:CobolParser.IoControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#rerunClause.
    def visitRerunClause(self, ctx:CobolParser.RerunClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#rerunEveryRecords.
    def visitRerunEveryRecords(self, ctx:CobolParser.RerunEveryRecordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#rerunEveryOf.
    def visitRerunEveryOf(self, ctx:CobolParser.RerunEveryOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#rerunEveryClock.
    def visitRerunEveryClock(self, ctx:CobolParser.RerunEveryClockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sameClause.
    def visitSameClause(self, ctx:CobolParser.SameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multipleFileClause.
    def visitMultipleFileClause(self, ctx:CobolParser.MultipleFileClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multipleFilePosition.
    def visitMultipleFilePosition(self, ctx:CobolParser.MultipleFilePositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#commitmentControlClause.
    def visitCommitmentControlClause(self, ctx:CobolParser.CommitmentControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDivision.
    def visitDataDivision(self, ctx:CobolParser.DataDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDivisionSection.
    def visitDataDivisionSection(self, ctx:CobolParser.DataDivisionSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileSection.
    def visitFileSection(self, ctx:CobolParser.FileSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileDescriptionEntry.
    def visitFileDescriptionEntry(self, ctx:CobolParser.FileDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileDescriptionEntryClause.
    def visitFileDescriptionEntryClause(self, ctx:CobolParser.FileDescriptionEntryClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#externalClause.
    def visitExternalClause(self, ctx:CobolParser.ExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#globalClause.
    def visitGlobalClause(self, ctx:CobolParser.GlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#blockContainsClause.
    def visitBlockContainsClause(self, ctx:CobolParser.BlockContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#blockContainsTo.
    def visitBlockContainsTo(self, ctx:CobolParser.BlockContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#recordContainsClause.
    def visitRecordContainsClause(self, ctx:CobolParser.RecordContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#recordContainsClauseFormat1.
    def visitRecordContainsClauseFormat1(self, ctx:CobolParser.RecordContainsClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#recordContainsClauseFormat2.
    def visitRecordContainsClauseFormat2(self, ctx:CobolParser.RecordContainsClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#recordContainsClauseFormat3.
    def visitRecordContainsClauseFormat3(self, ctx:CobolParser.RecordContainsClauseFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#recordContainsTo.
    def visitRecordContainsTo(self, ctx:CobolParser.RecordContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#labelRecordsClause.
    def visitLabelRecordsClause(self, ctx:CobolParser.LabelRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#valueOfClause.
    def visitValueOfClause(self, ctx:CobolParser.ValueOfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#valuePair.
    def visitValuePair(self, ctx:CobolParser.ValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataRecordsClause.
    def visitDataRecordsClause(self, ctx:CobolParser.DataRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#linageClause.
    def visitLinageClause(self, ctx:CobolParser.LinageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#linageAt.
    def visitLinageAt(self, ctx:CobolParser.LinageAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#linageFootingAt.
    def visitLinageFootingAt(self, ctx:CobolParser.LinageFootingAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#linageLinesAtTop.
    def visitLinageLinesAtTop(self, ctx:CobolParser.LinageLinesAtTopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#linageLinesAtBottom.
    def visitLinageLinesAtBottom(self, ctx:CobolParser.LinageLinesAtBottomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#recordingModeClause.
    def visitRecordingModeClause(self, ctx:CobolParser.RecordingModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#modeStatement.
    def visitModeStatement(self, ctx:CobolParser.ModeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#codeSetClause.
    def visitCodeSetClause(self, ctx:CobolParser.CodeSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportClause.
    def visitReportClause(self, ctx:CobolParser.ReportClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataBaseSection.
    def visitDataBaseSection(self, ctx:CobolParser.DataBaseSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataBaseSectionEntry.
    def visitDataBaseSectionEntry(self, ctx:CobolParser.DataBaseSectionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#workingStorageSection.
    def visitWorkingStorageSection(self, ctx:CobolParser.WorkingStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#linkageSection.
    def visitLinkageSection(self, ctx:CobolParser.LinkageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#communicationSection.
    def visitCommunicationSection(self, ctx:CobolParser.CommunicationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#communicationDescriptionEntry.
    def visitCommunicationDescriptionEntry(self, ctx:CobolParser.CommunicationDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#communicationDescriptionEntryFormat1.
    def visitCommunicationDescriptionEntryFormat1(self, ctx:CobolParser.CommunicationDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#communicationDescriptionEntryFormat2.
    def visitCommunicationDescriptionEntryFormat2(self, ctx:CobolParser.CommunicationDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#communicationDescriptionEntryFormat3.
    def visitCommunicationDescriptionEntryFormat3(self, ctx:CobolParser.CommunicationDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#destinationCountClause.
    def visitDestinationCountClause(self, ctx:CobolParser.DestinationCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#destinationTableClause.
    def visitDestinationTableClause(self, ctx:CobolParser.DestinationTableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#endKeyClause.
    def visitEndKeyClause(self, ctx:CobolParser.EndKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#errorKeyClause.
    def visitErrorKeyClause(self, ctx:CobolParser.ErrorKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#messageCountClause.
    def visitMessageCountClause(self, ctx:CobolParser.MessageCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#messageDateClause.
    def visitMessageDateClause(self, ctx:CobolParser.MessageDateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#messageTimeClause.
    def visitMessageTimeClause(self, ctx:CobolParser.MessageTimeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#statusKeyClause.
    def visitStatusKeyClause(self, ctx:CobolParser.StatusKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#symbolicDestinationClause.
    def visitSymbolicDestinationClause(self, ctx:CobolParser.SymbolicDestinationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#symbolicQueueClause.
    def visitSymbolicQueueClause(self, ctx:CobolParser.SymbolicQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#symbolicSourceClause.
    def visitSymbolicSourceClause(self, ctx:CobolParser.SymbolicSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#symbolicTerminalClause.
    def visitSymbolicTerminalClause(self, ctx:CobolParser.SymbolicTerminalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#symbolicSubQueueClause.
    def visitSymbolicSubQueueClause(self, ctx:CobolParser.SymbolicSubQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#textLengthClause.
    def visitTextLengthClause(self, ctx:CobolParser.TextLengthClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#localStorageSection.
    def visitLocalStorageSection(self, ctx:CobolParser.LocalStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenSection.
    def visitScreenSection(self, ctx:CobolParser.ScreenSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionEntry.
    def visitScreenDescriptionEntry(self, ctx:CobolParser.ScreenDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionBlankClause.
    def visitScreenDescriptionBlankClause(self, ctx:CobolParser.ScreenDescriptionBlankClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionBellClause.
    def visitScreenDescriptionBellClause(self, ctx:CobolParser.ScreenDescriptionBellClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionBlinkClause.
    def visitScreenDescriptionBlinkClause(self, ctx:CobolParser.ScreenDescriptionBlinkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionEraseClause.
    def visitScreenDescriptionEraseClause(self, ctx:CobolParser.ScreenDescriptionEraseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionLightClause.
    def visitScreenDescriptionLightClause(self, ctx:CobolParser.ScreenDescriptionLightClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionGridClause.
    def visitScreenDescriptionGridClause(self, ctx:CobolParser.ScreenDescriptionGridClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionReverseVideoClause.
    def visitScreenDescriptionReverseVideoClause(self, ctx:CobolParser.ScreenDescriptionReverseVideoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionUnderlineClause.
    def visitScreenDescriptionUnderlineClause(self, ctx:CobolParser.ScreenDescriptionUnderlineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionSizeClause.
    def visitScreenDescriptionSizeClause(self, ctx:CobolParser.ScreenDescriptionSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionLineClause.
    def visitScreenDescriptionLineClause(self, ctx:CobolParser.ScreenDescriptionLineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionColumnClause.
    def visitScreenDescriptionColumnClause(self, ctx:CobolParser.ScreenDescriptionColumnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionForegroundColorClause.
    def visitScreenDescriptionForegroundColorClause(self, ctx:CobolParser.ScreenDescriptionForegroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionBackgroundColorClause.
    def visitScreenDescriptionBackgroundColorClause(self, ctx:CobolParser.ScreenDescriptionBackgroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionControlClause.
    def visitScreenDescriptionControlClause(self, ctx:CobolParser.ScreenDescriptionControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionValueClause.
    def visitScreenDescriptionValueClause(self, ctx:CobolParser.ScreenDescriptionValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionPictureClause.
    def visitScreenDescriptionPictureClause(self, ctx:CobolParser.ScreenDescriptionPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionFromClause.
    def visitScreenDescriptionFromClause(self, ctx:CobolParser.ScreenDescriptionFromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionToClause.
    def visitScreenDescriptionToClause(self, ctx:CobolParser.ScreenDescriptionToClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionUsingClause.
    def visitScreenDescriptionUsingClause(self, ctx:CobolParser.ScreenDescriptionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionUsageClause.
    def visitScreenDescriptionUsageClause(self, ctx:CobolParser.ScreenDescriptionUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionBlankWhenZeroClause.
    def visitScreenDescriptionBlankWhenZeroClause(self, ctx:CobolParser.ScreenDescriptionBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionJustifiedClause.
    def visitScreenDescriptionJustifiedClause(self, ctx:CobolParser.ScreenDescriptionJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionSignClause.
    def visitScreenDescriptionSignClause(self, ctx:CobolParser.ScreenDescriptionSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionAutoClause.
    def visitScreenDescriptionAutoClause(self, ctx:CobolParser.ScreenDescriptionAutoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionSecureClause.
    def visitScreenDescriptionSecureClause(self, ctx:CobolParser.ScreenDescriptionSecureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionRequiredClause.
    def visitScreenDescriptionRequiredClause(self, ctx:CobolParser.ScreenDescriptionRequiredClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionPromptClause.
    def visitScreenDescriptionPromptClause(self, ctx:CobolParser.ScreenDescriptionPromptClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionPromptOccursClause.
    def visitScreenDescriptionPromptOccursClause(self, ctx:CobolParser.ScreenDescriptionPromptOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionFullClause.
    def visitScreenDescriptionFullClause(self, ctx:CobolParser.ScreenDescriptionFullClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenDescriptionZeroFillClause.
    def visitScreenDescriptionZeroFillClause(self, ctx:CobolParser.ScreenDescriptionZeroFillClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportSection.
    def visitReportSection(self, ctx:CobolParser.ReportSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportDescription.
    def visitReportDescription(self, ctx:CobolParser.ReportDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportDescriptionEntry.
    def visitReportDescriptionEntry(self, ctx:CobolParser.ReportDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportDescriptionGlobalClause.
    def visitReportDescriptionGlobalClause(self, ctx:CobolParser.ReportDescriptionGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportDescriptionPageLimitClause.
    def visitReportDescriptionPageLimitClause(self, ctx:CobolParser.ReportDescriptionPageLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportDescriptionHeadingClause.
    def visitReportDescriptionHeadingClause(self, ctx:CobolParser.ReportDescriptionHeadingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportDescriptionFirstDetailClause.
    def visitReportDescriptionFirstDetailClause(self, ctx:CobolParser.ReportDescriptionFirstDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportDescriptionLastDetailClause.
    def visitReportDescriptionLastDetailClause(self, ctx:CobolParser.ReportDescriptionLastDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportDescriptionFootingClause.
    def visitReportDescriptionFootingClause(self, ctx:CobolParser.ReportDescriptionFootingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupDescriptionEntry.
    def visitReportGroupDescriptionEntry(self, ctx:CobolParser.ReportGroupDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupDescriptionEntryFormat1.
    def visitReportGroupDescriptionEntryFormat1(self, ctx:CobolParser.ReportGroupDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupDescriptionEntryFormat2.
    def visitReportGroupDescriptionEntryFormat2(self, ctx:CobolParser.ReportGroupDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupDescriptionEntryFormat3.
    def visitReportGroupDescriptionEntryFormat3(self, ctx:CobolParser.ReportGroupDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupBlankWhenZeroClause.
    def visitReportGroupBlankWhenZeroClause(self, ctx:CobolParser.ReportGroupBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupColumnNumberClause.
    def visitReportGroupColumnNumberClause(self, ctx:CobolParser.ReportGroupColumnNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupIndicateClause.
    def visitReportGroupIndicateClause(self, ctx:CobolParser.ReportGroupIndicateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupJustifiedClause.
    def visitReportGroupJustifiedClause(self, ctx:CobolParser.ReportGroupJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupLineNumberClause.
    def visitReportGroupLineNumberClause(self, ctx:CobolParser.ReportGroupLineNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupLineNumberNextPage.
    def visitReportGroupLineNumberNextPage(self, ctx:CobolParser.ReportGroupLineNumberNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupLineNumberPlus.
    def visitReportGroupLineNumberPlus(self, ctx:CobolParser.ReportGroupLineNumberPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupNextGroupClause.
    def visitReportGroupNextGroupClause(self, ctx:CobolParser.ReportGroupNextGroupClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupNextGroupPlus.
    def visitReportGroupNextGroupPlus(self, ctx:CobolParser.ReportGroupNextGroupPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupNextGroupNextPage.
    def visitReportGroupNextGroupNextPage(self, ctx:CobolParser.ReportGroupNextGroupNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupPictureClause.
    def visitReportGroupPictureClause(self, ctx:CobolParser.ReportGroupPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupResetClause.
    def visitReportGroupResetClause(self, ctx:CobolParser.ReportGroupResetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupSignClause.
    def visitReportGroupSignClause(self, ctx:CobolParser.ReportGroupSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupSourceClause.
    def visitReportGroupSourceClause(self, ctx:CobolParser.ReportGroupSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupSumClause.
    def visitReportGroupSumClause(self, ctx:CobolParser.ReportGroupSumClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupTypeClause.
    def visitReportGroupTypeClause(self, ctx:CobolParser.ReportGroupTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupTypeReportHeading.
    def visitReportGroupTypeReportHeading(self, ctx:CobolParser.ReportGroupTypeReportHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupTypePageHeading.
    def visitReportGroupTypePageHeading(self, ctx:CobolParser.ReportGroupTypePageHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupTypeControlHeading.
    def visitReportGroupTypeControlHeading(self, ctx:CobolParser.ReportGroupTypeControlHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupTypeDetail.
    def visitReportGroupTypeDetail(self, ctx:CobolParser.ReportGroupTypeDetailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupTypeControlFooting.
    def visitReportGroupTypeControlFooting(self, ctx:CobolParser.ReportGroupTypeControlFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupUsageClause.
    def visitReportGroupUsageClause(self, ctx:CobolParser.ReportGroupUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupTypePageFooting.
    def visitReportGroupTypePageFooting(self, ctx:CobolParser.ReportGroupTypePageFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupTypeReportFooting.
    def visitReportGroupTypeReportFooting(self, ctx:CobolParser.ReportGroupTypeReportFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportGroupValueClause.
    def visitReportGroupValueClause(self, ctx:CobolParser.ReportGroupValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#programLibrarySection.
    def visitProgramLibrarySection(self, ctx:CobolParser.ProgramLibrarySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryDescriptionEntry.
    def visitLibraryDescriptionEntry(self, ctx:CobolParser.LibraryDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryDescriptionEntryFormat1.
    def visitLibraryDescriptionEntryFormat1(self, ctx:CobolParser.LibraryDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryDescriptionEntryFormat2.
    def visitLibraryDescriptionEntryFormat2(self, ctx:CobolParser.LibraryDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryAttributeClauseFormat1.
    def visitLibraryAttributeClauseFormat1(self, ctx:CobolParser.LibraryAttributeClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryAttributeClauseFormat2.
    def visitLibraryAttributeClauseFormat2(self, ctx:CobolParser.LibraryAttributeClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryAttributeFunction.
    def visitLibraryAttributeFunction(self, ctx:CobolParser.LibraryAttributeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryAttributeParameter.
    def visitLibraryAttributeParameter(self, ctx:CobolParser.LibraryAttributeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryAttributeTitle.
    def visitLibraryAttributeTitle(self, ctx:CobolParser.LibraryAttributeTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryEntryProcedureClauseFormat1.
    def visitLibraryEntryProcedureClauseFormat1(self, ctx:CobolParser.LibraryEntryProcedureClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryEntryProcedureClauseFormat2.
    def visitLibraryEntryProcedureClauseFormat2(self, ctx:CobolParser.LibraryEntryProcedureClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryEntryProcedureForClause.
    def visitLibraryEntryProcedureForClause(self, ctx:CobolParser.LibraryEntryProcedureForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryEntryProcedureGivingClause.
    def visitLibraryEntryProcedureGivingClause(self, ctx:CobolParser.LibraryEntryProcedureGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryEntryProcedureUsingClause.
    def visitLibraryEntryProcedureUsingClause(self, ctx:CobolParser.LibraryEntryProcedureUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryEntryProcedureUsingName.
    def visitLibraryEntryProcedureUsingName(self, ctx:CobolParser.LibraryEntryProcedureUsingNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryEntryProcedureWithClause.
    def visitLibraryEntryProcedureWithClause(self, ctx:CobolParser.LibraryEntryProcedureWithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryEntryProcedureWithName.
    def visitLibraryEntryProcedureWithName(self, ctx:CobolParser.LibraryEntryProcedureWithNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryIsCommonClause.
    def visitLibraryIsCommonClause(self, ctx:CobolParser.LibraryIsCommonClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryIsGlobalClause.
    def visitLibraryIsGlobalClause(self, ctx:CobolParser.LibraryIsGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDescriptionEntry.
    def visitDataDescriptionEntry(self, ctx:CobolParser.DataDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDescriptionEntryFormat1.
    def visitDataDescriptionEntryFormat1(self, ctx:CobolParser.DataDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDescriptionEntryFormat2.
    def visitDataDescriptionEntryFormat2(self, ctx:CobolParser.DataDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDescriptionEntryFormat3.
    def visitDataDescriptionEntryFormat3(self, ctx:CobolParser.DataDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDescriptionEntryExecSql.
    def visitDataDescriptionEntryExecSql(self, ctx:CobolParser.DataDescriptionEntryExecSqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataAlignedClause.
    def visitDataAlignedClause(self, ctx:CobolParser.DataAlignedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataBlankWhenZeroClause.
    def visitDataBlankWhenZeroClause(self, ctx:CobolParser.DataBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataCommonOwnLocalClause.
    def visitDataCommonOwnLocalClause(self, ctx:CobolParser.DataCommonOwnLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataExternalClause.
    def visitDataExternalClause(self, ctx:CobolParser.DataExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataGlobalClause.
    def visitDataGlobalClause(self, ctx:CobolParser.DataGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataIntegerStringClause.
    def visitDataIntegerStringClause(self, ctx:CobolParser.DataIntegerStringClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataJustifiedClause.
    def visitDataJustifiedClause(self, ctx:CobolParser.DataJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataOccursClause.
    def visitDataOccursClause(self, ctx:CobolParser.DataOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataOccursTo.
    def visitDataOccursTo(self, ctx:CobolParser.DataOccursToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataOccursDepending.
    def visitDataOccursDepending(self, ctx:CobolParser.DataOccursDependingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataOccursSort.
    def visitDataOccursSort(self, ctx:CobolParser.DataOccursSortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataOccursIndexed.
    def visitDataOccursIndexed(self, ctx:CobolParser.DataOccursIndexedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataPictureClause.
    def visitDataPictureClause(self, ctx:CobolParser.DataPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#pictureString.
    def visitPictureString(self, ctx:CobolParser.PictureStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#pictureChars.
    def visitPictureChars(self, ctx:CobolParser.PictureCharsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#pictureCardinality.
    def visitPictureCardinality(self, ctx:CobolParser.PictureCardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataReceivedByClause.
    def visitDataReceivedByClause(self, ctx:CobolParser.DataReceivedByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataRecordAreaClause.
    def visitDataRecordAreaClause(self, ctx:CobolParser.DataRecordAreaClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataRedefinesClause.
    def visitDataRedefinesClause(self, ctx:CobolParser.DataRedefinesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataRenamesClause.
    def visitDataRenamesClause(self, ctx:CobolParser.DataRenamesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataSignClause.
    def visitDataSignClause(self, ctx:CobolParser.DataSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataSynchronizedClause.
    def visitDataSynchronizedClause(self, ctx:CobolParser.DataSynchronizedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataThreadLocalClause.
    def visitDataThreadLocalClause(self, ctx:CobolParser.DataThreadLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataTypeClause.
    def visitDataTypeClause(self, ctx:CobolParser.DataTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataTypeDefClause.
    def visitDataTypeDefClause(self, ctx:CobolParser.DataTypeDefClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataUsageClause.
    def visitDataUsageClause(self, ctx:CobolParser.DataUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataUsingClause.
    def visitDataUsingClause(self, ctx:CobolParser.DataUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataValueClause.
    def visitDataValueClause(self, ctx:CobolParser.DataValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataValueInterval.
    def visitDataValueInterval(self, ctx:CobolParser.DataValueIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataValueIntervalFrom.
    def visitDataValueIntervalFrom(self, ctx:CobolParser.DataValueIntervalFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataValueIntervalTo.
    def visitDataValueIntervalTo(self, ctx:CobolParser.DataValueIntervalToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataWithLowerBoundsClause.
    def visitDataWithLowerBoundsClause(self, ctx:CobolParser.DataWithLowerBoundsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivision.
    def visitProcedureDivision(self, ctx:CobolParser.ProcedureDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivisionUsingClause.
    def visitProcedureDivisionUsingClause(self, ctx:CobolParser.ProcedureDivisionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivisionGivingClause.
    def visitProcedureDivisionGivingClause(self, ctx:CobolParser.ProcedureDivisionGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivisionUsingParameter.
    def visitProcedureDivisionUsingParameter(self, ctx:CobolParser.ProcedureDivisionUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivisionByReferencePhrase.
    def visitProcedureDivisionByReferencePhrase(self, ctx:CobolParser.ProcedureDivisionByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivisionByReference.
    def visitProcedureDivisionByReference(self, ctx:CobolParser.ProcedureDivisionByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivisionByValuePhrase.
    def visitProcedureDivisionByValuePhrase(self, ctx:CobolParser.ProcedureDivisionByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivisionByValue.
    def visitProcedureDivisionByValue(self, ctx:CobolParser.ProcedureDivisionByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDeclaratives.
    def visitProcedureDeclaratives(self, ctx:CobolParser.ProcedureDeclarativesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDeclarative.
    def visitProcedureDeclarative(self, ctx:CobolParser.ProcedureDeclarativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureSectionHeader.
    def visitProcedureSectionHeader(self, ctx:CobolParser.ProcedureSectionHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureDivisionBody.
    def visitProcedureDivisionBody(self, ctx:CobolParser.ProcedureDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureSection.
    def visitProcedureSection(self, ctx:CobolParser.ProcedureSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#paragraphs.
    def visitParagraphs(self, ctx:CobolParser.ParagraphsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#paragraph.
    def visitParagraph(self, ctx:CobolParser.ParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sentence.
    def visitSentence(self, ctx:CobolParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#statement.
    def visitStatement(self, ctx:CobolParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#acceptStatement.
    def visitAcceptStatement(self, ctx:CobolParser.AcceptStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#acceptFromDateStatement.
    def visitAcceptFromDateStatement(self, ctx:CobolParser.AcceptFromDateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#acceptFromMnemonicStatement.
    def visitAcceptFromMnemonicStatement(self, ctx:CobolParser.AcceptFromMnemonicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#acceptFromEscapeKeyStatement.
    def visitAcceptFromEscapeKeyStatement(self, ctx:CobolParser.AcceptFromEscapeKeyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#acceptMessageCountStatement.
    def visitAcceptMessageCountStatement(self, ctx:CobolParser.AcceptMessageCountStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#addStatement.
    def visitAddStatement(self, ctx:CobolParser.AddStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#addToStatement.
    def visitAddToStatement(self, ctx:CobolParser.AddToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#addToGivingStatement.
    def visitAddToGivingStatement(self, ctx:CobolParser.AddToGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#addCorrespondingStatement.
    def visitAddCorrespondingStatement(self, ctx:CobolParser.AddCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#addFrom.
    def visitAddFrom(self, ctx:CobolParser.AddFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#addTo.
    def visitAddTo(self, ctx:CobolParser.AddToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#addToGiving.
    def visitAddToGiving(self, ctx:CobolParser.AddToGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#addGiving.
    def visitAddGiving(self, ctx:CobolParser.AddGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alteredGoTo.
    def visitAlteredGoTo(self, ctx:CobolParser.AlteredGoToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alterStatement.
    def visitAlterStatement(self, ctx:CobolParser.AlterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alterProceedTo.
    def visitAlterProceedTo(self, ctx:CobolParser.AlterProceedToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callStatement.
    def visitCallStatement(self, ctx:CobolParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callUsingPhrase.
    def visitCallUsingPhrase(self, ctx:CobolParser.CallUsingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callUsingParameter.
    def visitCallUsingParameter(self, ctx:CobolParser.CallUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callByReferencePhrase.
    def visitCallByReferencePhrase(self, ctx:CobolParser.CallByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callByReference.
    def visitCallByReference(self, ctx:CobolParser.CallByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callByValuePhrase.
    def visitCallByValuePhrase(self, ctx:CobolParser.CallByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callByValue.
    def visitCallByValue(self, ctx:CobolParser.CallByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callByContentPhrase.
    def visitCallByContentPhrase(self, ctx:CobolParser.CallByContentPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callByContent.
    def visitCallByContent(self, ctx:CobolParser.CallByContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#callGivingPhrase.
    def visitCallGivingPhrase(self, ctx:CobolParser.CallGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#cancelStatement.
    def visitCancelStatement(self, ctx:CobolParser.CancelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#cancelCall.
    def visitCancelCall(self, ctx:CobolParser.CancelCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#closeStatement.
    def visitCloseStatement(self, ctx:CobolParser.CloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#closeFile.
    def visitCloseFile(self, ctx:CobolParser.CloseFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#closeReelUnitStatement.
    def visitCloseReelUnitStatement(self, ctx:CobolParser.CloseReelUnitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#closeRelativeStatement.
    def visitCloseRelativeStatement(self, ctx:CobolParser.CloseRelativeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#closePortFileIOStatement.
    def visitClosePortFileIOStatement(self, ctx:CobolParser.ClosePortFileIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#closePortFileIOUsing.
    def visitClosePortFileIOUsing(self, ctx:CobolParser.ClosePortFileIOUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#closePortFileIOUsingCloseDisposition.
    def visitClosePortFileIOUsingCloseDisposition(self, ctx:CobolParser.ClosePortFileIOUsingCloseDispositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#closePortFileIOUsingAssociatedData.
    def visitClosePortFileIOUsingAssociatedData(self, ctx:CobolParser.ClosePortFileIOUsingAssociatedDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#closePortFileIOUsingAssociatedDataLength.
    def visitClosePortFileIOUsingAssociatedDataLength(self, ctx:CobolParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#computeStatement.
    def visitComputeStatement(self, ctx:CobolParser.ComputeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#computeStore.
    def visitComputeStore(self, ctx:CobolParser.ComputeStoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#continueStatement.
    def visitContinueStatement(self, ctx:CobolParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#deleteStatement.
    def visitDeleteStatement(self, ctx:CobolParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#disableStatement.
    def visitDisableStatement(self, ctx:CobolParser.DisableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#displayStatement.
    def visitDisplayStatement(self, ctx:CobolParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#displayOperand.
    def visitDisplayOperand(self, ctx:CobolParser.DisplayOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#displayAt.
    def visitDisplayAt(self, ctx:CobolParser.DisplayAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#displayUpon.
    def visitDisplayUpon(self, ctx:CobolParser.DisplayUponContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#displayWith.
    def visitDisplayWith(self, ctx:CobolParser.DisplayWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#divideStatement.
    def visitDivideStatement(self, ctx:CobolParser.DivideStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#divideIntoStatement.
    def visitDivideIntoStatement(self, ctx:CobolParser.DivideIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#divideIntoGivingStatement.
    def visitDivideIntoGivingStatement(self, ctx:CobolParser.DivideIntoGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#divideByGivingStatement.
    def visitDivideByGivingStatement(self, ctx:CobolParser.DivideByGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#divideGivingPhrase.
    def visitDivideGivingPhrase(self, ctx:CobolParser.DivideGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#divideInto.
    def visitDivideInto(self, ctx:CobolParser.DivideIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#divideGiving.
    def visitDivideGiving(self, ctx:CobolParser.DivideGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#divideRemainder.
    def visitDivideRemainder(self, ctx:CobolParser.DivideRemainderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#enableStatement.
    def visitEnableStatement(self, ctx:CobolParser.EnableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#entryStatement.
    def visitEntryStatement(self, ctx:CobolParser.EntryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateStatement.
    def visitEvaluateStatement(self, ctx:CobolParser.EvaluateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateSelect.
    def visitEvaluateSelect(self, ctx:CobolParser.EvaluateSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateAlsoSelect.
    def visitEvaluateAlsoSelect(self, ctx:CobolParser.EvaluateAlsoSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateWhenPhrase.
    def visitEvaluateWhenPhrase(self, ctx:CobolParser.EvaluateWhenPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateWhen.
    def visitEvaluateWhen(self, ctx:CobolParser.EvaluateWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateCondition.
    def visitEvaluateCondition(self, ctx:CobolParser.EvaluateConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateThrough.
    def visitEvaluateThrough(self, ctx:CobolParser.EvaluateThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateAlsoCondition.
    def visitEvaluateAlsoCondition(self, ctx:CobolParser.EvaluateAlsoConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateWhenOther.
    def visitEvaluateWhenOther(self, ctx:CobolParser.EvaluateWhenOtherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#evaluateValue.
    def visitEvaluateValue(self, ctx:CobolParser.EvaluateValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#execCicsStatement.
    def visitExecCicsStatement(self, ctx:CobolParser.ExecCicsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#execSqlStatement.
    def visitExecSqlStatement(self, ctx:CobolParser.ExecSqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#execSqlImsStatement.
    def visitExecSqlImsStatement(self, ctx:CobolParser.ExecSqlImsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#exhibitStatement.
    def visitExhibitStatement(self, ctx:CobolParser.ExhibitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#exhibitOperand.
    def visitExhibitOperand(self, ctx:CobolParser.ExhibitOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#exitStatement.
    def visitExitStatement(self, ctx:CobolParser.ExitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#generateStatement.
    def visitGenerateStatement(self, ctx:CobolParser.GenerateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#gobackStatement.
    def visitGobackStatement(self, ctx:CobolParser.GobackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#goToStatement.
    def visitGoToStatement(self, ctx:CobolParser.GoToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#goToStatementSimple.
    def visitGoToStatementSimple(self, ctx:CobolParser.GoToStatementSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#goToDependingOnStatement.
    def visitGoToDependingOnStatement(self, ctx:CobolParser.GoToDependingOnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#ifStatement.
    def visitIfStatement(self, ctx:CobolParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#ifThen.
    def visitIfThen(self, ctx:CobolParser.IfThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#ifElse.
    def visitIfElse(self, ctx:CobolParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#initializeStatement.
    def visitInitializeStatement(self, ctx:CobolParser.InitializeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#initializeReplacingPhrase.
    def visitInitializeReplacingPhrase(self, ctx:CobolParser.InitializeReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#initializeReplacingBy.
    def visitInitializeReplacingBy(self, ctx:CobolParser.InitializeReplacingByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#initiateStatement.
    def visitInitiateStatement(self, ctx:CobolParser.InitiateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectStatement.
    def visitInspectStatement(self, ctx:CobolParser.InspectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectTallyingPhrase.
    def visitInspectTallyingPhrase(self, ctx:CobolParser.InspectTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectReplacingPhrase.
    def visitInspectReplacingPhrase(self, ctx:CobolParser.InspectReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectTallyingReplacingPhrase.
    def visitInspectTallyingReplacingPhrase(self, ctx:CobolParser.InspectTallyingReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectConvertingPhrase.
    def visitInspectConvertingPhrase(self, ctx:CobolParser.InspectConvertingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectFor.
    def visitInspectFor(self, ctx:CobolParser.InspectForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectCharacters.
    def visitInspectCharacters(self, ctx:CobolParser.InspectCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectReplacingCharacters.
    def visitInspectReplacingCharacters(self, ctx:CobolParser.InspectReplacingCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectAllLeadings.
    def visitInspectAllLeadings(self, ctx:CobolParser.InspectAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectReplacingAllLeadings.
    def visitInspectReplacingAllLeadings(self, ctx:CobolParser.InspectReplacingAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectAllLeading.
    def visitInspectAllLeading(self, ctx:CobolParser.InspectAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectReplacingAllLeading.
    def visitInspectReplacingAllLeading(self, ctx:CobolParser.InspectReplacingAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectBy.
    def visitInspectBy(self, ctx:CobolParser.InspectByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectTo.
    def visitInspectTo(self, ctx:CobolParser.InspectToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inspectBeforeAfter.
    def visitInspectBeforeAfter(self, ctx:CobolParser.InspectBeforeAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeStatement.
    def visitMergeStatement(self, ctx:CobolParser.MergeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeOnKeyClause.
    def visitMergeOnKeyClause(self, ctx:CobolParser.MergeOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeCollatingSequencePhrase.
    def visitMergeCollatingSequencePhrase(self, ctx:CobolParser.MergeCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeCollatingAlphanumeric.
    def visitMergeCollatingAlphanumeric(self, ctx:CobolParser.MergeCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeCollatingNational.
    def visitMergeCollatingNational(self, ctx:CobolParser.MergeCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeUsing.
    def visitMergeUsing(self, ctx:CobolParser.MergeUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeOutputProcedurePhrase.
    def visitMergeOutputProcedurePhrase(self, ctx:CobolParser.MergeOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeOutputThrough.
    def visitMergeOutputThrough(self, ctx:CobolParser.MergeOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeGivingPhrase.
    def visitMergeGivingPhrase(self, ctx:CobolParser.MergeGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mergeGiving.
    def visitMergeGiving(self, ctx:CobolParser.MergeGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#moveStatement.
    def visitMoveStatement(self, ctx:CobolParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#moveToStatement.
    def visitMoveToStatement(self, ctx:CobolParser.MoveToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#moveToSendingArea.
    def visitMoveToSendingArea(self, ctx:CobolParser.MoveToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#moveCorrespondingToStatement.
    def visitMoveCorrespondingToStatement(self, ctx:CobolParser.MoveCorrespondingToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#moveCorrespondingToSendingArea.
    def visitMoveCorrespondingToSendingArea(self, ctx:CobolParser.MoveCorrespondingToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx:CobolParser.MultiplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multiplyRegular.
    def visitMultiplyRegular(self, ctx:CobolParser.MultiplyRegularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multiplyRegularOperand.
    def visitMultiplyRegularOperand(self, ctx:CobolParser.MultiplyRegularOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multiplyGiving.
    def visitMultiplyGiving(self, ctx:CobolParser.MultiplyGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multiplyGivingOperand.
    def visitMultiplyGivingOperand(self, ctx:CobolParser.MultiplyGivingOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multiplyGivingResult.
    def visitMultiplyGivingResult(self, ctx:CobolParser.MultiplyGivingResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#nextSentenceStatement.
    def visitNextSentenceStatement(self, ctx:CobolParser.NextSentenceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#openStatement.
    def visitOpenStatement(self, ctx:CobolParser.OpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#openInputStatement.
    def visitOpenInputStatement(self, ctx:CobolParser.OpenInputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#openInput.
    def visitOpenInput(self, ctx:CobolParser.OpenInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#openOutputStatement.
    def visitOpenOutputStatement(self, ctx:CobolParser.OpenOutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#openOutput.
    def visitOpenOutput(self, ctx:CobolParser.OpenOutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#openIOStatement.
    def visitOpenIOStatement(self, ctx:CobolParser.OpenIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#openExtendStatement.
    def visitOpenExtendStatement(self, ctx:CobolParser.OpenExtendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performStatement.
    def visitPerformStatement(self, ctx:CobolParser.PerformStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performInlineStatement.
    def visitPerformInlineStatement(self, ctx:CobolParser.PerformInlineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performProcedureStatement.
    def visitPerformProcedureStatement(self, ctx:CobolParser.PerformProcedureStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performType.
    def visitPerformType(self, ctx:CobolParser.PerformTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performTimes.
    def visitPerformTimes(self, ctx:CobolParser.PerformTimesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performUntil.
    def visitPerformUntil(self, ctx:CobolParser.PerformUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performVarying.
    def visitPerformVarying(self, ctx:CobolParser.PerformVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performVaryingClause.
    def visitPerformVaryingClause(self, ctx:CobolParser.PerformVaryingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performVaryingPhrase.
    def visitPerformVaryingPhrase(self, ctx:CobolParser.PerformVaryingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performAfter.
    def visitPerformAfter(self, ctx:CobolParser.PerformAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performFrom.
    def visitPerformFrom(self, ctx:CobolParser.PerformFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performBy.
    def visitPerformBy(self, ctx:CobolParser.PerformByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#performTestClause.
    def visitPerformTestClause(self, ctx:CobolParser.PerformTestClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#purgeStatement.
    def visitPurgeStatement(self, ctx:CobolParser.PurgeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#readStatement.
    def visitReadStatement(self, ctx:CobolParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#readInto.
    def visitReadInto(self, ctx:CobolParser.ReadIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#readWith.
    def visitReadWith(self, ctx:CobolParser.ReadWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#readKey.
    def visitReadKey(self, ctx:CobolParser.ReadKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveStatement.
    def visitReceiveStatement(self, ctx:CobolParser.ReceiveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveFromStatement.
    def visitReceiveFromStatement(self, ctx:CobolParser.ReceiveFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveFrom.
    def visitReceiveFrom(self, ctx:CobolParser.ReceiveFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveIntoStatement.
    def visitReceiveIntoStatement(self, ctx:CobolParser.ReceiveIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveNoData.
    def visitReceiveNoData(self, ctx:CobolParser.ReceiveNoDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveWithData.
    def visitReceiveWithData(self, ctx:CobolParser.ReceiveWithDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveBefore.
    def visitReceiveBefore(self, ctx:CobolParser.ReceiveBeforeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveWith.
    def visitReceiveWith(self, ctx:CobolParser.ReceiveWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveThread.
    def visitReceiveThread(self, ctx:CobolParser.ReceiveThreadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveSize.
    def visitReceiveSize(self, ctx:CobolParser.ReceiveSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#receiveStatus.
    def visitReceiveStatus(self, ctx:CobolParser.ReceiveStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#releaseStatement.
    def visitReleaseStatement(self, ctx:CobolParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#returnStatement.
    def visitReturnStatement(self, ctx:CobolParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#returnInto.
    def visitReturnInto(self, ctx:CobolParser.ReturnIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#rewriteStatement.
    def visitRewriteStatement(self, ctx:CobolParser.RewriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#rewriteFrom.
    def visitRewriteFrom(self, ctx:CobolParser.RewriteFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#searchStatement.
    def visitSearchStatement(self, ctx:CobolParser.SearchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#searchVarying.
    def visitSearchVarying(self, ctx:CobolParser.SearchVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#searchWhen.
    def visitSearchWhen(self, ctx:CobolParser.SearchWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendStatement.
    def visitSendStatement(self, ctx:CobolParser.SendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendStatementSync.
    def visitSendStatementSync(self, ctx:CobolParser.SendStatementSyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendStatementAsync.
    def visitSendStatementAsync(self, ctx:CobolParser.SendStatementAsyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendFromPhrase.
    def visitSendFromPhrase(self, ctx:CobolParser.SendFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendWithPhrase.
    def visitSendWithPhrase(self, ctx:CobolParser.SendWithPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendReplacingPhrase.
    def visitSendReplacingPhrase(self, ctx:CobolParser.SendReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendAdvancingPhrase.
    def visitSendAdvancingPhrase(self, ctx:CobolParser.SendAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendAdvancingPage.
    def visitSendAdvancingPage(self, ctx:CobolParser.SendAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendAdvancingLines.
    def visitSendAdvancingLines(self, ctx:CobolParser.SendAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sendAdvancingMnemonic.
    def visitSendAdvancingMnemonic(self, ctx:CobolParser.SendAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#setStatement.
    def visitSetStatement(self, ctx:CobolParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#setToStatement.
    def visitSetToStatement(self, ctx:CobolParser.SetToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#setUpDownByStatement.
    def visitSetUpDownByStatement(self, ctx:CobolParser.SetUpDownByStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#setTo.
    def visitSetTo(self, ctx:CobolParser.SetToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#setToValue.
    def visitSetToValue(self, ctx:CobolParser.SetToValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#setByValue.
    def visitSetByValue(self, ctx:CobolParser.SetByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortStatement.
    def visitSortStatement(self, ctx:CobolParser.SortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortOnKeyClause.
    def visitSortOnKeyClause(self, ctx:CobolParser.SortOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortDuplicatesPhrase.
    def visitSortDuplicatesPhrase(self, ctx:CobolParser.SortDuplicatesPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortCollatingSequencePhrase.
    def visitSortCollatingSequencePhrase(self, ctx:CobolParser.SortCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortCollatingAlphanumeric.
    def visitSortCollatingAlphanumeric(self, ctx:CobolParser.SortCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortCollatingNational.
    def visitSortCollatingNational(self, ctx:CobolParser.SortCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortInputProcedurePhrase.
    def visitSortInputProcedurePhrase(self, ctx:CobolParser.SortInputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortInputThrough.
    def visitSortInputThrough(self, ctx:CobolParser.SortInputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortUsing.
    def visitSortUsing(self, ctx:CobolParser.SortUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortOutputProcedurePhrase.
    def visitSortOutputProcedurePhrase(self, ctx:CobolParser.SortOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortOutputThrough.
    def visitSortOutputThrough(self, ctx:CobolParser.SortOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortGivingPhrase.
    def visitSortGivingPhrase(self, ctx:CobolParser.SortGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sortGiving.
    def visitSortGiving(self, ctx:CobolParser.SortGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#startStatement.
    def visitStartStatement(self, ctx:CobolParser.StartStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#startKey.
    def visitStartKey(self, ctx:CobolParser.StartKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stopStatement.
    def visitStopStatement(self, ctx:CobolParser.StopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stopStatementGiving.
    def visitStopStatementGiving(self, ctx:CobolParser.StopStatementGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stringStatement.
    def visitStringStatement(self, ctx:CobolParser.StringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stringSendingPhrase.
    def visitStringSendingPhrase(self, ctx:CobolParser.StringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stringSending.
    def visitStringSending(self, ctx:CobolParser.StringSendingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stringDelimitedByPhrase.
    def visitStringDelimitedByPhrase(self, ctx:CobolParser.StringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stringForPhrase.
    def visitStringForPhrase(self, ctx:CobolParser.StringForPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stringIntoPhrase.
    def visitStringIntoPhrase(self, ctx:CobolParser.StringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#stringWithPointerPhrase.
    def visitStringWithPointerPhrase(self, ctx:CobolParser.StringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractStatement.
    def visitSubtractStatement(self, ctx:CobolParser.SubtractStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractFromStatement.
    def visitSubtractFromStatement(self, ctx:CobolParser.SubtractFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractFromGivingStatement.
    def visitSubtractFromGivingStatement(self, ctx:CobolParser.SubtractFromGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractCorrespondingStatement.
    def visitSubtractCorrespondingStatement(self, ctx:CobolParser.SubtractCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractSubtrahend.
    def visitSubtractSubtrahend(self, ctx:CobolParser.SubtractSubtrahendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractMinuend.
    def visitSubtractMinuend(self, ctx:CobolParser.SubtractMinuendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractMinuendGiving.
    def visitSubtractMinuendGiving(self, ctx:CobolParser.SubtractMinuendGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractGiving.
    def visitSubtractGiving(self, ctx:CobolParser.SubtractGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subtractMinuendCorresponding.
    def visitSubtractMinuendCorresponding(self, ctx:CobolParser.SubtractMinuendCorrespondingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#terminateStatement.
    def visitTerminateStatement(self, ctx:CobolParser.TerminateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringStatement.
    def visitUnstringStatement(self, ctx:CobolParser.UnstringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringSendingPhrase.
    def visitUnstringSendingPhrase(self, ctx:CobolParser.UnstringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringDelimitedByPhrase.
    def visitUnstringDelimitedByPhrase(self, ctx:CobolParser.UnstringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringOrAllPhrase.
    def visitUnstringOrAllPhrase(self, ctx:CobolParser.UnstringOrAllPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringIntoPhrase.
    def visitUnstringIntoPhrase(self, ctx:CobolParser.UnstringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringInto.
    def visitUnstringInto(self, ctx:CobolParser.UnstringIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringDelimiterIn.
    def visitUnstringDelimiterIn(self, ctx:CobolParser.UnstringDelimiterInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringCountIn.
    def visitUnstringCountIn(self, ctx:CobolParser.UnstringCountInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringWithPointerPhrase.
    def visitUnstringWithPointerPhrase(self, ctx:CobolParser.UnstringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#unstringTallyingPhrase.
    def visitUnstringTallyingPhrase(self, ctx:CobolParser.UnstringTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#useStatement.
    def visitUseStatement(self, ctx:CobolParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#useAfterClause.
    def visitUseAfterClause(self, ctx:CobolParser.UseAfterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#useAfterOn.
    def visitUseAfterOn(self, ctx:CobolParser.UseAfterOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#useDebugClause.
    def visitUseDebugClause(self, ctx:CobolParser.UseDebugClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#useDebugOn.
    def visitUseDebugOn(self, ctx:CobolParser.UseDebugOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#writeStatement.
    def visitWriteStatement(self, ctx:CobolParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#writeFromPhrase.
    def visitWriteFromPhrase(self, ctx:CobolParser.WriteFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#writeAdvancingPhrase.
    def visitWriteAdvancingPhrase(self, ctx:CobolParser.WriteAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#writeAdvancingPage.
    def visitWriteAdvancingPage(self, ctx:CobolParser.WriteAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#writeAdvancingLines.
    def visitWriteAdvancingLines(self, ctx:CobolParser.WriteAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#writeAdvancingMnemonic.
    def visitWriteAdvancingMnemonic(self, ctx:CobolParser.WriteAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#writeAtEndOfPagePhrase.
    def visitWriteAtEndOfPagePhrase(self, ctx:CobolParser.WriteAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#writeNotAtEndOfPagePhrase.
    def visitWriteNotAtEndOfPagePhrase(self, ctx:CobolParser.WriteNotAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#atEndPhrase.
    def visitAtEndPhrase(self, ctx:CobolParser.AtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#notAtEndPhrase.
    def visitNotAtEndPhrase(self, ctx:CobolParser.NotAtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#invalidKeyPhrase.
    def visitInvalidKeyPhrase(self, ctx:CobolParser.InvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#notInvalidKeyPhrase.
    def visitNotInvalidKeyPhrase(self, ctx:CobolParser.NotInvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#onOverflowPhrase.
    def visitOnOverflowPhrase(self, ctx:CobolParser.OnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#notOnOverflowPhrase.
    def visitNotOnOverflowPhrase(self, ctx:CobolParser.NotOnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#onSizeErrorPhrase.
    def visitOnSizeErrorPhrase(self, ctx:CobolParser.OnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#notOnSizeErrorPhrase.
    def visitNotOnSizeErrorPhrase(self, ctx:CobolParser.NotOnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#onExceptionClause.
    def visitOnExceptionClause(self, ctx:CobolParser.OnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#notOnExceptionClause.
    def visitNotOnExceptionClause(self, ctx:CobolParser.NotOnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:CobolParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#plusMinus.
    def visitPlusMinus(self, ctx:CobolParser.PlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multDivs.
    def visitMultDivs(self, ctx:CobolParser.MultDivsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#multDiv.
    def visitMultDiv(self, ctx:CobolParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#powers.
    def visitPowers(self, ctx:CobolParser.PowersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#power.
    def visitPower(self, ctx:CobolParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#basis.
    def visitBasis(self, ctx:CobolParser.BasisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#condition.
    def visitCondition(self, ctx:CobolParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#andOrCondition.
    def visitAndOrCondition(self, ctx:CobolParser.AndOrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#combinableCondition.
    def visitCombinableCondition(self, ctx:CobolParser.CombinableConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#simpleCondition.
    def visitSimpleCondition(self, ctx:CobolParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#classCondition.
    def visitClassCondition(self, ctx:CobolParser.ClassConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#conditionNameReference.
    def visitConditionNameReference(self, ctx:CobolParser.ConditionNameReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#conditionNameSubscriptReference.
    def visitConditionNameSubscriptReference(self, ctx:CobolParser.ConditionNameSubscriptReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#relationCondition.
    def visitRelationCondition(self, ctx:CobolParser.RelationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#relationSignCondition.
    def visitRelationSignCondition(self, ctx:CobolParser.RelationSignConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#relationArithmeticComparison.
    def visitRelationArithmeticComparison(self, ctx:CobolParser.RelationArithmeticComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#relationCombinedComparison.
    def visitRelationCombinedComparison(self, ctx:CobolParser.RelationCombinedComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#relationCombinedCondition.
    def visitRelationCombinedCondition(self, ctx:CobolParser.RelationCombinedConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#relationalOperator.
    def visitRelationalOperator(self, ctx:CobolParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#abbreviation.
    def visitAbbreviation(self, ctx:CobolParser.AbbreviationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#identifier.
    def visitIdentifier(self, ctx:CobolParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#tableCall.
    def visitTableCall(self, ctx:CobolParser.TableCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#functionCall.
    def visitFunctionCall(self, ctx:CobolParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#referenceModifier.
    def visitReferenceModifier(self, ctx:CobolParser.ReferenceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#characterPosition.
    def visitCharacterPosition(self, ctx:CobolParser.CharacterPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#length.
    def visitLength(self, ctx:CobolParser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#subscript.
    def visitSubscript(self, ctx:CobolParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#argument.
    def visitArgument(self, ctx:CobolParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#qualifiedDataName.
    def visitQualifiedDataName(self, ctx:CobolParser.QualifiedDataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#qualifiedDataNameFormat1.
    def visitQualifiedDataNameFormat1(self, ctx:CobolParser.QualifiedDataNameFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#qualifiedDataNameFormat2.
    def visitQualifiedDataNameFormat2(self, ctx:CobolParser.QualifiedDataNameFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#qualifiedDataNameFormat3.
    def visitQualifiedDataNameFormat3(self, ctx:CobolParser.QualifiedDataNameFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#qualifiedDataNameFormat4.
    def visitQualifiedDataNameFormat4(self, ctx:CobolParser.QualifiedDataNameFormat4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#qualifiedInData.
    def visitQualifiedInData(self, ctx:CobolParser.QualifiedInDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inData.
    def visitInData(self, ctx:CobolParser.InDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inFile.
    def visitInFile(self, ctx:CobolParser.InFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inMnemonic.
    def visitInMnemonic(self, ctx:CobolParser.InMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inSection.
    def visitInSection(self, ctx:CobolParser.InSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inLibrary.
    def visitInLibrary(self, ctx:CobolParser.InLibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#inTable.
    def visitInTable(self, ctx:CobolParser.InTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#alphabetName.
    def visitAlphabetName(self, ctx:CobolParser.AlphabetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#assignmentName.
    def visitAssignmentName(self, ctx:CobolParser.AssignmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#basisName.
    def visitBasisName(self, ctx:CobolParser.BasisNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#cdName.
    def visitCdName(self, ctx:CobolParser.CdNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#className.
    def visitClassName(self, ctx:CobolParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#computerName.
    def visitComputerName(self, ctx:CobolParser.ComputerNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#conditionName.
    def visitConditionName(self, ctx:CobolParser.ConditionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataName.
    def visitDataName(self, ctx:CobolParser.DataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#dataDescName.
    def visitDataDescName(self, ctx:CobolParser.DataDescNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#environmentName.
    def visitEnvironmentName(self, ctx:CobolParser.EnvironmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#fileName.
    def visitFileName(self, ctx:CobolParser.FileNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#functionName.
    def visitFunctionName(self, ctx:CobolParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#indexName.
    def visitIndexName(self, ctx:CobolParser.IndexNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#languageName.
    def visitLanguageName(self, ctx:CobolParser.LanguageNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#libraryName.
    def visitLibraryName(self, ctx:CobolParser.LibraryNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#localName.
    def visitLocalName(self, ctx:CobolParser.LocalNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#mnemonicName.
    def visitMnemonicName(self, ctx:CobolParser.MnemonicNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#paragraphName.
    def visitParagraphName(self, ctx:CobolParser.ParagraphNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#procedureName.
    def visitProcedureName(self, ctx:CobolParser.ProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#programName.
    def visitProgramName(self, ctx:CobolParser.ProgramNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#recordName.
    def visitRecordName(self, ctx:CobolParser.RecordNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#reportName.
    def visitReportName(self, ctx:CobolParser.ReportNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#routineName.
    def visitRoutineName(self, ctx:CobolParser.RoutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#screenName.
    def visitScreenName(self, ctx:CobolParser.ScreenNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#sectionName.
    def visitSectionName(self, ctx:CobolParser.SectionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#systemName.
    def visitSystemName(self, ctx:CobolParser.SystemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#symbolicCharacter.
    def visitSymbolicCharacter(self, ctx:CobolParser.SymbolicCharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#textName.
    def visitTextName(self, ctx:CobolParser.TextNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#cobolWord.
    def visitCobolWord(self, ctx:CobolParser.CobolWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#literal.
    def visitLiteral(self, ctx:CobolParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:CobolParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#numericLiteral.
    def visitNumericLiteral(self, ctx:CobolParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:CobolParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#cicsDfhRespLiteral.
    def visitCicsDfhRespLiteral(self, ctx:CobolParser.CicsDfhRespLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#cicsDfhValueLiteral.
    def visitCicsDfhValueLiteral(self, ctx:CobolParser.CicsDfhValueLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#figurativeConstant.
    def visitFigurativeConstant(self, ctx:CobolParser.FigurativeConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#specialRegister.
    def visitSpecialRegister(self, ctx:CobolParser.SpecialRegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolParser#commentEntry.
    def visitCommentEntry(self, ctx:CobolParser.CommentEntryContext):
        return self.visitChildren(ctx)



del CobolParser