# Generated from parser/Cobol/Cobol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CobolParser import CobolParser
else:
    from CobolParser import CobolParser

# This class defines a complete listener for a parse tree produced by CobolParser.
class CobolListener(ParseTreeListener):

    # Enter a parse tree produced by CobolParser#startRule.
    def enterStartRule(self, ctx:CobolParser.StartRuleContext):
        pass

    # Exit a parse tree produced by CobolParser#startRule.
    def exitStartRule(self, ctx:CobolParser.StartRuleContext):
        pass


    # Enter a parse tree produced by CobolParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CobolParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CobolParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CobolParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CobolParser#programUnit.
    def enterProgramUnit(self, ctx:CobolParser.ProgramUnitContext):
        pass

    # Exit a parse tree produced by CobolParser#programUnit.
    def exitProgramUnit(self, ctx:CobolParser.ProgramUnitContext):
        pass


    # Enter a parse tree produced by CobolParser#endProgramStatement.
    def enterEndProgramStatement(self, ctx:CobolParser.EndProgramStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#endProgramStatement.
    def exitEndProgramStatement(self, ctx:CobolParser.EndProgramStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#identificationDivision.
    def enterIdentificationDivision(self, ctx:CobolParser.IdentificationDivisionContext):
        pass

    # Exit a parse tree produced by CobolParser#identificationDivision.
    def exitIdentificationDivision(self, ctx:CobolParser.IdentificationDivisionContext):
        pass


    # Enter a parse tree produced by CobolParser#identificationDivisionBody.
    def enterIdentificationDivisionBody(self, ctx:CobolParser.IdentificationDivisionBodyContext):
        pass

    # Exit a parse tree produced by CobolParser#identificationDivisionBody.
    def exitIdentificationDivisionBody(self, ctx:CobolParser.IdentificationDivisionBodyContext):
        pass


    # Enter a parse tree produced by CobolParser#programIdParagraph.
    def enterProgramIdParagraph(self, ctx:CobolParser.ProgramIdParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#programIdParagraph.
    def exitProgramIdParagraph(self, ctx:CobolParser.ProgramIdParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#authorParagraph.
    def enterAuthorParagraph(self, ctx:CobolParser.AuthorParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#authorParagraph.
    def exitAuthorParagraph(self, ctx:CobolParser.AuthorParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#installationParagraph.
    def enterInstallationParagraph(self, ctx:CobolParser.InstallationParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#installationParagraph.
    def exitInstallationParagraph(self, ctx:CobolParser.InstallationParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#dateWrittenParagraph.
    def enterDateWrittenParagraph(self, ctx:CobolParser.DateWrittenParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#dateWrittenParagraph.
    def exitDateWrittenParagraph(self, ctx:CobolParser.DateWrittenParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#dateCompiledParagraph.
    def enterDateCompiledParagraph(self, ctx:CobolParser.DateCompiledParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#dateCompiledParagraph.
    def exitDateCompiledParagraph(self, ctx:CobolParser.DateCompiledParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#securityParagraph.
    def enterSecurityParagraph(self, ctx:CobolParser.SecurityParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#securityParagraph.
    def exitSecurityParagraph(self, ctx:CobolParser.SecurityParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#remarksParagraph.
    def enterRemarksParagraph(self, ctx:CobolParser.RemarksParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#remarksParagraph.
    def exitRemarksParagraph(self, ctx:CobolParser.RemarksParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#environmentDivision.
    def enterEnvironmentDivision(self, ctx:CobolParser.EnvironmentDivisionContext):
        pass

    # Exit a parse tree produced by CobolParser#environmentDivision.
    def exitEnvironmentDivision(self, ctx:CobolParser.EnvironmentDivisionContext):
        pass


    # Enter a parse tree produced by CobolParser#environmentDivisionBody.
    def enterEnvironmentDivisionBody(self, ctx:CobolParser.EnvironmentDivisionBodyContext):
        pass

    # Exit a parse tree produced by CobolParser#environmentDivisionBody.
    def exitEnvironmentDivisionBody(self, ctx:CobolParser.EnvironmentDivisionBodyContext):
        pass


    # Enter a parse tree produced by CobolParser#configurationSection.
    def enterConfigurationSection(self, ctx:CobolParser.ConfigurationSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#configurationSection.
    def exitConfigurationSection(self, ctx:CobolParser.ConfigurationSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#configurationSectionParagraph.
    def enterConfigurationSectionParagraph(self, ctx:CobolParser.ConfigurationSectionParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#configurationSectionParagraph.
    def exitConfigurationSectionParagraph(self, ctx:CobolParser.ConfigurationSectionParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#sourceComputerParagraph.
    def enterSourceComputerParagraph(self, ctx:CobolParser.SourceComputerParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#sourceComputerParagraph.
    def exitSourceComputerParagraph(self, ctx:CobolParser.SourceComputerParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#objectComputerParagraph.
    def enterObjectComputerParagraph(self, ctx:CobolParser.ObjectComputerParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#objectComputerParagraph.
    def exitObjectComputerParagraph(self, ctx:CobolParser.ObjectComputerParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#objectComputerClause.
    def enterObjectComputerClause(self, ctx:CobolParser.ObjectComputerClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#objectComputerClause.
    def exitObjectComputerClause(self, ctx:CobolParser.ObjectComputerClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#memorySizeClause.
    def enterMemorySizeClause(self, ctx:CobolParser.MemorySizeClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#memorySizeClause.
    def exitMemorySizeClause(self, ctx:CobolParser.MemorySizeClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#diskSizeClause.
    def enterDiskSizeClause(self, ctx:CobolParser.DiskSizeClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#diskSizeClause.
    def exitDiskSizeClause(self, ctx:CobolParser.DiskSizeClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#collatingSequenceClause.
    def enterCollatingSequenceClause(self, ctx:CobolParser.CollatingSequenceClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#collatingSequenceClause.
    def exitCollatingSequenceClause(self, ctx:CobolParser.CollatingSequenceClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#collatingSequenceClauseAlphanumeric.
    def enterCollatingSequenceClauseAlphanumeric(self, ctx:CobolParser.CollatingSequenceClauseAlphanumericContext):
        pass

    # Exit a parse tree produced by CobolParser#collatingSequenceClauseAlphanumeric.
    def exitCollatingSequenceClauseAlphanumeric(self, ctx:CobolParser.CollatingSequenceClauseAlphanumericContext):
        pass


    # Enter a parse tree produced by CobolParser#collatingSequenceClauseNational.
    def enterCollatingSequenceClauseNational(self, ctx:CobolParser.CollatingSequenceClauseNationalContext):
        pass

    # Exit a parse tree produced by CobolParser#collatingSequenceClauseNational.
    def exitCollatingSequenceClauseNational(self, ctx:CobolParser.CollatingSequenceClauseNationalContext):
        pass


    # Enter a parse tree produced by CobolParser#segmentLimitClause.
    def enterSegmentLimitClause(self, ctx:CobolParser.SegmentLimitClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#segmentLimitClause.
    def exitSegmentLimitClause(self, ctx:CobolParser.SegmentLimitClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#characterSetClause.
    def enterCharacterSetClause(self, ctx:CobolParser.CharacterSetClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#characterSetClause.
    def exitCharacterSetClause(self, ctx:CobolParser.CharacterSetClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#specialNamesParagraph.
    def enterSpecialNamesParagraph(self, ctx:CobolParser.SpecialNamesParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#specialNamesParagraph.
    def exitSpecialNamesParagraph(self, ctx:CobolParser.SpecialNamesParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#specialNameClause.
    def enterSpecialNameClause(self, ctx:CobolParser.SpecialNameClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#specialNameClause.
    def exitSpecialNameClause(self, ctx:CobolParser.SpecialNameClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#alphabetClause.
    def enterAlphabetClause(self, ctx:CobolParser.AlphabetClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#alphabetClause.
    def exitAlphabetClause(self, ctx:CobolParser.AlphabetClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#alphabetClauseFormat1.
    def enterAlphabetClauseFormat1(self, ctx:CobolParser.AlphabetClauseFormat1Context):
        pass

    # Exit a parse tree produced by CobolParser#alphabetClauseFormat1.
    def exitAlphabetClauseFormat1(self, ctx:CobolParser.AlphabetClauseFormat1Context):
        pass


    # Enter a parse tree produced by CobolParser#alphabetLiterals.
    def enterAlphabetLiterals(self, ctx:CobolParser.AlphabetLiteralsContext):
        pass

    # Exit a parse tree produced by CobolParser#alphabetLiterals.
    def exitAlphabetLiterals(self, ctx:CobolParser.AlphabetLiteralsContext):
        pass


    # Enter a parse tree produced by CobolParser#alphabetThrough.
    def enterAlphabetThrough(self, ctx:CobolParser.AlphabetThroughContext):
        pass

    # Exit a parse tree produced by CobolParser#alphabetThrough.
    def exitAlphabetThrough(self, ctx:CobolParser.AlphabetThroughContext):
        pass


    # Enter a parse tree produced by CobolParser#alphabetAlso.
    def enterAlphabetAlso(self, ctx:CobolParser.AlphabetAlsoContext):
        pass

    # Exit a parse tree produced by CobolParser#alphabetAlso.
    def exitAlphabetAlso(self, ctx:CobolParser.AlphabetAlsoContext):
        pass


    # Enter a parse tree produced by CobolParser#alphabetClauseFormat2.
    def enterAlphabetClauseFormat2(self, ctx:CobolParser.AlphabetClauseFormat2Context):
        pass

    # Exit a parse tree produced by CobolParser#alphabetClauseFormat2.
    def exitAlphabetClauseFormat2(self, ctx:CobolParser.AlphabetClauseFormat2Context):
        pass


    # Enter a parse tree produced by CobolParser#channelClause.
    def enterChannelClause(self, ctx:CobolParser.ChannelClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#channelClause.
    def exitChannelClause(self, ctx:CobolParser.ChannelClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#classClause.
    def enterClassClause(self, ctx:CobolParser.ClassClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#classClause.
    def exitClassClause(self, ctx:CobolParser.ClassClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#classClauseThrough.
    def enterClassClauseThrough(self, ctx:CobolParser.ClassClauseThroughContext):
        pass

    # Exit a parse tree produced by CobolParser#classClauseThrough.
    def exitClassClauseThrough(self, ctx:CobolParser.ClassClauseThroughContext):
        pass


    # Enter a parse tree produced by CobolParser#classClauseFrom.
    def enterClassClauseFrom(self, ctx:CobolParser.ClassClauseFromContext):
        pass

    # Exit a parse tree produced by CobolParser#classClauseFrom.
    def exitClassClauseFrom(self, ctx:CobolParser.ClassClauseFromContext):
        pass


    # Enter a parse tree produced by CobolParser#classClauseTo.
    def enterClassClauseTo(self, ctx:CobolParser.ClassClauseToContext):
        pass

    # Exit a parse tree produced by CobolParser#classClauseTo.
    def exitClassClauseTo(self, ctx:CobolParser.ClassClauseToContext):
        pass


    # Enter a parse tree produced by CobolParser#currencySignClause.
    def enterCurrencySignClause(self, ctx:CobolParser.CurrencySignClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#currencySignClause.
    def exitCurrencySignClause(self, ctx:CobolParser.CurrencySignClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#decimalPointClause.
    def enterDecimalPointClause(self, ctx:CobolParser.DecimalPointClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#decimalPointClause.
    def exitDecimalPointClause(self, ctx:CobolParser.DecimalPointClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#defaultComputationalSignClause.
    def enterDefaultComputationalSignClause(self, ctx:CobolParser.DefaultComputationalSignClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#defaultComputationalSignClause.
    def exitDefaultComputationalSignClause(self, ctx:CobolParser.DefaultComputationalSignClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#defaultDisplaySignClause.
    def enterDefaultDisplaySignClause(self, ctx:CobolParser.DefaultDisplaySignClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#defaultDisplaySignClause.
    def exitDefaultDisplaySignClause(self, ctx:CobolParser.DefaultDisplaySignClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#environmentSwitchNameClause.
    def enterEnvironmentSwitchNameClause(self, ctx:CobolParser.EnvironmentSwitchNameClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#environmentSwitchNameClause.
    def exitEnvironmentSwitchNameClause(self, ctx:CobolParser.EnvironmentSwitchNameClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def enterEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CobolParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def exitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CobolParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#odtClause.
    def enterOdtClause(self, ctx:CobolParser.OdtClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#odtClause.
    def exitOdtClause(self, ctx:CobolParser.OdtClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reserveNetworkClause.
    def enterReserveNetworkClause(self, ctx:CobolParser.ReserveNetworkClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reserveNetworkClause.
    def exitReserveNetworkClause(self, ctx:CobolParser.ReserveNetworkClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#symbolicCharactersClause.
    def enterSymbolicCharactersClause(self, ctx:CobolParser.SymbolicCharactersClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#symbolicCharactersClause.
    def exitSymbolicCharactersClause(self, ctx:CobolParser.SymbolicCharactersClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#symbolicCharacters.
    def enterSymbolicCharacters(self, ctx:CobolParser.SymbolicCharactersContext):
        pass

    # Exit a parse tree produced by CobolParser#symbolicCharacters.
    def exitSymbolicCharacters(self, ctx:CobolParser.SymbolicCharactersContext):
        pass


    # Enter a parse tree produced by CobolParser#inputOutputSection.
    def enterInputOutputSection(self, ctx:CobolParser.InputOutputSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#inputOutputSection.
    def exitInputOutputSection(self, ctx:CobolParser.InputOutputSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#inputOutputSectionParagraph.
    def enterInputOutputSectionParagraph(self, ctx:CobolParser.InputOutputSectionParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#inputOutputSectionParagraph.
    def exitInputOutputSectionParagraph(self, ctx:CobolParser.InputOutputSectionParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#fileControlParagraph.
    def enterFileControlParagraph(self, ctx:CobolParser.FileControlParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#fileControlParagraph.
    def exitFileControlParagraph(self, ctx:CobolParser.FileControlParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#fileControlEntry.
    def enterFileControlEntry(self, ctx:CobolParser.FileControlEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#fileControlEntry.
    def exitFileControlEntry(self, ctx:CobolParser.FileControlEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#selectClause.
    def enterSelectClause(self, ctx:CobolParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#selectClause.
    def exitSelectClause(self, ctx:CobolParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#fileControlClause.
    def enterFileControlClause(self, ctx:CobolParser.FileControlClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#fileControlClause.
    def exitFileControlClause(self, ctx:CobolParser.FileControlClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#assignClause.
    def enterAssignClause(self, ctx:CobolParser.AssignClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#assignClause.
    def exitAssignClause(self, ctx:CobolParser.AssignClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reserveClause.
    def enterReserveClause(self, ctx:CobolParser.ReserveClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reserveClause.
    def exitReserveClause(self, ctx:CobolParser.ReserveClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#organizationClause.
    def enterOrganizationClause(self, ctx:CobolParser.OrganizationClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#organizationClause.
    def exitOrganizationClause(self, ctx:CobolParser.OrganizationClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#paddingCharacterClause.
    def enterPaddingCharacterClause(self, ctx:CobolParser.PaddingCharacterClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#paddingCharacterClause.
    def exitPaddingCharacterClause(self, ctx:CobolParser.PaddingCharacterClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#recordDelimiterClause.
    def enterRecordDelimiterClause(self, ctx:CobolParser.RecordDelimiterClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#recordDelimiterClause.
    def exitRecordDelimiterClause(self, ctx:CobolParser.RecordDelimiterClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#accessModeClause.
    def enterAccessModeClause(self, ctx:CobolParser.AccessModeClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#accessModeClause.
    def exitAccessModeClause(self, ctx:CobolParser.AccessModeClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#recordKeyClause.
    def enterRecordKeyClause(self, ctx:CobolParser.RecordKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#recordKeyClause.
    def exitRecordKeyClause(self, ctx:CobolParser.RecordKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#alternateRecordKeyClause.
    def enterAlternateRecordKeyClause(self, ctx:CobolParser.AlternateRecordKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#alternateRecordKeyClause.
    def exitAlternateRecordKeyClause(self, ctx:CobolParser.AlternateRecordKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#passwordClause.
    def enterPasswordClause(self, ctx:CobolParser.PasswordClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#passwordClause.
    def exitPasswordClause(self, ctx:CobolParser.PasswordClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#fileStatusClause.
    def enterFileStatusClause(self, ctx:CobolParser.FileStatusClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#fileStatusClause.
    def exitFileStatusClause(self, ctx:CobolParser.FileStatusClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#relativeKeyClause.
    def enterRelativeKeyClause(self, ctx:CobolParser.RelativeKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#relativeKeyClause.
    def exitRelativeKeyClause(self, ctx:CobolParser.RelativeKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#ioControlParagraph.
    def enterIoControlParagraph(self, ctx:CobolParser.IoControlParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#ioControlParagraph.
    def exitIoControlParagraph(self, ctx:CobolParser.IoControlParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#ioControlClause.
    def enterIoControlClause(self, ctx:CobolParser.IoControlClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#ioControlClause.
    def exitIoControlClause(self, ctx:CobolParser.IoControlClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#rerunClause.
    def enterRerunClause(self, ctx:CobolParser.RerunClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#rerunClause.
    def exitRerunClause(self, ctx:CobolParser.RerunClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#rerunEveryRecords.
    def enterRerunEveryRecords(self, ctx:CobolParser.RerunEveryRecordsContext):
        pass

    # Exit a parse tree produced by CobolParser#rerunEveryRecords.
    def exitRerunEveryRecords(self, ctx:CobolParser.RerunEveryRecordsContext):
        pass


    # Enter a parse tree produced by CobolParser#rerunEveryOf.
    def enterRerunEveryOf(self, ctx:CobolParser.RerunEveryOfContext):
        pass

    # Exit a parse tree produced by CobolParser#rerunEveryOf.
    def exitRerunEveryOf(self, ctx:CobolParser.RerunEveryOfContext):
        pass


    # Enter a parse tree produced by CobolParser#rerunEveryClock.
    def enterRerunEveryClock(self, ctx:CobolParser.RerunEveryClockContext):
        pass

    # Exit a parse tree produced by CobolParser#rerunEveryClock.
    def exitRerunEveryClock(self, ctx:CobolParser.RerunEveryClockContext):
        pass


    # Enter a parse tree produced by CobolParser#sameClause.
    def enterSameClause(self, ctx:CobolParser.SameClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#sameClause.
    def exitSameClause(self, ctx:CobolParser.SameClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#multipleFileClause.
    def enterMultipleFileClause(self, ctx:CobolParser.MultipleFileClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#multipleFileClause.
    def exitMultipleFileClause(self, ctx:CobolParser.MultipleFileClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#multipleFilePosition.
    def enterMultipleFilePosition(self, ctx:CobolParser.MultipleFilePositionContext):
        pass

    # Exit a parse tree produced by CobolParser#multipleFilePosition.
    def exitMultipleFilePosition(self, ctx:CobolParser.MultipleFilePositionContext):
        pass


    # Enter a parse tree produced by CobolParser#commitmentControlClause.
    def enterCommitmentControlClause(self, ctx:CobolParser.CommitmentControlClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#commitmentControlClause.
    def exitCommitmentControlClause(self, ctx:CobolParser.CommitmentControlClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataDivision.
    def enterDataDivision(self, ctx:CobolParser.DataDivisionContext):
        pass

    # Exit a parse tree produced by CobolParser#dataDivision.
    def exitDataDivision(self, ctx:CobolParser.DataDivisionContext):
        pass


    # Enter a parse tree produced by CobolParser#dataDivisionSection.
    def enterDataDivisionSection(self, ctx:CobolParser.DataDivisionSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#dataDivisionSection.
    def exitDataDivisionSection(self, ctx:CobolParser.DataDivisionSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#fileSection.
    def enterFileSection(self, ctx:CobolParser.FileSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#fileSection.
    def exitFileSection(self, ctx:CobolParser.FileSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#fileDescriptionEntry.
    def enterFileDescriptionEntry(self, ctx:CobolParser.FileDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#fileDescriptionEntry.
    def exitFileDescriptionEntry(self, ctx:CobolParser.FileDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#fileDescriptionEntryClause.
    def enterFileDescriptionEntryClause(self, ctx:CobolParser.FileDescriptionEntryClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#fileDescriptionEntryClause.
    def exitFileDescriptionEntryClause(self, ctx:CobolParser.FileDescriptionEntryClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#externalClause.
    def enterExternalClause(self, ctx:CobolParser.ExternalClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#externalClause.
    def exitExternalClause(self, ctx:CobolParser.ExternalClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#globalClause.
    def enterGlobalClause(self, ctx:CobolParser.GlobalClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#globalClause.
    def exitGlobalClause(self, ctx:CobolParser.GlobalClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#blockContainsClause.
    def enterBlockContainsClause(self, ctx:CobolParser.BlockContainsClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#blockContainsClause.
    def exitBlockContainsClause(self, ctx:CobolParser.BlockContainsClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#blockContainsTo.
    def enterBlockContainsTo(self, ctx:CobolParser.BlockContainsToContext):
        pass

    # Exit a parse tree produced by CobolParser#blockContainsTo.
    def exitBlockContainsTo(self, ctx:CobolParser.BlockContainsToContext):
        pass


    # Enter a parse tree produced by CobolParser#recordContainsClause.
    def enterRecordContainsClause(self, ctx:CobolParser.RecordContainsClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#recordContainsClause.
    def exitRecordContainsClause(self, ctx:CobolParser.RecordContainsClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#recordContainsClauseFormat1.
    def enterRecordContainsClauseFormat1(self, ctx:CobolParser.RecordContainsClauseFormat1Context):
        pass

    # Exit a parse tree produced by CobolParser#recordContainsClauseFormat1.
    def exitRecordContainsClauseFormat1(self, ctx:CobolParser.RecordContainsClauseFormat1Context):
        pass


    # Enter a parse tree produced by CobolParser#recordContainsClauseFormat2.
    def enterRecordContainsClauseFormat2(self, ctx:CobolParser.RecordContainsClauseFormat2Context):
        pass

    # Exit a parse tree produced by CobolParser#recordContainsClauseFormat2.
    def exitRecordContainsClauseFormat2(self, ctx:CobolParser.RecordContainsClauseFormat2Context):
        pass


    # Enter a parse tree produced by CobolParser#recordContainsClauseFormat3.
    def enterRecordContainsClauseFormat3(self, ctx:CobolParser.RecordContainsClauseFormat3Context):
        pass

    # Exit a parse tree produced by CobolParser#recordContainsClauseFormat3.
    def exitRecordContainsClauseFormat3(self, ctx:CobolParser.RecordContainsClauseFormat3Context):
        pass


    # Enter a parse tree produced by CobolParser#recordContainsTo.
    def enterRecordContainsTo(self, ctx:CobolParser.RecordContainsToContext):
        pass

    # Exit a parse tree produced by CobolParser#recordContainsTo.
    def exitRecordContainsTo(self, ctx:CobolParser.RecordContainsToContext):
        pass


    # Enter a parse tree produced by CobolParser#labelRecordsClause.
    def enterLabelRecordsClause(self, ctx:CobolParser.LabelRecordsClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#labelRecordsClause.
    def exitLabelRecordsClause(self, ctx:CobolParser.LabelRecordsClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#valueOfClause.
    def enterValueOfClause(self, ctx:CobolParser.ValueOfClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#valueOfClause.
    def exitValueOfClause(self, ctx:CobolParser.ValueOfClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#valuePair.
    def enterValuePair(self, ctx:CobolParser.ValuePairContext):
        pass

    # Exit a parse tree produced by CobolParser#valuePair.
    def exitValuePair(self, ctx:CobolParser.ValuePairContext):
        pass


    # Enter a parse tree produced by CobolParser#dataRecordsClause.
    def enterDataRecordsClause(self, ctx:CobolParser.DataRecordsClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataRecordsClause.
    def exitDataRecordsClause(self, ctx:CobolParser.DataRecordsClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#linageClause.
    def enterLinageClause(self, ctx:CobolParser.LinageClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#linageClause.
    def exitLinageClause(self, ctx:CobolParser.LinageClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#linageAt.
    def enterLinageAt(self, ctx:CobolParser.LinageAtContext):
        pass

    # Exit a parse tree produced by CobolParser#linageAt.
    def exitLinageAt(self, ctx:CobolParser.LinageAtContext):
        pass


    # Enter a parse tree produced by CobolParser#linageFootingAt.
    def enterLinageFootingAt(self, ctx:CobolParser.LinageFootingAtContext):
        pass

    # Exit a parse tree produced by CobolParser#linageFootingAt.
    def exitLinageFootingAt(self, ctx:CobolParser.LinageFootingAtContext):
        pass


    # Enter a parse tree produced by CobolParser#linageLinesAtTop.
    def enterLinageLinesAtTop(self, ctx:CobolParser.LinageLinesAtTopContext):
        pass

    # Exit a parse tree produced by CobolParser#linageLinesAtTop.
    def exitLinageLinesAtTop(self, ctx:CobolParser.LinageLinesAtTopContext):
        pass


    # Enter a parse tree produced by CobolParser#linageLinesAtBottom.
    def enterLinageLinesAtBottom(self, ctx:CobolParser.LinageLinesAtBottomContext):
        pass

    # Exit a parse tree produced by CobolParser#linageLinesAtBottom.
    def exitLinageLinesAtBottom(self, ctx:CobolParser.LinageLinesAtBottomContext):
        pass


    # Enter a parse tree produced by CobolParser#recordingModeClause.
    def enterRecordingModeClause(self, ctx:CobolParser.RecordingModeClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#recordingModeClause.
    def exitRecordingModeClause(self, ctx:CobolParser.RecordingModeClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#modeStatement.
    def enterModeStatement(self, ctx:CobolParser.ModeStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#modeStatement.
    def exitModeStatement(self, ctx:CobolParser.ModeStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#codeSetClause.
    def enterCodeSetClause(self, ctx:CobolParser.CodeSetClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#codeSetClause.
    def exitCodeSetClause(self, ctx:CobolParser.CodeSetClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportClause.
    def enterReportClause(self, ctx:CobolParser.ReportClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportClause.
    def exitReportClause(self, ctx:CobolParser.ReportClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataBaseSection.
    def enterDataBaseSection(self, ctx:CobolParser.DataBaseSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#dataBaseSection.
    def exitDataBaseSection(self, ctx:CobolParser.DataBaseSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#dataBaseSectionEntry.
    def enterDataBaseSectionEntry(self, ctx:CobolParser.DataBaseSectionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#dataBaseSectionEntry.
    def exitDataBaseSectionEntry(self, ctx:CobolParser.DataBaseSectionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#workingStorageSection.
    def enterWorkingStorageSection(self, ctx:CobolParser.WorkingStorageSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#workingStorageSection.
    def exitWorkingStorageSection(self, ctx:CobolParser.WorkingStorageSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#linkageSection.
    def enterLinkageSection(self, ctx:CobolParser.LinkageSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#linkageSection.
    def exitLinkageSection(self, ctx:CobolParser.LinkageSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#communicationSection.
    def enterCommunicationSection(self, ctx:CobolParser.CommunicationSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#communicationSection.
    def exitCommunicationSection(self, ctx:CobolParser.CommunicationSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#communicationDescriptionEntry.
    def enterCommunicationDescriptionEntry(self, ctx:CobolParser.CommunicationDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#communicationDescriptionEntry.
    def exitCommunicationDescriptionEntry(self, ctx:CobolParser.CommunicationDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#communicationDescriptionEntryFormat1.
    def enterCommunicationDescriptionEntryFormat1(self, ctx:CobolParser.CommunicationDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CobolParser#communicationDescriptionEntryFormat1.
    def exitCommunicationDescriptionEntryFormat1(self, ctx:CobolParser.CommunicationDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CobolParser#communicationDescriptionEntryFormat2.
    def enterCommunicationDescriptionEntryFormat2(self, ctx:CobolParser.CommunicationDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CobolParser#communicationDescriptionEntryFormat2.
    def exitCommunicationDescriptionEntryFormat2(self, ctx:CobolParser.CommunicationDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CobolParser#communicationDescriptionEntryFormat3.
    def enterCommunicationDescriptionEntryFormat3(self, ctx:CobolParser.CommunicationDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by CobolParser#communicationDescriptionEntryFormat3.
    def exitCommunicationDescriptionEntryFormat3(self, ctx:CobolParser.CommunicationDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by CobolParser#destinationCountClause.
    def enterDestinationCountClause(self, ctx:CobolParser.DestinationCountClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#destinationCountClause.
    def exitDestinationCountClause(self, ctx:CobolParser.DestinationCountClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#destinationTableClause.
    def enterDestinationTableClause(self, ctx:CobolParser.DestinationTableClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#destinationTableClause.
    def exitDestinationTableClause(self, ctx:CobolParser.DestinationTableClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#endKeyClause.
    def enterEndKeyClause(self, ctx:CobolParser.EndKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#endKeyClause.
    def exitEndKeyClause(self, ctx:CobolParser.EndKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#errorKeyClause.
    def enterErrorKeyClause(self, ctx:CobolParser.ErrorKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#errorKeyClause.
    def exitErrorKeyClause(self, ctx:CobolParser.ErrorKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#messageCountClause.
    def enterMessageCountClause(self, ctx:CobolParser.MessageCountClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#messageCountClause.
    def exitMessageCountClause(self, ctx:CobolParser.MessageCountClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#messageDateClause.
    def enterMessageDateClause(self, ctx:CobolParser.MessageDateClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#messageDateClause.
    def exitMessageDateClause(self, ctx:CobolParser.MessageDateClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#messageTimeClause.
    def enterMessageTimeClause(self, ctx:CobolParser.MessageTimeClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#messageTimeClause.
    def exitMessageTimeClause(self, ctx:CobolParser.MessageTimeClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#statusKeyClause.
    def enterStatusKeyClause(self, ctx:CobolParser.StatusKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#statusKeyClause.
    def exitStatusKeyClause(self, ctx:CobolParser.StatusKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#symbolicDestinationClause.
    def enterSymbolicDestinationClause(self, ctx:CobolParser.SymbolicDestinationClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#symbolicDestinationClause.
    def exitSymbolicDestinationClause(self, ctx:CobolParser.SymbolicDestinationClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#symbolicQueueClause.
    def enterSymbolicQueueClause(self, ctx:CobolParser.SymbolicQueueClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#symbolicQueueClause.
    def exitSymbolicQueueClause(self, ctx:CobolParser.SymbolicQueueClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#symbolicSourceClause.
    def enterSymbolicSourceClause(self, ctx:CobolParser.SymbolicSourceClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#symbolicSourceClause.
    def exitSymbolicSourceClause(self, ctx:CobolParser.SymbolicSourceClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#symbolicTerminalClause.
    def enterSymbolicTerminalClause(self, ctx:CobolParser.SymbolicTerminalClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#symbolicTerminalClause.
    def exitSymbolicTerminalClause(self, ctx:CobolParser.SymbolicTerminalClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#symbolicSubQueueClause.
    def enterSymbolicSubQueueClause(self, ctx:CobolParser.SymbolicSubQueueClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#symbolicSubQueueClause.
    def exitSymbolicSubQueueClause(self, ctx:CobolParser.SymbolicSubQueueClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#textLengthClause.
    def enterTextLengthClause(self, ctx:CobolParser.TextLengthClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#textLengthClause.
    def exitTextLengthClause(self, ctx:CobolParser.TextLengthClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#localStorageSection.
    def enterLocalStorageSection(self, ctx:CobolParser.LocalStorageSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#localStorageSection.
    def exitLocalStorageSection(self, ctx:CobolParser.LocalStorageSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#screenSection.
    def enterScreenSection(self, ctx:CobolParser.ScreenSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#screenSection.
    def exitScreenSection(self, ctx:CobolParser.ScreenSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionEntry.
    def enterScreenDescriptionEntry(self, ctx:CobolParser.ScreenDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionEntry.
    def exitScreenDescriptionEntry(self, ctx:CobolParser.ScreenDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionBlankClause.
    def enterScreenDescriptionBlankClause(self, ctx:CobolParser.ScreenDescriptionBlankClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionBlankClause.
    def exitScreenDescriptionBlankClause(self, ctx:CobolParser.ScreenDescriptionBlankClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionBellClause.
    def enterScreenDescriptionBellClause(self, ctx:CobolParser.ScreenDescriptionBellClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionBellClause.
    def exitScreenDescriptionBellClause(self, ctx:CobolParser.ScreenDescriptionBellClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionBlinkClause.
    def enterScreenDescriptionBlinkClause(self, ctx:CobolParser.ScreenDescriptionBlinkClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionBlinkClause.
    def exitScreenDescriptionBlinkClause(self, ctx:CobolParser.ScreenDescriptionBlinkClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionEraseClause.
    def enterScreenDescriptionEraseClause(self, ctx:CobolParser.ScreenDescriptionEraseClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionEraseClause.
    def exitScreenDescriptionEraseClause(self, ctx:CobolParser.ScreenDescriptionEraseClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionLightClause.
    def enterScreenDescriptionLightClause(self, ctx:CobolParser.ScreenDescriptionLightClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionLightClause.
    def exitScreenDescriptionLightClause(self, ctx:CobolParser.ScreenDescriptionLightClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionGridClause.
    def enterScreenDescriptionGridClause(self, ctx:CobolParser.ScreenDescriptionGridClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionGridClause.
    def exitScreenDescriptionGridClause(self, ctx:CobolParser.ScreenDescriptionGridClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionReverseVideoClause.
    def enterScreenDescriptionReverseVideoClause(self, ctx:CobolParser.ScreenDescriptionReverseVideoClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionReverseVideoClause.
    def exitScreenDescriptionReverseVideoClause(self, ctx:CobolParser.ScreenDescriptionReverseVideoClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionUnderlineClause.
    def enterScreenDescriptionUnderlineClause(self, ctx:CobolParser.ScreenDescriptionUnderlineClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionUnderlineClause.
    def exitScreenDescriptionUnderlineClause(self, ctx:CobolParser.ScreenDescriptionUnderlineClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionSizeClause.
    def enterScreenDescriptionSizeClause(self, ctx:CobolParser.ScreenDescriptionSizeClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionSizeClause.
    def exitScreenDescriptionSizeClause(self, ctx:CobolParser.ScreenDescriptionSizeClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionLineClause.
    def enterScreenDescriptionLineClause(self, ctx:CobolParser.ScreenDescriptionLineClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionLineClause.
    def exitScreenDescriptionLineClause(self, ctx:CobolParser.ScreenDescriptionLineClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionColumnClause.
    def enterScreenDescriptionColumnClause(self, ctx:CobolParser.ScreenDescriptionColumnClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionColumnClause.
    def exitScreenDescriptionColumnClause(self, ctx:CobolParser.ScreenDescriptionColumnClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionForegroundColorClause.
    def enterScreenDescriptionForegroundColorClause(self, ctx:CobolParser.ScreenDescriptionForegroundColorClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionForegroundColorClause.
    def exitScreenDescriptionForegroundColorClause(self, ctx:CobolParser.ScreenDescriptionForegroundColorClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionBackgroundColorClause.
    def enterScreenDescriptionBackgroundColorClause(self, ctx:CobolParser.ScreenDescriptionBackgroundColorClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionBackgroundColorClause.
    def exitScreenDescriptionBackgroundColorClause(self, ctx:CobolParser.ScreenDescriptionBackgroundColorClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionControlClause.
    def enterScreenDescriptionControlClause(self, ctx:CobolParser.ScreenDescriptionControlClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionControlClause.
    def exitScreenDescriptionControlClause(self, ctx:CobolParser.ScreenDescriptionControlClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionValueClause.
    def enterScreenDescriptionValueClause(self, ctx:CobolParser.ScreenDescriptionValueClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionValueClause.
    def exitScreenDescriptionValueClause(self, ctx:CobolParser.ScreenDescriptionValueClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionPictureClause.
    def enterScreenDescriptionPictureClause(self, ctx:CobolParser.ScreenDescriptionPictureClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionPictureClause.
    def exitScreenDescriptionPictureClause(self, ctx:CobolParser.ScreenDescriptionPictureClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionFromClause.
    def enterScreenDescriptionFromClause(self, ctx:CobolParser.ScreenDescriptionFromClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionFromClause.
    def exitScreenDescriptionFromClause(self, ctx:CobolParser.ScreenDescriptionFromClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionToClause.
    def enterScreenDescriptionToClause(self, ctx:CobolParser.ScreenDescriptionToClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionToClause.
    def exitScreenDescriptionToClause(self, ctx:CobolParser.ScreenDescriptionToClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionUsingClause.
    def enterScreenDescriptionUsingClause(self, ctx:CobolParser.ScreenDescriptionUsingClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionUsingClause.
    def exitScreenDescriptionUsingClause(self, ctx:CobolParser.ScreenDescriptionUsingClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionUsageClause.
    def enterScreenDescriptionUsageClause(self, ctx:CobolParser.ScreenDescriptionUsageClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionUsageClause.
    def exitScreenDescriptionUsageClause(self, ctx:CobolParser.ScreenDescriptionUsageClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionBlankWhenZeroClause.
    def enterScreenDescriptionBlankWhenZeroClause(self, ctx:CobolParser.ScreenDescriptionBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionBlankWhenZeroClause.
    def exitScreenDescriptionBlankWhenZeroClause(self, ctx:CobolParser.ScreenDescriptionBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionJustifiedClause.
    def enterScreenDescriptionJustifiedClause(self, ctx:CobolParser.ScreenDescriptionJustifiedClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionJustifiedClause.
    def exitScreenDescriptionJustifiedClause(self, ctx:CobolParser.ScreenDescriptionJustifiedClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionSignClause.
    def enterScreenDescriptionSignClause(self, ctx:CobolParser.ScreenDescriptionSignClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionSignClause.
    def exitScreenDescriptionSignClause(self, ctx:CobolParser.ScreenDescriptionSignClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionAutoClause.
    def enterScreenDescriptionAutoClause(self, ctx:CobolParser.ScreenDescriptionAutoClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionAutoClause.
    def exitScreenDescriptionAutoClause(self, ctx:CobolParser.ScreenDescriptionAutoClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionSecureClause.
    def enterScreenDescriptionSecureClause(self, ctx:CobolParser.ScreenDescriptionSecureClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionSecureClause.
    def exitScreenDescriptionSecureClause(self, ctx:CobolParser.ScreenDescriptionSecureClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionRequiredClause.
    def enterScreenDescriptionRequiredClause(self, ctx:CobolParser.ScreenDescriptionRequiredClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionRequiredClause.
    def exitScreenDescriptionRequiredClause(self, ctx:CobolParser.ScreenDescriptionRequiredClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionPromptClause.
    def enterScreenDescriptionPromptClause(self, ctx:CobolParser.ScreenDescriptionPromptClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionPromptClause.
    def exitScreenDescriptionPromptClause(self, ctx:CobolParser.ScreenDescriptionPromptClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionPromptOccursClause.
    def enterScreenDescriptionPromptOccursClause(self, ctx:CobolParser.ScreenDescriptionPromptOccursClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionPromptOccursClause.
    def exitScreenDescriptionPromptOccursClause(self, ctx:CobolParser.ScreenDescriptionPromptOccursClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionFullClause.
    def enterScreenDescriptionFullClause(self, ctx:CobolParser.ScreenDescriptionFullClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionFullClause.
    def exitScreenDescriptionFullClause(self, ctx:CobolParser.ScreenDescriptionFullClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#screenDescriptionZeroFillClause.
    def enterScreenDescriptionZeroFillClause(self, ctx:CobolParser.ScreenDescriptionZeroFillClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#screenDescriptionZeroFillClause.
    def exitScreenDescriptionZeroFillClause(self, ctx:CobolParser.ScreenDescriptionZeroFillClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportSection.
    def enterReportSection(self, ctx:CobolParser.ReportSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#reportSection.
    def exitReportSection(self, ctx:CobolParser.ReportSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#reportDescription.
    def enterReportDescription(self, ctx:CobolParser.ReportDescriptionContext):
        pass

    # Exit a parse tree produced by CobolParser#reportDescription.
    def exitReportDescription(self, ctx:CobolParser.ReportDescriptionContext):
        pass


    # Enter a parse tree produced by CobolParser#reportDescriptionEntry.
    def enterReportDescriptionEntry(self, ctx:CobolParser.ReportDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#reportDescriptionEntry.
    def exitReportDescriptionEntry(self, ctx:CobolParser.ReportDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#reportDescriptionGlobalClause.
    def enterReportDescriptionGlobalClause(self, ctx:CobolParser.ReportDescriptionGlobalClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportDescriptionGlobalClause.
    def exitReportDescriptionGlobalClause(self, ctx:CobolParser.ReportDescriptionGlobalClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportDescriptionPageLimitClause.
    def enterReportDescriptionPageLimitClause(self, ctx:CobolParser.ReportDescriptionPageLimitClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportDescriptionPageLimitClause.
    def exitReportDescriptionPageLimitClause(self, ctx:CobolParser.ReportDescriptionPageLimitClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportDescriptionHeadingClause.
    def enterReportDescriptionHeadingClause(self, ctx:CobolParser.ReportDescriptionHeadingClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportDescriptionHeadingClause.
    def exitReportDescriptionHeadingClause(self, ctx:CobolParser.ReportDescriptionHeadingClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportDescriptionFirstDetailClause.
    def enterReportDescriptionFirstDetailClause(self, ctx:CobolParser.ReportDescriptionFirstDetailClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportDescriptionFirstDetailClause.
    def exitReportDescriptionFirstDetailClause(self, ctx:CobolParser.ReportDescriptionFirstDetailClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportDescriptionLastDetailClause.
    def enterReportDescriptionLastDetailClause(self, ctx:CobolParser.ReportDescriptionLastDetailClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportDescriptionLastDetailClause.
    def exitReportDescriptionLastDetailClause(self, ctx:CobolParser.ReportDescriptionLastDetailClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportDescriptionFootingClause.
    def enterReportDescriptionFootingClause(self, ctx:CobolParser.ReportDescriptionFootingClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportDescriptionFootingClause.
    def exitReportDescriptionFootingClause(self, ctx:CobolParser.ReportDescriptionFootingClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupDescriptionEntry.
    def enterReportGroupDescriptionEntry(self, ctx:CobolParser.ReportGroupDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupDescriptionEntry.
    def exitReportGroupDescriptionEntry(self, ctx:CobolParser.ReportGroupDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupDescriptionEntryFormat1.
    def enterReportGroupDescriptionEntryFormat1(self, ctx:CobolParser.ReportGroupDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupDescriptionEntryFormat1.
    def exitReportGroupDescriptionEntryFormat1(self, ctx:CobolParser.ReportGroupDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupDescriptionEntryFormat2.
    def enterReportGroupDescriptionEntryFormat2(self, ctx:CobolParser.ReportGroupDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupDescriptionEntryFormat2.
    def exitReportGroupDescriptionEntryFormat2(self, ctx:CobolParser.ReportGroupDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupDescriptionEntryFormat3.
    def enterReportGroupDescriptionEntryFormat3(self, ctx:CobolParser.ReportGroupDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupDescriptionEntryFormat3.
    def exitReportGroupDescriptionEntryFormat3(self, ctx:CobolParser.ReportGroupDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupBlankWhenZeroClause.
    def enterReportGroupBlankWhenZeroClause(self, ctx:CobolParser.ReportGroupBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupBlankWhenZeroClause.
    def exitReportGroupBlankWhenZeroClause(self, ctx:CobolParser.ReportGroupBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupColumnNumberClause.
    def enterReportGroupColumnNumberClause(self, ctx:CobolParser.ReportGroupColumnNumberClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupColumnNumberClause.
    def exitReportGroupColumnNumberClause(self, ctx:CobolParser.ReportGroupColumnNumberClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupIndicateClause.
    def enterReportGroupIndicateClause(self, ctx:CobolParser.ReportGroupIndicateClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupIndicateClause.
    def exitReportGroupIndicateClause(self, ctx:CobolParser.ReportGroupIndicateClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupJustifiedClause.
    def enterReportGroupJustifiedClause(self, ctx:CobolParser.ReportGroupJustifiedClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupJustifiedClause.
    def exitReportGroupJustifiedClause(self, ctx:CobolParser.ReportGroupJustifiedClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupLineNumberClause.
    def enterReportGroupLineNumberClause(self, ctx:CobolParser.ReportGroupLineNumberClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupLineNumberClause.
    def exitReportGroupLineNumberClause(self, ctx:CobolParser.ReportGroupLineNumberClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupLineNumberNextPage.
    def enterReportGroupLineNumberNextPage(self, ctx:CobolParser.ReportGroupLineNumberNextPageContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupLineNumberNextPage.
    def exitReportGroupLineNumberNextPage(self, ctx:CobolParser.ReportGroupLineNumberNextPageContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupLineNumberPlus.
    def enterReportGroupLineNumberPlus(self, ctx:CobolParser.ReportGroupLineNumberPlusContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupLineNumberPlus.
    def exitReportGroupLineNumberPlus(self, ctx:CobolParser.ReportGroupLineNumberPlusContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupNextGroupClause.
    def enterReportGroupNextGroupClause(self, ctx:CobolParser.ReportGroupNextGroupClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupNextGroupClause.
    def exitReportGroupNextGroupClause(self, ctx:CobolParser.ReportGroupNextGroupClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupNextGroupPlus.
    def enterReportGroupNextGroupPlus(self, ctx:CobolParser.ReportGroupNextGroupPlusContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupNextGroupPlus.
    def exitReportGroupNextGroupPlus(self, ctx:CobolParser.ReportGroupNextGroupPlusContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupNextGroupNextPage.
    def enterReportGroupNextGroupNextPage(self, ctx:CobolParser.ReportGroupNextGroupNextPageContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupNextGroupNextPage.
    def exitReportGroupNextGroupNextPage(self, ctx:CobolParser.ReportGroupNextGroupNextPageContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupPictureClause.
    def enterReportGroupPictureClause(self, ctx:CobolParser.ReportGroupPictureClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupPictureClause.
    def exitReportGroupPictureClause(self, ctx:CobolParser.ReportGroupPictureClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupResetClause.
    def enterReportGroupResetClause(self, ctx:CobolParser.ReportGroupResetClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupResetClause.
    def exitReportGroupResetClause(self, ctx:CobolParser.ReportGroupResetClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupSignClause.
    def enterReportGroupSignClause(self, ctx:CobolParser.ReportGroupSignClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupSignClause.
    def exitReportGroupSignClause(self, ctx:CobolParser.ReportGroupSignClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupSourceClause.
    def enterReportGroupSourceClause(self, ctx:CobolParser.ReportGroupSourceClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupSourceClause.
    def exitReportGroupSourceClause(self, ctx:CobolParser.ReportGroupSourceClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupSumClause.
    def enterReportGroupSumClause(self, ctx:CobolParser.ReportGroupSumClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupSumClause.
    def exitReportGroupSumClause(self, ctx:CobolParser.ReportGroupSumClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupTypeClause.
    def enterReportGroupTypeClause(self, ctx:CobolParser.ReportGroupTypeClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupTypeClause.
    def exitReportGroupTypeClause(self, ctx:CobolParser.ReportGroupTypeClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupTypeReportHeading.
    def enterReportGroupTypeReportHeading(self, ctx:CobolParser.ReportGroupTypeReportHeadingContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupTypeReportHeading.
    def exitReportGroupTypeReportHeading(self, ctx:CobolParser.ReportGroupTypeReportHeadingContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupTypePageHeading.
    def enterReportGroupTypePageHeading(self, ctx:CobolParser.ReportGroupTypePageHeadingContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupTypePageHeading.
    def exitReportGroupTypePageHeading(self, ctx:CobolParser.ReportGroupTypePageHeadingContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupTypeControlHeading.
    def enterReportGroupTypeControlHeading(self, ctx:CobolParser.ReportGroupTypeControlHeadingContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupTypeControlHeading.
    def exitReportGroupTypeControlHeading(self, ctx:CobolParser.ReportGroupTypeControlHeadingContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupTypeDetail.
    def enterReportGroupTypeDetail(self, ctx:CobolParser.ReportGroupTypeDetailContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupTypeDetail.
    def exitReportGroupTypeDetail(self, ctx:CobolParser.ReportGroupTypeDetailContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupTypeControlFooting.
    def enterReportGroupTypeControlFooting(self, ctx:CobolParser.ReportGroupTypeControlFootingContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupTypeControlFooting.
    def exitReportGroupTypeControlFooting(self, ctx:CobolParser.ReportGroupTypeControlFootingContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupUsageClause.
    def enterReportGroupUsageClause(self, ctx:CobolParser.ReportGroupUsageClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupUsageClause.
    def exitReportGroupUsageClause(self, ctx:CobolParser.ReportGroupUsageClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupTypePageFooting.
    def enterReportGroupTypePageFooting(self, ctx:CobolParser.ReportGroupTypePageFootingContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupTypePageFooting.
    def exitReportGroupTypePageFooting(self, ctx:CobolParser.ReportGroupTypePageFootingContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupTypeReportFooting.
    def enterReportGroupTypeReportFooting(self, ctx:CobolParser.ReportGroupTypeReportFootingContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupTypeReportFooting.
    def exitReportGroupTypeReportFooting(self, ctx:CobolParser.ReportGroupTypeReportFootingContext):
        pass


    # Enter a parse tree produced by CobolParser#reportGroupValueClause.
    def enterReportGroupValueClause(self, ctx:CobolParser.ReportGroupValueClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#reportGroupValueClause.
    def exitReportGroupValueClause(self, ctx:CobolParser.ReportGroupValueClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#programLibrarySection.
    def enterProgramLibrarySection(self, ctx:CobolParser.ProgramLibrarySectionContext):
        pass

    # Exit a parse tree produced by CobolParser#programLibrarySection.
    def exitProgramLibrarySection(self, ctx:CobolParser.ProgramLibrarySectionContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryDescriptionEntry.
    def enterLibraryDescriptionEntry(self, ctx:CobolParser.LibraryDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryDescriptionEntry.
    def exitLibraryDescriptionEntry(self, ctx:CobolParser.LibraryDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryDescriptionEntryFormat1.
    def enterLibraryDescriptionEntryFormat1(self, ctx:CobolParser.LibraryDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CobolParser#libraryDescriptionEntryFormat1.
    def exitLibraryDescriptionEntryFormat1(self, ctx:CobolParser.LibraryDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CobolParser#libraryDescriptionEntryFormat2.
    def enterLibraryDescriptionEntryFormat2(self, ctx:CobolParser.LibraryDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CobolParser#libraryDescriptionEntryFormat2.
    def exitLibraryDescriptionEntryFormat2(self, ctx:CobolParser.LibraryDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CobolParser#libraryAttributeClauseFormat1.
    def enterLibraryAttributeClauseFormat1(self, ctx:CobolParser.LibraryAttributeClauseFormat1Context):
        pass

    # Exit a parse tree produced by CobolParser#libraryAttributeClauseFormat1.
    def exitLibraryAttributeClauseFormat1(self, ctx:CobolParser.LibraryAttributeClauseFormat1Context):
        pass


    # Enter a parse tree produced by CobolParser#libraryAttributeClauseFormat2.
    def enterLibraryAttributeClauseFormat2(self, ctx:CobolParser.LibraryAttributeClauseFormat2Context):
        pass

    # Exit a parse tree produced by CobolParser#libraryAttributeClauseFormat2.
    def exitLibraryAttributeClauseFormat2(self, ctx:CobolParser.LibraryAttributeClauseFormat2Context):
        pass


    # Enter a parse tree produced by CobolParser#libraryAttributeFunction.
    def enterLibraryAttributeFunction(self, ctx:CobolParser.LibraryAttributeFunctionContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryAttributeFunction.
    def exitLibraryAttributeFunction(self, ctx:CobolParser.LibraryAttributeFunctionContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryAttributeParameter.
    def enterLibraryAttributeParameter(self, ctx:CobolParser.LibraryAttributeParameterContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryAttributeParameter.
    def exitLibraryAttributeParameter(self, ctx:CobolParser.LibraryAttributeParameterContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryAttributeTitle.
    def enterLibraryAttributeTitle(self, ctx:CobolParser.LibraryAttributeTitleContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryAttributeTitle.
    def exitLibraryAttributeTitle(self, ctx:CobolParser.LibraryAttributeTitleContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryEntryProcedureClauseFormat1.
    def enterLibraryEntryProcedureClauseFormat1(self, ctx:CobolParser.LibraryEntryProcedureClauseFormat1Context):
        pass

    # Exit a parse tree produced by CobolParser#libraryEntryProcedureClauseFormat1.
    def exitLibraryEntryProcedureClauseFormat1(self, ctx:CobolParser.LibraryEntryProcedureClauseFormat1Context):
        pass


    # Enter a parse tree produced by CobolParser#libraryEntryProcedureClauseFormat2.
    def enterLibraryEntryProcedureClauseFormat2(self, ctx:CobolParser.LibraryEntryProcedureClauseFormat2Context):
        pass

    # Exit a parse tree produced by CobolParser#libraryEntryProcedureClauseFormat2.
    def exitLibraryEntryProcedureClauseFormat2(self, ctx:CobolParser.LibraryEntryProcedureClauseFormat2Context):
        pass


    # Enter a parse tree produced by CobolParser#libraryEntryProcedureForClause.
    def enterLibraryEntryProcedureForClause(self, ctx:CobolParser.LibraryEntryProcedureForClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryEntryProcedureForClause.
    def exitLibraryEntryProcedureForClause(self, ctx:CobolParser.LibraryEntryProcedureForClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryEntryProcedureGivingClause.
    def enterLibraryEntryProcedureGivingClause(self, ctx:CobolParser.LibraryEntryProcedureGivingClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryEntryProcedureGivingClause.
    def exitLibraryEntryProcedureGivingClause(self, ctx:CobolParser.LibraryEntryProcedureGivingClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryEntryProcedureUsingClause.
    def enterLibraryEntryProcedureUsingClause(self, ctx:CobolParser.LibraryEntryProcedureUsingClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryEntryProcedureUsingClause.
    def exitLibraryEntryProcedureUsingClause(self, ctx:CobolParser.LibraryEntryProcedureUsingClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryEntryProcedureUsingName.
    def enterLibraryEntryProcedureUsingName(self, ctx:CobolParser.LibraryEntryProcedureUsingNameContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryEntryProcedureUsingName.
    def exitLibraryEntryProcedureUsingName(self, ctx:CobolParser.LibraryEntryProcedureUsingNameContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryEntryProcedureWithClause.
    def enterLibraryEntryProcedureWithClause(self, ctx:CobolParser.LibraryEntryProcedureWithClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryEntryProcedureWithClause.
    def exitLibraryEntryProcedureWithClause(self, ctx:CobolParser.LibraryEntryProcedureWithClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryEntryProcedureWithName.
    def enterLibraryEntryProcedureWithName(self, ctx:CobolParser.LibraryEntryProcedureWithNameContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryEntryProcedureWithName.
    def exitLibraryEntryProcedureWithName(self, ctx:CobolParser.LibraryEntryProcedureWithNameContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryIsCommonClause.
    def enterLibraryIsCommonClause(self, ctx:CobolParser.LibraryIsCommonClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryIsCommonClause.
    def exitLibraryIsCommonClause(self, ctx:CobolParser.LibraryIsCommonClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryIsGlobalClause.
    def enterLibraryIsGlobalClause(self, ctx:CobolParser.LibraryIsGlobalClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryIsGlobalClause.
    def exitLibraryIsGlobalClause(self, ctx:CobolParser.LibraryIsGlobalClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataDescriptionEntry.
    def enterDataDescriptionEntry(self, ctx:CobolParser.DataDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#dataDescriptionEntry.
    def exitDataDescriptionEntry(self, ctx:CobolParser.DataDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolParser#dataDescriptionEntryFormat1.
    def enterDataDescriptionEntryFormat1(self, ctx:CobolParser.DataDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CobolParser#dataDescriptionEntryFormat1.
    def exitDataDescriptionEntryFormat1(self, ctx:CobolParser.DataDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CobolParser#dataDescriptionEntryFormat2.
    def enterDataDescriptionEntryFormat2(self, ctx:CobolParser.DataDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CobolParser#dataDescriptionEntryFormat2.
    def exitDataDescriptionEntryFormat2(self, ctx:CobolParser.DataDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CobolParser#dataDescriptionEntryFormat3.
    def enterDataDescriptionEntryFormat3(self, ctx:CobolParser.DataDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by CobolParser#dataDescriptionEntryFormat3.
    def exitDataDescriptionEntryFormat3(self, ctx:CobolParser.DataDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by CobolParser#dataDescriptionEntryExecSql.
    def enterDataDescriptionEntryExecSql(self, ctx:CobolParser.DataDescriptionEntryExecSqlContext):
        pass

    # Exit a parse tree produced by CobolParser#dataDescriptionEntryExecSql.
    def exitDataDescriptionEntryExecSql(self, ctx:CobolParser.DataDescriptionEntryExecSqlContext):
        pass


    # Enter a parse tree produced by CobolParser#dataAlignedClause.
    def enterDataAlignedClause(self, ctx:CobolParser.DataAlignedClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataAlignedClause.
    def exitDataAlignedClause(self, ctx:CobolParser.DataAlignedClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataBlankWhenZeroClause.
    def enterDataBlankWhenZeroClause(self, ctx:CobolParser.DataBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataBlankWhenZeroClause.
    def exitDataBlankWhenZeroClause(self, ctx:CobolParser.DataBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataCommonOwnLocalClause.
    def enterDataCommonOwnLocalClause(self, ctx:CobolParser.DataCommonOwnLocalClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataCommonOwnLocalClause.
    def exitDataCommonOwnLocalClause(self, ctx:CobolParser.DataCommonOwnLocalClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataExternalClause.
    def enterDataExternalClause(self, ctx:CobolParser.DataExternalClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataExternalClause.
    def exitDataExternalClause(self, ctx:CobolParser.DataExternalClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataGlobalClause.
    def enterDataGlobalClause(self, ctx:CobolParser.DataGlobalClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataGlobalClause.
    def exitDataGlobalClause(self, ctx:CobolParser.DataGlobalClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataIntegerStringClause.
    def enterDataIntegerStringClause(self, ctx:CobolParser.DataIntegerStringClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataIntegerStringClause.
    def exitDataIntegerStringClause(self, ctx:CobolParser.DataIntegerStringClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataJustifiedClause.
    def enterDataJustifiedClause(self, ctx:CobolParser.DataJustifiedClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataJustifiedClause.
    def exitDataJustifiedClause(self, ctx:CobolParser.DataJustifiedClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataOccursClause.
    def enterDataOccursClause(self, ctx:CobolParser.DataOccursClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataOccursClause.
    def exitDataOccursClause(self, ctx:CobolParser.DataOccursClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataOccursTo.
    def enterDataOccursTo(self, ctx:CobolParser.DataOccursToContext):
        pass

    # Exit a parse tree produced by CobolParser#dataOccursTo.
    def exitDataOccursTo(self, ctx:CobolParser.DataOccursToContext):
        pass


    # Enter a parse tree produced by CobolParser#dataOccursDepending.
    def enterDataOccursDepending(self, ctx:CobolParser.DataOccursDependingContext):
        pass

    # Exit a parse tree produced by CobolParser#dataOccursDepending.
    def exitDataOccursDepending(self, ctx:CobolParser.DataOccursDependingContext):
        pass


    # Enter a parse tree produced by CobolParser#dataOccursSort.
    def enterDataOccursSort(self, ctx:CobolParser.DataOccursSortContext):
        pass

    # Exit a parse tree produced by CobolParser#dataOccursSort.
    def exitDataOccursSort(self, ctx:CobolParser.DataOccursSortContext):
        pass


    # Enter a parse tree produced by CobolParser#dataOccursIndexed.
    def enterDataOccursIndexed(self, ctx:CobolParser.DataOccursIndexedContext):
        pass

    # Exit a parse tree produced by CobolParser#dataOccursIndexed.
    def exitDataOccursIndexed(self, ctx:CobolParser.DataOccursIndexedContext):
        pass


    # Enter a parse tree produced by CobolParser#dataPictureClause.
    def enterDataPictureClause(self, ctx:CobolParser.DataPictureClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataPictureClause.
    def exitDataPictureClause(self, ctx:CobolParser.DataPictureClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#pictureString.
    def enterPictureString(self, ctx:CobolParser.PictureStringContext):
        pass

    # Exit a parse tree produced by CobolParser#pictureString.
    def exitPictureString(self, ctx:CobolParser.PictureStringContext):
        pass


    # Enter a parse tree produced by CobolParser#pictureChars.
    def enterPictureChars(self, ctx:CobolParser.PictureCharsContext):
        pass

    # Exit a parse tree produced by CobolParser#pictureChars.
    def exitPictureChars(self, ctx:CobolParser.PictureCharsContext):
        pass


    # Enter a parse tree produced by CobolParser#pictureCardinality.
    def enterPictureCardinality(self, ctx:CobolParser.PictureCardinalityContext):
        pass

    # Exit a parse tree produced by CobolParser#pictureCardinality.
    def exitPictureCardinality(self, ctx:CobolParser.PictureCardinalityContext):
        pass


    # Enter a parse tree produced by CobolParser#dataReceivedByClause.
    def enterDataReceivedByClause(self, ctx:CobolParser.DataReceivedByClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataReceivedByClause.
    def exitDataReceivedByClause(self, ctx:CobolParser.DataReceivedByClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataRecordAreaClause.
    def enterDataRecordAreaClause(self, ctx:CobolParser.DataRecordAreaClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataRecordAreaClause.
    def exitDataRecordAreaClause(self, ctx:CobolParser.DataRecordAreaClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataRedefinesClause.
    def enterDataRedefinesClause(self, ctx:CobolParser.DataRedefinesClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataRedefinesClause.
    def exitDataRedefinesClause(self, ctx:CobolParser.DataRedefinesClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataRenamesClause.
    def enterDataRenamesClause(self, ctx:CobolParser.DataRenamesClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataRenamesClause.
    def exitDataRenamesClause(self, ctx:CobolParser.DataRenamesClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataSignClause.
    def enterDataSignClause(self, ctx:CobolParser.DataSignClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataSignClause.
    def exitDataSignClause(self, ctx:CobolParser.DataSignClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataSynchronizedClause.
    def enterDataSynchronizedClause(self, ctx:CobolParser.DataSynchronizedClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataSynchronizedClause.
    def exitDataSynchronizedClause(self, ctx:CobolParser.DataSynchronizedClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataThreadLocalClause.
    def enterDataThreadLocalClause(self, ctx:CobolParser.DataThreadLocalClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataThreadLocalClause.
    def exitDataThreadLocalClause(self, ctx:CobolParser.DataThreadLocalClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataTypeClause.
    def enterDataTypeClause(self, ctx:CobolParser.DataTypeClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataTypeClause.
    def exitDataTypeClause(self, ctx:CobolParser.DataTypeClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataTypeDefClause.
    def enterDataTypeDefClause(self, ctx:CobolParser.DataTypeDefClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataTypeDefClause.
    def exitDataTypeDefClause(self, ctx:CobolParser.DataTypeDefClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataUsageClause.
    def enterDataUsageClause(self, ctx:CobolParser.DataUsageClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataUsageClause.
    def exitDataUsageClause(self, ctx:CobolParser.DataUsageClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataUsingClause.
    def enterDataUsingClause(self, ctx:CobolParser.DataUsingClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataUsingClause.
    def exitDataUsingClause(self, ctx:CobolParser.DataUsingClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataValueClause.
    def enterDataValueClause(self, ctx:CobolParser.DataValueClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataValueClause.
    def exitDataValueClause(self, ctx:CobolParser.DataValueClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#dataValueInterval.
    def enterDataValueInterval(self, ctx:CobolParser.DataValueIntervalContext):
        pass

    # Exit a parse tree produced by CobolParser#dataValueInterval.
    def exitDataValueInterval(self, ctx:CobolParser.DataValueIntervalContext):
        pass


    # Enter a parse tree produced by CobolParser#dataValueIntervalFrom.
    def enterDataValueIntervalFrom(self, ctx:CobolParser.DataValueIntervalFromContext):
        pass

    # Exit a parse tree produced by CobolParser#dataValueIntervalFrom.
    def exitDataValueIntervalFrom(self, ctx:CobolParser.DataValueIntervalFromContext):
        pass


    # Enter a parse tree produced by CobolParser#dataValueIntervalTo.
    def enterDataValueIntervalTo(self, ctx:CobolParser.DataValueIntervalToContext):
        pass

    # Exit a parse tree produced by CobolParser#dataValueIntervalTo.
    def exitDataValueIntervalTo(self, ctx:CobolParser.DataValueIntervalToContext):
        pass


    # Enter a parse tree produced by CobolParser#dataWithLowerBoundsClause.
    def enterDataWithLowerBoundsClause(self, ctx:CobolParser.DataWithLowerBoundsClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#dataWithLowerBoundsClause.
    def exitDataWithLowerBoundsClause(self, ctx:CobolParser.DataWithLowerBoundsClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivision.
    def enterProcedureDivision(self, ctx:CobolParser.ProcedureDivisionContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivision.
    def exitProcedureDivision(self, ctx:CobolParser.ProcedureDivisionContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivisionUsingClause.
    def enterProcedureDivisionUsingClause(self, ctx:CobolParser.ProcedureDivisionUsingClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivisionUsingClause.
    def exitProcedureDivisionUsingClause(self, ctx:CobolParser.ProcedureDivisionUsingClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivisionGivingClause.
    def enterProcedureDivisionGivingClause(self, ctx:CobolParser.ProcedureDivisionGivingClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivisionGivingClause.
    def exitProcedureDivisionGivingClause(self, ctx:CobolParser.ProcedureDivisionGivingClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivisionUsingParameter.
    def enterProcedureDivisionUsingParameter(self, ctx:CobolParser.ProcedureDivisionUsingParameterContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivisionUsingParameter.
    def exitProcedureDivisionUsingParameter(self, ctx:CobolParser.ProcedureDivisionUsingParameterContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivisionByReferencePhrase.
    def enterProcedureDivisionByReferencePhrase(self, ctx:CobolParser.ProcedureDivisionByReferencePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivisionByReferencePhrase.
    def exitProcedureDivisionByReferencePhrase(self, ctx:CobolParser.ProcedureDivisionByReferencePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivisionByReference.
    def enterProcedureDivisionByReference(self, ctx:CobolParser.ProcedureDivisionByReferenceContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivisionByReference.
    def exitProcedureDivisionByReference(self, ctx:CobolParser.ProcedureDivisionByReferenceContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivisionByValuePhrase.
    def enterProcedureDivisionByValuePhrase(self, ctx:CobolParser.ProcedureDivisionByValuePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivisionByValuePhrase.
    def exitProcedureDivisionByValuePhrase(self, ctx:CobolParser.ProcedureDivisionByValuePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivisionByValue.
    def enterProcedureDivisionByValue(self, ctx:CobolParser.ProcedureDivisionByValueContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivisionByValue.
    def exitProcedureDivisionByValue(self, ctx:CobolParser.ProcedureDivisionByValueContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDeclaratives.
    def enterProcedureDeclaratives(self, ctx:CobolParser.ProcedureDeclarativesContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDeclaratives.
    def exitProcedureDeclaratives(self, ctx:CobolParser.ProcedureDeclarativesContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDeclarative.
    def enterProcedureDeclarative(self, ctx:CobolParser.ProcedureDeclarativeContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDeclarative.
    def exitProcedureDeclarative(self, ctx:CobolParser.ProcedureDeclarativeContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureSectionHeader.
    def enterProcedureSectionHeader(self, ctx:CobolParser.ProcedureSectionHeaderContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureSectionHeader.
    def exitProcedureSectionHeader(self, ctx:CobolParser.ProcedureSectionHeaderContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureDivisionBody.
    def enterProcedureDivisionBody(self, ctx:CobolParser.ProcedureDivisionBodyContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureDivisionBody.
    def exitProcedureDivisionBody(self, ctx:CobolParser.ProcedureDivisionBodyContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureSection.
    def enterProcedureSection(self, ctx:CobolParser.ProcedureSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureSection.
    def exitProcedureSection(self, ctx:CobolParser.ProcedureSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#paragraphs.
    def enterParagraphs(self, ctx:CobolParser.ParagraphsContext):
        pass

    # Exit a parse tree produced by CobolParser#paragraphs.
    def exitParagraphs(self, ctx:CobolParser.ParagraphsContext):
        pass


    # Enter a parse tree produced by CobolParser#paragraph.
    def enterParagraph(self, ctx:CobolParser.ParagraphContext):
        pass

    # Exit a parse tree produced by CobolParser#paragraph.
    def exitParagraph(self, ctx:CobolParser.ParagraphContext):
        pass


    # Enter a parse tree produced by CobolParser#sentence.
    def enterSentence(self, ctx:CobolParser.SentenceContext):
        pass

    # Exit a parse tree produced by CobolParser#sentence.
    def exitSentence(self, ctx:CobolParser.SentenceContext):
        pass


    # Enter a parse tree produced by CobolParser#statement.
    def enterStatement(self, ctx:CobolParser.StatementContext):
        pass

    # Exit a parse tree produced by CobolParser#statement.
    def exitStatement(self, ctx:CobolParser.StatementContext):
        pass


    # Enter a parse tree produced by CobolParser#acceptStatement.
    def enterAcceptStatement(self, ctx:CobolParser.AcceptStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#acceptStatement.
    def exitAcceptStatement(self, ctx:CobolParser.AcceptStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#acceptFromDateStatement.
    def enterAcceptFromDateStatement(self, ctx:CobolParser.AcceptFromDateStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#acceptFromDateStatement.
    def exitAcceptFromDateStatement(self, ctx:CobolParser.AcceptFromDateStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#acceptFromMnemonicStatement.
    def enterAcceptFromMnemonicStatement(self, ctx:CobolParser.AcceptFromMnemonicStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#acceptFromMnemonicStatement.
    def exitAcceptFromMnemonicStatement(self, ctx:CobolParser.AcceptFromMnemonicStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#acceptFromEscapeKeyStatement.
    def enterAcceptFromEscapeKeyStatement(self, ctx:CobolParser.AcceptFromEscapeKeyStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#acceptFromEscapeKeyStatement.
    def exitAcceptFromEscapeKeyStatement(self, ctx:CobolParser.AcceptFromEscapeKeyStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#acceptMessageCountStatement.
    def enterAcceptMessageCountStatement(self, ctx:CobolParser.AcceptMessageCountStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#acceptMessageCountStatement.
    def exitAcceptMessageCountStatement(self, ctx:CobolParser.AcceptMessageCountStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#addStatement.
    def enterAddStatement(self, ctx:CobolParser.AddStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#addStatement.
    def exitAddStatement(self, ctx:CobolParser.AddStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#addToStatement.
    def enterAddToStatement(self, ctx:CobolParser.AddToStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#addToStatement.
    def exitAddToStatement(self, ctx:CobolParser.AddToStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#addToGivingStatement.
    def enterAddToGivingStatement(self, ctx:CobolParser.AddToGivingStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#addToGivingStatement.
    def exitAddToGivingStatement(self, ctx:CobolParser.AddToGivingStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#addCorrespondingStatement.
    def enterAddCorrespondingStatement(self, ctx:CobolParser.AddCorrespondingStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#addCorrespondingStatement.
    def exitAddCorrespondingStatement(self, ctx:CobolParser.AddCorrespondingStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#addFrom.
    def enterAddFrom(self, ctx:CobolParser.AddFromContext):
        pass

    # Exit a parse tree produced by CobolParser#addFrom.
    def exitAddFrom(self, ctx:CobolParser.AddFromContext):
        pass


    # Enter a parse tree produced by CobolParser#addTo.
    def enterAddTo(self, ctx:CobolParser.AddToContext):
        pass

    # Exit a parse tree produced by CobolParser#addTo.
    def exitAddTo(self, ctx:CobolParser.AddToContext):
        pass


    # Enter a parse tree produced by CobolParser#addToGiving.
    def enterAddToGiving(self, ctx:CobolParser.AddToGivingContext):
        pass

    # Exit a parse tree produced by CobolParser#addToGiving.
    def exitAddToGiving(self, ctx:CobolParser.AddToGivingContext):
        pass


    # Enter a parse tree produced by CobolParser#addGiving.
    def enterAddGiving(self, ctx:CobolParser.AddGivingContext):
        pass

    # Exit a parse tree produced by CobolParser#addGiving.
    def exitAddGiving(self, ctx:CobolParser.AddGivingContext):
        pass


    # Enter a parse tree produced by CobolParser#alteredGoTo.
    def enterAlteredGoTo(self, ctx:CobolParser.AlteredGoToContext):
        pass

    # Exit a parse tree produced by CobolParser#alteredGoTo.
    def exitAlteredGoTo(self, ctx:CobolParser.AlteredGoToContext):
        pass


    # Enter a parse tree produced by CobolParser#alterStatement.
    def enterAlterStatement(self, ctx:CobolParser.AlterStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#alterStatement.
    def exitAlterStatement(self, ctx:CobolParser.AlterStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#alterProceedTo.
    def enterAlterProceedTo(self, ctx:CobolParser.AlterProceedToContext):
        pass

    # Exit a parse tree produced by CobolParser#alterProceedTo.
    def exitAlterProceedTo(self, ctx:CobolParser.AlterProceedToContext):
        pass


    # Enter a parse tree produced by CobolParser#callStatement.
    def enterCallStatement(self, ctx:CobolParser.CallStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#callStatement.
    def exitCallStatement(self, ctx:CobolParser.CallStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#callUsingPhrase.
    def enterCallUsingPhrase(self, ctx:CobolParser.CallUsingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#callUsingPhrase.
    def exitCallUsingPhrase(self, ctx:CobolParser.CallUsingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#callUsingParameter.
    def enterCallUsingParameter(self, ctx:CobolParser.CallUsingParameterContext):
        pass

    # Exit a parse tree produced by CobolParser#callUsingParameter.
    def exitCallUsingParameter(self, ctx:CobolParser.CallUsingParameterContext):
        pass


    # Enter a parse tree produced by CobolParser#callByReferencePhrase.
    def enterCallByReferencePhrase(self, ctx:CobolParser.CallByReferencePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#callByReferencePhrase.
    def exitCallByReferencePhrase(self, ctx:CobolParser.CallByReferencePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#callByReference.
    def enterCallByReference(self, ctx:CobolParser.CallByReferenceContext):
        pass

    # Exit a parse tree produced by CobolParser#callByReference.
    def exitCallByReference(self, ctx:CobolParser.CallByReferenceContext):
        pass


    # Enter a parse tree produced by CobolParser#callByValuePhrase.
    def enterCallByValuePhrase(self, ctx:CobolParser.CallByValuePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#callByValuePhrase.
    def exitCallByValuePhrase(self, ctx:CobolParser.CallByValuePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#callByValue.
    def enterCallByValue(self, ctx:CobolParser.CallByValueContext):
        pass

    # Exit a parse tree produced by CobolParser#callByValue.
    def exitCallByValue(self, ctx:CobolParser.CallByValueContext):
        pass


    # Enter a parse tree produced by CobolParser#callByContentPhrase.
    def enterCallByContentPhrase(self, ctx:CobolParser.CallByContentPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#callByContentPhrase.
    def exitCallByContentPhrase(self, ctx:CobolParser.CallByContentPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#callByContent.
    def enterCallByContent(self, ctx:CobolParser.CallByContentContext):
        pass

    # Exit a parse tree produced by CobolParser#callByContent.
    def exitCallByContent(self, ctx:CobolParser.CallByContentContext):
        pass


    # Enter a parse tree produced by CobolParser#callGivingPhrase.
    def enterCallGivingPhrase(self, ctx:CobolParser.CallGivingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#callGivingPhrase.
    def exitCallGivingPhrase(self, ctx:CobolParser.CallGivingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#cancelStatement.
    def enterCancelStatement(self, ctx:CobolParser.CancelStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#cancelStatement.
    def exitCancelStatement(self, ctx:CobolParser.CancelStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#cancelCall.
    def enterCancelCall(self, ctx:CobolParser.CancelCallContext):
        pass

    # Exit a parse tree produced by CobolParser#cancelCall.
    def exitCancelCall(self, ctx:CobolParser.CancelCallContext):
        pass


    # Enter a parse tree produced by CobolParser#closeStatement.
    def enterCloseStatement(self, ctx:CobolParser.CloseStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#closeStatement.
    def exitCloseStatement(self, ctx:CobolParser.CloseStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#closeFile.
    def enterCloseFile(self, ctx:CobolParser.CloseFileContext):
        pass

    # Exit a parse tree produced by CobolParser#closeFile.
    def exitCloseFile(self, ctx:CobolParser.CloseFileContext):
        pass


    # Enter a parse tree produced by CobolParser#closeReelUnitStatement.
    def enterCloseReelUnitStatement(self, ctx:CobolParser.CloseReelUnitStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#closeReelUnitStatement.
    def exitCloseReelUnitStatement(self, ctx:CobolParser.CloseReelUnitStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#closeRelativeStatement.
    def enterCloseRelativeStatement(self, ctx:CobolParser.CloseRelativeStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#closeRelativeStatement.
    def exitCloseRelativeStatement(self, ctx:CobolParser.CloseRelativeStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#closePortFileIOStatement.
    def enterClosePortFileIOStatement(self, ctx:CobolParser.ClosePortFileIOStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#closePortFileIOStatement.
    def exitClosePortFileIOStatement(self, ctx:CobolParser.ClosePortFileIOStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#closePortFileIOUsing.
    def enterClosePortFileIOUsing(self, ctx:CobolParser.ClosePortFileIOUsingContext):
        pass

    # Exit a parse tree produced by CobolParser#closePortFileIOUsing.
    def exitClosePortFileIOUsing(self, ctx:CobolParser.ClosePortFileIOUsingContext):
        pass


    # Enter a parse tree produced by CobolParser#closePortFileIOUsingCloseDisposition.
    def enterClosePortFileIOUsingCloseDisposition(self, ctx:CobolParser.ClosePortFileIOUsingCloseDispositionContext):
        pass

    # Exit a parse tree produced by CobolParser#closePortFileIOUsingCloseDisposition.
    def exitClosePortFileIOUsingCloseDisposition(self, ctx:CobolParser.ClosePortFileIOUsingCloseDispositionContext):
        pass


    # Enter a parse tree produced by CobolParser#closePortFileIOUsingAssociatedData.
    def enterClosePortFileIOUsingAssociatedData(self, ctx:CobolParser.ClosePortFileIOUsingAssociatedDataContext):
        pass

    # Exit a parse tree produced by CobolParser#closePortFileIOUsingAssociatedData.
    def exitClosePortFileIOUsingAssociatedData(self, ctx:CobolParser.ClosePortFileIOUsingAssociatedDataContext):
        pass


    # Enter a parse tree produced by CobolParser#closePortFileIOUsingAssociatedDataLength.
    def enterClosePortFileIOUsingAssociatedDataLength(self, ctx:CobolParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        pass

    # Exit a parse tree produced by CobolParser#closePortFileIOUsingAssociatedDataLength.
    def exitClosePortFileIOUsingAssociatedDataLength(self, ctx:CobolParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        pass


    # Enter a parse tree produced by CobolParser#computeStatement.
    def enterComputeStatement(self, ctx:CobolParser.ComputeStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#computeStatement.
    def exitComputeStatement(self, ctx:CobolParser.ComputeStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#computeStore.
    def enterComputeStore(self, ctx:CobolParser.ComputeStoreContext):
        pass

    # Exit a parse tree produced by CobolParser#computeStore.
    def exitComputeStore(self, ctx:CobolParser.ComputeStoreContext):
        pass


    # Enter a parse tree produced by CobolParser#continueStatement.
    def enterContinueStatement(self, ctx:CobolParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#continueStatement.
    def exitContinueStatement(self, ctx:CobolParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#deleteStatement.
    def enterDeleteStatement(self, ctx:CobolParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#deleteStatement.
    def exitDeleteStatement(self, ctx:CobolParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#disableStatement.
    def enterDisableStatement(self, ctx:CobolParser.DisableStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#disableStatement.
    def exitDisableStatement(self, ctx:CobolParser.DisableStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#displayStatement.
    def enterDisplayStatement(self, ctx:CobolParser.DisplayStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#displayStatement.
    def exitDisplayStatement(self, ctx:CobolParser.DisplayStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#displayOperand.
    def enterDisplayOperand(self, ctx:CobolParser.DisplayOperandContext):
        pass

    # Exit a parse tree produced by CobolParser#displayOperand.
    def exitDisplayOperand(self, ctx:CobolParser.DisplayOperandContext):
        pass


    # Enter a parse tree produced by CobolParser#displayAt.
    def enterDisplayAt(self, ctx:CobolParser.DisplayAtContext):
        pass

    # Exit a parse tree produced by CobolParser#displayAt.
    def exitDisplayAt(self, ctx:CobolParser.DisplayAtContext):
        pass


    # Enter a parse tree produced by CobolParser#displayUpon.
    def enterDisplayUpon(self, ctx:CobolParser.DisplayUponContext):
        pass

    # Exit a parse tree produced by CobolParser#displayUpon.
    def exitDisplayUpon(self, ctx:CobolParser.DisplayUponContext):
        pass


    # Enter a parse tree produced by CobolParser#displayWith.
    def enterDisplayWith(self, ctx:CobolParser.DisplayWithContext):
        pass

    # Exit a parse tree produced by CobolParser#displayWith.
    def exitDisplayWith(self, ctx:CobolParser.DisplayWithContext):
        pass


    # Enter a parse tree produced by CobolParser#divideStatement.
    def enterDivideStatement(self, ctx:CobolParser.DivideStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#divideStatement.
    def exitDivideStatement(self, ctx:CobolParser.DivideStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#divideIntoStatement.
    def enterDivideIntoStatement(self, ctx:CobolParser.DivideIntoStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#divideIntoStatement.
    def exitDivideIntoStatement(self, ctx:CobolParser.DivideIntoStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#divideIntoGivingStatement.
    def enterDivideIntoGivingStatement(self, ctx:CobolParser.DivideIntoGivingStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#divideIntoGivingStatement.
    def exitDivideIntoGivingStatement(self, ctx:CobolParser.DivideIntoGivingStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#divideByGivingStatement.
    def enterDivideByGivingStatement(self, ctx:CobolParser.DivideByGivingStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#divideByGivingStatement.
    def exitDivideByGivingStatement(self, ctx:CobolParser.DivideByGivingStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#divideGivingPhrase.
    def enterDivideGivingPhrase(self, ctx:CobolParser.DivideGivingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#divideGivingPhrase.
    def exitDivideGivingPhrase(self, ctx:CobolParser.DivideGivingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#divideInto.
    def enterDivideInto(self, ctx:CobolParser.DivideIntoContext):
        pass

    # Exit a parse tree produced by CobolParser#divideInto.
    def exitDivideInto(self, ctx:CobolParser.DivideIntoContext):
        pass


    # Enter a parse tree produced by CobolParser#divideGiving.
    def enterDivideGiving(self, ctx:CobolParser.DivideGivingContext):
        pass

    # Exit a parse tree produced by CobolParser#divideGiving.
    def exitDivideGiving(self, ctx:CobolParser.DivideGivingContext):
        pass


    # Enter a parse tree produced by CobolParser#divideRemainder.
    def enterDivideRemainder(self, ctx:CobolParser.DivideRemainderContext):
        pass

    # Exit a parse tree produced by CobolParser#divideRemainder.
    def exitDivideRemainder(self, ctx:CobolParser.DivideRemainderContext):
        pass


    # Enter a parse tree produced by CobolParser#enableStatement.
    def enterEnableStatement(self, ctx:CobolParser.EnableStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#enableStatement.
    def exitEnableStatement(self, ctx:CobolParser.EnableStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#entryStatement.
    def enterEntryStatement(self, ctx:CobolParser.EntryStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#entryStatement.
    def exitEntryStatement(self, ctx:CobolParser.EntryStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateStatement.
    def enterEvaluateStatement(self, ctx:CobolParser.EvaluateStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateStatement.
    def exitEvaluateStatement(self, ctx:CobolParser.EvaluateStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateSelect.
    def enterEvaluateSelect(self, ctx:CobolParser.EvaluateSelectContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateSelect.
    def exitEvaluateSelect(self, ctx:CobolParser.EvaluateSelectContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateAlsoSelect.
    def enterEvaluateAlsoSelect(self, ctx:CobolParser.EvaluateAlsoSelectContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateAlsoSelect.
    def exitEvaluateAlsoSelect(self, ctx:CobolParser.EvaluateAlsoSelectContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateWhenPhrase.
    def enterEvaluateWhenPhrase(self, ctx:CobolParser.EvaluateWhenPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateWhenPhrase.
    def exitEvaluateWhenPhrase(self, ctx:CobolParser.EvaluateWhenPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateWhen.
    def enterEvaluateWhen(self, ctx:CobolParser.EvaluateWhenContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateWhen.
    def exitEvaluateWhen(self, ctx:CobolParser.EvaluateWhenContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateCondition.
    def enterEvaluateCondition(self, ctx:CobolParser.EvaluateConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateCondition.
    def exitEvaluateCondition(self, ctx:CobolParser.EvaluateConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateThrough.
    def enterEvaluateThrough(self, ctx:CobolParser.EvaluateThroughContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateThrough.
    def exitEvaluateThrough(self, ctx:CobolParser.EvaluateThroughContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateAlsoCondition.
    def enterEvaluateAlsoCondition(self, ctx:CobolParser.EvaluateAlsoConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateAlsoCondition.
    def exitEvaluateAlsoCondition(self, ctx:CobolParser.EvaluateAlsoConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateWhenOther.
    def enterEvaluateWhenOther(self, ctx:CobolParser.EvaluateWhenOtherContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateWhenOther.
    def exitEvaluateWhenOther(self, ctx:CobolParser.EvaluateWhenOtherContext):
        pass


    # Enter a parse tree produced by CobolParser#evaluateValue.
    def enterEvaluateValue(self, ctx:CobolParser.EvaluateValueContext):
        pass

    # Exit a parse tree produced by CobolParser#evaluateValue.
    def exitEvaluateValue(self, ctx:CobolParser.EvaluateValueContext):
        pass


    # Enter a parse tree produced by CobolParser#execCicsStatement.
    def enterExecCicsStatement(self, ctx:CobolParser.ExecCicsStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#execCicsStatement.
    def exitExecCicsStatement(self, ctx:CobolParser.ExecCicsStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#execSqlStatement.
    def enterExecSqlStatement(self, ctx:CobolParser.ExecSqlStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#execSqlStatement.
    def exitExecSqlStatement(self, ctx:CobolParser.ExecSqlStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#execSqlImsStatement.
    def enterExecSqlImsStatement(self, ctx:CobolParser.ExecSqlImsStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#execSqlImsStatement.
    def exitExecSqlImsStatement(self, ctx:CobolParser.ExecSqlImsStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#exhibitStatement.
    def enterExhibitStatement(self, ctx:CobolParser.ExhibitStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#exhibitStatement.
    def exitExhibitStatement(self, ctx:CobolParser.ExhibitStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#exhibitOperand.
    def enterExhibitOperand(self, ctx:CobolParser.ExhibitOperandContext):
        pass

    # Exit a parse tree produced by CobolParser#exhibitOperand.
    def exitExhibitOperand(self, ctx:CobolParser.ExhibitOperandContext):
        pass


    # Enter a parse tree produced by CobolParser#exitStatement.
    def enterExitStatement(self, ctx:CobolParser.ExitStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#exitStatement.
    def exitExitStatement(self, ctx:CobolParser.ExitStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#generateStatement.
    def enterGenerateStatement(self, ctx:CobolParser.GenerateStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#generateStatement.
    def exitGenerateStatement(self, ctx:CobolParser.GenerateStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#gobackStatement.
    def enterGobackStatement(self, ctx:CobolParser.GobackStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#gobackStatement.
    def exitGobackStatement(self, ctx:CobolParser.GobackStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#goToStatement.
    def enterGoToStatement(self, ctx:CobolParser.GoToStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#goToStatement.
    def exitGoToStatement(self, ctx:CobolParser.GoToStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#goToStatementSimple.
    def enterGoToStatementSimple(self, ctx:CobolParser.GoToStatementSimpleContext):
        pass

    # Exit a parse tree produced by CobolParser#goToStatementSimple.
    def exitGoToStatementSimple(self, ctx:CobolParser.GoToStatementSimpleContext):
        pass


    # Enter a parse tree produced by CobolParser#goToDependingOnStatement.
    def enterGoToDependingOnStatement(self, ctx:CobolParser.GoToDependingOnStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#goToDependingOnStatement.
    def exitGoToDependingOnStatement(self, ctx:CobolParser.GoToDependingOnStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#ifStatement.
    def enterIfStatement(self, ctx:CobolParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#ifStatement.
    def exitIfStatement(self, ctx:CobolParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#ifThen.
    def enterIfThen(self, ctx:CobolParser.IfThenContext):
        pass

    # Exit a parse tree produced by CobolParser#ifThen.
    def exitIfThen(self, ctx:CobolParser.IfThenContext):
        pass


    # Enter a parse tree produced by CobolParser#ifElse.
    def enterIfElse(self, ctx:CobolParser.IfElseContext):
        pass

    # Exit a parse tree produced by CobolParser#ifElse.
    def exitIfElse(self, ctx:CobolParser.IfElseContext):
        pass


    # Enter a parse tree produced by CobolParser#initializeStatement.
    def enterInitializeStatement(self, ctx:CobolParser.InitializeStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#initializeStatement.
    def exitInitializeStatement(self, ctx:CobolParser.InitializeStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#initializeReplacingPhrase.
    def enterInitializeReplacingPhrase(self, ctx:CobolParser.InitializeReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#initializeReplacingPhrase.
    def exitInitializeReplacingPhrase(self, ctx:CobolParser.InitializeReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#initializeReplacingBy.
    def enterInitializeReplacingBy(self, ctx:CobolParser.InitializeReplacingByContext):
        pass

    # Exit a parse tree produced by CobolParser#initializeReplacingBy.
    def exitInitializeReplacingBy(self, ctx:CobolParser.InitializeReplacingByContext):
        pass


    # Enter a parse tree produced by CobolParser#initiateStatement.
    def enterInitiateStatement(self, ctx:CobolParser.InitiateStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#initiateStatement.
    def exitInitiateStatement(self, ctx:CobolParser.InitiateStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectStatement.
    def enterInspectStatement(self, ctx:CobolParser.InspectStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectStatement.
    def exitInspectStatement(self, ctx:CobolParser.InspectStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectTallyingPhrase.
    def enterInspectTallyingPhrase(self, ctx:CobolParser.InspectTallyingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectTallyingPhrase.
    def exitInspectTallyingPhrase(self, ctx:CobolParser.InspectTallyingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectReplacingPhrase.
    def enterInspectReplacingPhrase(self, ctx:CobolParser.InspectReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectReplacingPhrase.
    def exitInspectReplacingPhrase(self, ctx:CobolParser.InspectReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectTallyingReplacingPhrase.
    def enterInspectTallyingReplacingPhrase(self, ctx:CobolParser.InspectTallyingReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectTallyingReplacingPhrase.
    def exitInspectTallyingReplacingPhrase(self, ctx:CobolParser.InspectTallyingReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectConvertingPhrase.
    def enterInspectConvertingPhrase(self, ctx:CobolParser.InspectConvertingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectConvertingPhrase.
    def exitInspectConvertingPhrase(self, ctx:CobolParser.InspectConvertingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectFor.
    def enterInspectFor(self, ctx:CobolParser.InspectForContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectFor.
    def exitInspectFor(self, ctx:CobolParser.InspectForContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectCharacters.
    def enterInspectCharacters(self, ctx:CobolParser.InspectCharactersContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectCharacters.
    def exitInspectCharacters(self, ctx:CobolParser.InspectCharactersContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectReplacingCharacters.
    def enterInspectReplacingCharacters(self, ctx:CobolParser.InspectReplacingCharactersContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectReplacingCharacters.
    def exitInspectReplacingCharacters(self, ctx:CobolParser.InspectReplacingCharactersContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectAllLeadings.
    def enterInspectAllLeadings(self, ctx:CobolParser.InspectAllLeadingsContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectAllLeadings.
    def exitInspectAllLeadings(self, ctx:CobolParser.InspectAllLeadingsContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectReplacingAllLeadings.
    def enterInspectReplacingAllLeadings(self, ctx:CobolParser.InspectReplacingAllLeadingsContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectReplacingAllLeadings.
    def exitInspectReplacingAllLeadings(self, ctx:CobolParser.InspectReplacingAllLeadingsContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectAllLeading.
    def enterInspectAllLeading(self, ctx:CobolParser.InspectAllLeadingContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectAllLeading.
    def exitInspectAllLeading(self, ctx:CobolParser.InspectAllLeadingContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectReplacingAllLeading.
    def enterInspectReplacingAllLeading(self, ctx:CobolParser.InspectReplacingAllLeadingContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectReplacingAllLeading.
    def exitInspectReplacingAllLeading(self, ctx:CobolParser.InspectReplacingAllLeadingContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectBy.
    def enterInspectBy(self, ctx:CobolParser.InspectByContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectBy.
    def exitInspectBy(self, ctx:CobolParser.InspectByContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectTo.
    def enterInspectTo(self, ctx:CobolParser.InspectToContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectTo.
    def exitInspectTo(self, ctx:CobolParser.InspectToContext):
        pass


    # Enter a parse tree produced by CobolParser#inspectBeforeAfter.
    def enterInspectBeforeAfter(self, ctx:CobolParser.InspectBeforeAfterContext):
        pass

    # Exit a parse tree produced by CobolParser#inspectBeforeAfter.
    def exitInspectBeforeAfter(self, ctx:CobolParser.InspectBeforeAfterContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeStatement.
    def enterMergeStatement(self, ctx:CobolParser.MergeStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeStatement.
    def exitMergeStatement(self, ctx:CobolParser.MergeStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeOnKeyClause.
    def enterMergeOnKeyClause(self, ctx:CobolParser.MergeOnKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeOnKeyClause.
    def exitMergeOnKeyClause(self, ctx:CobolParser.MergeOnKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeCollatingSequencePhrase.
    def enterMergeCollatingSequencePhrase(self, ctx:CobolParser.MergeCollatingSequencePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeCollatingSequencePhrase.
    def exitMergeCollatingSequencePhrase(self, ctx:CobolParser.MergeCollatingSequencePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeCollatingAlphanumeric.
    def enterMergeCollatingAlphanumeric(self, ctx:CobolParser.MergeCollatingAlphanumericContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeCollatingAlphanumeric.
    def exitMergeCollatingAlphanumeric(self, ctx:CobolParser.MergeCollatingAlphanumericContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeCollatingNational.
    def enterMergeCollatingNational(self, ctx:CobolParser.MergeCollatingNationalContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeCollatingNational.
    def exitMergeCollatingNational(self, ctx:CobolParser.MergeCollatingNationalContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeUsing.
    def enterMergeUsing(self, ctx:CobolParser.MergeUsingContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeUsing.
    def exitMergeUsing(self, ctx:CobolParser.MergeUsingContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeOutputProcedurePhrase.
    def enterMergeOutputProcedurePhrase(self, ctx:CobolParser.MergeOutputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeOutputProcedurePhrase.
    def exitMergeOutputProcedurePhrase(self, ctx:CobolParser.MergeOutputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeOutputThrough.
    def enterMergeOutputThrough(self, ctx:CobolParser.MergeOutputThroughContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeOutputThrough.
    def exitMergeOutputThrough(self, ctx:CobolParser.MergeOutputThroughContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeGivingPhrase.
    def enterMergeGivingPhrase(self, ctx:CobolParser.MergeGivingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeGivingPhrase.
    def exitMergeGivingPhrase(self, ctx:CobolParser.MergeGivingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#mergeGiving.
    def enterMergeGiving(self, ctx:CobolParser.MergeGivingContext):
        pass

    # Exit a parse tree produced by CobolParser#mergeGiving.
    def exitMergeGiving(self, ctx:CobolParser.MergeGivingContext):
        pass


    # Enter a parse tree produced by CobolParser#moveStatement.
    def enterMoveStatement(self, ctx:CobolParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#moveStatement.
    def exitMoveStatement(self, ctx:CobolParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#moveToStatement.
    def enterMoveToStatement(self, ctx:CobolParser.MoveToStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#moveToStatement.
    def exitMoveToStatement(self, ctx:CobolParser.MoveToStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#moveToSendingArea.
    def enterMoveToSendingArea(self, ctx:CobolParser.MoveToSendingAreaContext):
        pass

    # Exit a parse tree produced by CobolParser#moveToSendingArea.
    def exitMoveToSendingArea(self, ctx:CobolParser.MoveToSendingAreaContext):
        pass


    # Enter a parse tree produced by CobolParser#moveCorrespondingToStatement.
    def enterMoveCorrespondingToStatement(self, ctx:CobolParser.MoveCorrespondingToStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#moveCorrespondingToStatement.
    def exitMoveCorrespondingToStatement(self, ctx:CobolParser.MoveCorrespondingToStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#moveCorrespondingToSendingArea.
    def enterMoveCorrespondingToSendingArea(self, ctx:CobolParser.MoveCorrespondingToSendingAreaContext):
        pass

    # Exit a parse tree produced by CobolParser#moveCorrespondingToSendingArea.
    def exitMoveCorrespondingToSendingArea(self, ctx:CobolParser.MoveCorrespondingToSendingAreaContext):
        pass


    # Enter a parse tree produced by CobolParser#multiplyStatement.
    def enterMultiplyStatement(self, ctx:CobolParser.MultiplyStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#multiplyStatement.
    def exitMultiplyStatement(self, ctx:CobolParser.MultiplyStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#multiplyRegular.
    def enterMultiplyRegular(self, ctx:CobolParser.MultiplyRegularContext):
        pass

    # Exit a parse tree produced by CobolParser#multiplyRegular.
    def exitMultiplyRegular(self, ctx:CobolParser.MultiplyRegularContext):
        pass


    # Enter a parse tree produced by CobolParser#multiplyRegularOperand.
    def enterMultiplyRegularOperand(self, ctx:CobolParser.MultiplyRegularOperandContext):
        pass

    # Exit a parse tree produced by CobolParser#multiplyRegularOperand.
    def exitMultiplyRegularOperand(self, ctx:CobolParser.MultiplyRegularOperandContext):
        pass


    # Enter a parse tree produced by CobolParser#multiplyGiving.
    def enterMultiplyGiving(self, ctx:CobolParser.MultiplyGivingContext):
        pass

    # Exit a parse tree produced by CobolParser#multiplyGiving.
    def exitMultiplyGiving(self, ctx:CobolParser.MultiplyGivingContext):
        pass


    # Enter a parse tree produced by CobolParser#multiplyGivingOperand.
    def enterMultiplyGivingOperand(self, ctx:CobolParser.MultiplyGivingOperandContext):
        pass

    # Exit a parse tree produced by CobolParser#multiplyGivingOperand.
    def exitMultiplyGivingOperand(self, ctx:CobolParser.MultiplyGivingOperandContext):
        pass


    # Enter a parse tree produced by CobolParser#multiplyGivingResult.
    def enterMultiplyGivingResult(self, ctx:CobolParser.MultiplyGivingResultContext):
        pass

    # Exit a parse tree produced by CobolParser#multiplyGivingResult.
    def exitMultiplyGivingResult(self, ctx:CobolParser.MultiplyGivingResultContext):
        pass


    # Enter a parse tree produced by CobolParser#nextSentenceStatement.
    def enterNextSentenceStatement(self, ctx:CobolParser.NextSentenceStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#nextSentenceStatement.
    def exitNextSentenceStatement(self, ctx:CobolParser.NextSentenceStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#openStatement.
    def enterOpenStatement(self, ctx:CobolParser.OpenStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#openStatement.
    def exitOpenStatement(self, ctx:CobolParser.OpenStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#openInputStatement.
    def enterOpenInputStatement(self, ctx:CobolParser.OpenInputStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#openInputStatement.
    def exitOpenInputStatement(self, ctx:CobolParser.OpenInputStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#openInput.
    def enterOpenInput(self, ctx:CobolParser.OpenInputContext):
        pass

    # Exit a parse tree produced by CobolParser#openInput.
    def exitOpenInput(self, ctx:CobolParser.OpenInputContext):
        pass


    # Enter a parse tree produced by CobolParser#openOutputStatement.
    def enterOpenOutputStatement(self, ctx:CobolParser.OpenOutputStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#openOutputStatement.
    def exitOpenOutputStatement(self, ctx:CobolParser.OpenOutputStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#openOutput.
    def enterOpenOutput(self, ctx:CobolParser.OpenOutputContext):
        pass

    # Exit a parse tree produced by CobolParser#openOutput.
    def exitOpenOutput(self, ctx:CobolParser.OpenOutputContext):
        pass


    # Enter a parse tree produced by CobolParser#openIOStatement.
    def enterOpenIOStatement(self, ctx:CobolParser.OpenIOStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#openIOStatement.
    def exitOpenIOStatement(self, ctx:CobolParser.OpenIOStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#openExtendStatement.
    def enterOpenExtendStatement(self, ctx:CobolParser.OpenExtendStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#openExtendStatement.
    def exitOpenExtendStatement(self, ctx:CobolParser.OpenExtendStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#performStatement.
    def enterPerformStatement(self, ctx:CobolParser.PerformStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#performStatement.
    def exitPerformStatement(self, ctx:CobolParser.PerformStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#performInlineStatement.
    def enterPerformInlineStatement(self, ctx:CobolParser.PerformInlineStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#performInlineStatement.
    def exitPerformInlineStatement(self, ctx:CobolParser.PerformInlineStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#performProcedureStatement.
    def enterPerformProcedureStatement(self, ctx:CobolParser.PerformProcedureStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#performProcedureStatement.
    def exitPerformProcedureStatement(self, ctx:CobolParser.PerformProcedureStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#performType.
    def enterPerformType(self, ctx:CobolParser.PerformTypeContext):
        pass

    # Exit a parse tree produced by CobolParser#performType.
    def exitPerformType(self, ctx:CobolParser.PerformTypeContext):
        pass


    # Enter a parse tree produced by CobolParser#performTimes.
    def enterPerformTimes(self, ctx:CobolParser.PerformTimesContext):
        pass

    # Exit a parse tree produced by CobolParser#performTimes.
    def exitPerformTimes(self, ctx:CobolParser.PerformTimesContext):
        pass


    # Enter a parse tree produced by CobolParser#performUntil.
    def enterPerformUntil(self, ctx:CobolParser.PerformUntilContext):
        pass

    # Exit a parse tree produced by CobolParser#performUntil.
    def exitPerformUntil(self, ctx:CobolParser.PerformUntilContext):
        pass


    # Enter a parse tree produced by CobolParser#performVarying.
    def enterPerformVarying(self, ctx:CobolParser.PerformVaryingContext):
        pass

    # Exit a parse tree produced by CobolParser#performVarying.
    def exitPerformVarying(self, ctx:CobolParser.PerformVaryingContext):
        pass


    # Enter a parse tree produced by CobolParser#performVaryingClause.
    def enterPerformVaryingClause(self, ctx:CobolParser.PerformVaryingClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#performVaryingClause.
    def exitPerformVaryingClause(self, ctx:CobolParser.PerformVaryingClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#performVaryingPhrase.
    def enterPerformVaryingPhrase(self, ctx:CobolParser.PerformVaryingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#performVaryingPhrase.
    def exitPerformVaryingPhrase(self, ctx:CobolParser.PerformVaryingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#performAfter.
    def enterPerformAfter(self, ctx:CobolParser.PerformAfterContext):
        pass

    # Exit a parse tree produced by CobolParser#performAfter.
    def exitPerformAfter(self, ctx:CobolParser.PerformAfterContext):
        pass


    # Enter a parse tree produced by CobolParser#performFrom.
    def enterPerformFrom(self, ctx:CobolParser.PerformFromContext):
        pass

    # Exit a parse tree produced by CobolParser#performFrom.
    def exitPerformFrom(self, ctx:CobolParser.PerformFromContext):
        pass


    # Enter a parse tree produced by CobolParser#performBy.
    def enterPerformBy(self, ctx:CobolParser.PerformByContext):
        pass

    # Exit a parse tree produced by CobolParser#performBy.
    def exitPerformBy(self, ctx:CobolParser.PerformByContext):
        pass


    # Enter a parse tree produced by CobolParser#performTestClause.
    def enterPerformTestClause(self, ctx:CobolParser.PerformTestClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#performTestClause.
    def exitPerformTestClause(self, ctx:CobolParser.PerformTestClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#purgeStatement.
    def enterPurgeStatement(self, ctx:CobolParser.PurgeStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#purgeStatement.
    def exitPurgeStatement(self, ctx:CobolParser.PurgeStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#readStatement.
    def enterReadStatement(self, ctx:CobolParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#readStatement.
    def exitReadStatement(self, ctx:CobolParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#readInto.
    def enterReadInto(self, ctx:CobolParser.ReadIntoContext):
        pass

    # Exit a parse tree produced by CobolParser#readInto.
    def exitReadInto(self, ctx:CobolParser.ReadIntoContext):
        pass


    # Enter a parse tree produced by CobolParser#readWith.
    def enterReadWith(self, ctx:CobolParser.ReadWithContext):
        pass

    # Exit a parse tree produced by CobolParser#readWith.
    def exitReadWith(self, ctx:CobolParser.ReadWithContext):
        pass


    # Enter a parse tree produced by CobolParser#readKey.
    def enterReadKey(self, ctx:CobolParser.ReadKeyContext):
        pass

    # Exit a parse tree produced by CobolParser#readKey.
    def exitReadKey(self, ctx:CobolParser.ReadKeyContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveStatement.
    def enterReceiveStatement(self, ctx:CobolParser.ReceiveStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveStatement.
    def exitReceiveStatement(self, ctx:CobolParser.ReceiveStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveFromStatement.
    def enterReceiveFromStatement(self, ctx:CobolParser.ReceiveFromStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveFromStatement.
    def exitReceiveFromStatement(self, ctx:CobolParser.ReceiveFromStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveFrom.
    def enterReceiveFrom(self, ctx:CobolParser.ReceiveFromContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveFrom.
    def exitReceiveFrom(self, ctx:CobolParser.ReceiveFromContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveIntoStatement.
    def enterReceiveIntoStatement(self, ctx:CobolParser.ReceiveIntoStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveIntoStatement.
    def exitReceiveIntoStatement(self, ctx:CobolParser.ReceiveIntoStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveNoData.
    def enterReceiveNoData(self, ctx:CobolParser.ReceiveNoDataContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveNoData.
    def exitReceiveNoData(self, ctx:CobolParser.ReceiveNoDataContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveWithData.
    def enterReceiveWithData(self, ctx:CobolParser.ReceiveWithDataContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveWithData.
    def exitReceiveWithData(self, ctx:CobolParser.ReceiveWithDataContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveBefore.
    def enterReceiveBefore(self, ctx:CobolParser.ReceiveBeforeContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveBefore.
    def exitReceiveBefore(self, ctx:CobolParser.ReceiveBeforeContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveWith.
    def enterReceiveWith(self, ctx:CobolParser.ReceiveWithContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveWith.
    def exitReceiveWith(self, ctx:CobolParser.ReceiveWithContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveThread.
    def enterReceiveThread(self, ctx:CobolParser.ReceiveThreadContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveThread.
    def exitReceiveThread(self, ctx:CobolParser.ReceiveThreadContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveSize.
    def enterReceiveSize(self, ctx:CobolParser.ReceiveSizeContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveSize.
    def exitReceiveSize(self, ctx:CobolParser.ReceiveSizeContext):
        pass


    # Enter a parse tree produced by CobolParser#receiveStatus.
    def enterReceiveStatus(self, ctx:CobolParser.ReceiveStatusContext):
        pass

    # Exit a parse tree produced by CobolParser#receiveStatus.
    def exitReceiveStatus(self, ctx:CobolParser.ReceiveStatusContext):
        pass


    # Enter a parse tree produced by CobolParser#releaseStatement.
    def enterReleaseStatement(self, ctx:CobolParser.ReleaseStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#releaseStatement.
    def exitReleaseStatement(self, ctx:CobolParser.ReleaseStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#returnStatement.
    def enterReturnStatement(self, ctx:CobolParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#returnStatement.
    def exitReturnStatement(self, ctx:CobolParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#returnInto.
    def enterReturnInto(self, ctx:CobolParser.ReturnIntoContext):
        pass

    # Exit a parse tree produced by CobolParser#returnInto.
    def exitReturnInto(self, ctx:CobolParser.ReturnIntoContext):
        pass


    # Enter a parse tree produced by CobolParser#rewriteStatement.
    def enterRewriteStatement(self, ctx:CobolParser.RewriteStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#rewriteStatement.
    def exitRewriteStatement(self, ctx:CobolParser.RewriteStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#rewriteFrom.
    def enterRewriteFrom(self, ctx:CobolParser.RewriteFromContext):
        pass

    # Exit a parse tree produced by CobolParser#rewriteFrom.
    def exitRewriteFrom(self, ctx:CobolParser.RewriteFromContext):
        pass


    # Enter a parse tree produced by CobolParser#searchStatement.
    def enterSearchStatement(self, ctx:CobolParser.SearchStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#searchStatement.
    def exitSearchStatement(self, ctx:CobolParser.SearchStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#searchVarying.
    def enterSearchVarying(self, ctx:CobolParser.SearchVaryingContext):
        pass

    # Exit a parse tree produced by CobolParser#searchVarying.
    def exitSearchVarying(self, ctx:CobolParser.SearchVaryingContext):
        pass


    # Enter a parse tree produced by CobolParser#searchWhen.
    def enterSearchWhen(self, ctx:CobolParser.SearchWhenContext):
        pass

    # Exit a parse tree produced by CobolParser#searchWhen.
    def exitSearchWhen(self, ctx:CobolParser.SearchWhenContext):
        pass


    # Enter a parse tree produced by CobolParser#sendStatement.
    def enterSendStatement(self, ctx:CobolParser.SendStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#sendStatement.
    def exitSendStatement(self, ctx:CobolParser.SendStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#sendStatementSync.
    def enterSendStatementSync(self, ctx:CobolParser.SendStatementSyncContext):
        pass

    # Exit a parse tree produced by CobolParser#sendStatementSync.
    def exitSendStatementSync(self, ctx:CobolParser.SendStatementSyncContext):
        pass


    # Enter a parse tree produced by CobolParser#sendStatementAsync.
    def enterSendStatementAsync(self, ctx:CobolParser.SendStatementAsyncContext):
        pass

    # Exit a parse tree produced by CobolParser#sendStatementAsync.
    def exitSendStatementAsync(self, ctx:CobolParser.SendStatementAsyncContext):
        pass


    # Enter a parse tree produced by CobolParser#sendFromPhrase.
    def enterSendFromPhrase(self, ctx:CobolParser.SendFromPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#sendFromPhrase.
    def exitSendFromPhrase(self, ctx:CobolParser.SendFromPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#sendWithPhrase.
    def enterSendWithPhrase(self, ctx:CobolParser.SendWithPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#sendWithPhrase.
    def exitSendWithPhrase(self, ctx:CobolParser.SendWithPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#sendReplacingPhrase.
    def enterSendReplacingPhrase(self, ctx:CobolParser.SendReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#sendReplacingPhrase.
    def exitSendReplacingPhrase(self, ctx:CobolParser.SendReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#sendAdvancingPhrase.
    def enterSendAdvancingPhrase(self, ctx:CobolParser.SendAdvancingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#sendAdvancingPhrase.
    def exitSendAdvancingPhrase(self, ctx:CobolParser.SendAdvancingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#sendAdvancingPage.
    def enterSendAdvancingPage(self, ctx:CobolParser.SendAdvancingPageContext):
        pass

    # Exit a parse tree produced by CobolParser#sendAdvancingPage.
    def exitSendAdvancingPage(self, ctx:CobolParser.SendAdvancingPageContext):
        pass


    # Enter a parse tree produced by CobolParser#sendAdvancingLines.
    def enterSendAdvancingLines(self, ctx:CobolParser.SendAdvancingLinesContext):
        pass

    # Exit a parse tree produced by CobolParser#sendAdvancingLines.
    def exitSendAdvancingLines(self, ctx:CobolParser.SendAdvancingLinesContext):
        pass


    # Enter a parse tree produced by CobolParser#sendAdvancingMnemonic.
    def enterSendAdvancingMnemonic(self, ctx:CobolParser.SendAdvancingMnemonicContext):
        pass

    # Exit a parse tree produced by CobolParser#sendAdvancingMnemonic.
    def exitSendAdvancingMnemonic(self, ctx:CobolParser.SendAdvancingMnemonicContext):
        pass


    # Enter a parse tree produced by CobolParser#setStatement.
    def enterSetStatement(self, ctx:CobolParser.SetStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#setStatement.
    def exitSetStatement(self, ctx:CobolParser.SetStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#setToStatement.
    def enterSetToStatement(self, ctx:CobolParser.SetToStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#setToStatement.
    def exitSetToStatement(self, ctx:CobolParser.SetToStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#setUpDownByStatement.
    def enterSetUpDownByStatement(self, ctx:CobolParser.SetUpDownByStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#setUpDownByStatement.
    def exitSetUpDownByStatement(self, ctx:CobolParser.SetUpDownByStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#setTo.
    def enterSetTo(self, ctx:CobolParser.SetToContext):
        pass

    # Exit a parse tree produced by CobolParser#setTo.
    def exitSetTo(self, ctx:CobolParser.SetToContext):
        pass


    # Enter a parse tree produced by CobolParser#setToValue.
    def enterSetToValue(self, ctx:CobolParser.SetToValueContext):
        pass

    # Exit a parse tree produced by CobolParser#setToValue.
    def exitSetToValue(self, ctx:CobolParser.SetToValueContext):
        pass


    # Enter a parse tree produced by CobolParser#setByValue.
    def enterSetByValue(self, ctx:CobolParser.SetByValueContext):
        pass

    # Exit a parse tree produced by CobolParser#setByValue.
    def exitSetByValue(self, ctx:CobolParser.SetByValueContext):
        pass


    # Enter a parse tree produced by CobolParser#sortStatement.
    def enterSortStatement(self, ctx:CobolParser.SortStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#sortStatement.
    def exitSortStatement(self, ctx:CobolParser.SortStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#sortOnKeyClause.
    def enterSortOnKeyClause(self, ctx:CobolParser.SortOnKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#sortOnKeyClause.
    def exitSortOnKeyClause(self, ctx:CobolParser.SortOnKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#sortDuplicatesPhrase.
    def enterSortDuplicatesPhrase(self, ctx:CobolParser.SortDuplicatesPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#sortDuplicatesPhrase.
    def exitSortDuplicatesPhrase(self, ctx:CobolParser.SortDuplicatesPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#sortCollatingSequencePhrase.
    def enterSortCollatingSequencePhrase(self, ctx:CobolParser.SortCollatingSequencePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#sortCollatingSequencePhrase.
    def exitSortCollatingSequencePhrase(self, ctx:CobolParser.SortCollatingSequencePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#sortCollatingAlphanumeric.
    def enterSortCollatingAlphanumeric(self, ctx:CobolParser.SortCollatingAlphanumericContext):
        pass

    # Exit a parse tree produced by CobolParser#sortCollatingAlphanumeric.
    def exitSortCollatingAlphanumeric(self, ctx:CobolParser.SortCollatingAlphanumericContext):
        pass


    # Enter a parse tree produced by CobolParser#sortCollatingNational.
    def enterSortCollatingNational(self, ctx:CobolParser.SortCollatingNationalContext):
        pass

    # Exit a parse tree produced by CobolParser#sortCollatingNational.
    def exitSortCollatingNational(self, ctx:CobolParser.SortCollatingNationalContext):
        pass


    # Enter a parse tree produced by CobolParser#sortInputProcedurePhrase.
    def enterSortInputProcedurePhrase(self, ctx:CobolParser.SortInputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#sortInputProcedurePhrase.
    def exitSortInputProcedurePhrase(self, ctx:CobolParser.SortInputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#sortInputThrough.
    def enterSortInputThrough(self, ctx:CobolParser.SortInputThroughContext):
        pass

    # Exit a parse tree produced by CobolParser#sortInputThrough.
    def exitSortInputThrough(self, ctx:CobolParser.SortInputThroughContext):
        pass


    # Enter a parse tree produced by CobolParser#sortUsing.
    def enterSortUsing(self, ctx:CobolParser.SortUsingContext):
        pass

    # Exit a parse tree produced by CobolParser#sortUsing.
    def exitSortUsing(self, ctx:CobolParser.SortUsingContext):
        pass


    # Enter a parse tree produced by CobolParser#sortOutputProcedurePhrase.
    def enterSortOutputProcedurePhrase(self, ctx:CobolParser.SortOutputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#sortOutputProcedurePhrase.
    def exitSortOutputProcedurePhrase(self, ctx:CobolParser.SortOutputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#sortOutputThrough.
    def enterSortOutputThrough(self, ctx:CobolParser.SortOutputThroughContext):
        pass

    # Exit a parse tree produced by CobolParser#sortOutputThrough.
    def exitSortOutputThrough(self, ctx:CobolParser.SortOutputThroughContext):
        pass


    # Enter a parse tree produced by CobolParser#sortGivingPhrase.
    def enterSortGivingPhrase(self, ctx:CobolParser.SortGivingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#sortGivingPhrase.
    def exitSortGivingPhrase(self, ctx:CobolParser.SortGivingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#sortGiving.
    def enterSortGiving(self, ctx:CobolParser.SortGivingContext):
        pass

    # Exit a parse tree produced by CobolParser#sortGiving.
    def exitSortGiving(self, ctx:CobolParser.SortGivingContext):
        pass


    # Enter a parse tree produced by CobolParser#startStatement.
    def enterStartStatement(self, ctx:CobolParser.StartStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#startStatement.
    def exitStartStatement(self, ctx:CobolParser.StartStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#startKey.
    def enterStartKey(self, ctx:CobolParser.StartKeyContext):
        pass

    # Exit a parse tree produced by CobolParser#startKey.
    def exitStartKey(self, ctx:CobolParser.StartKeyContext):
        pass


    # Enter a parse tree produced by CobolParser#stopStatement.
    def enterStopStatement(self, ctx:CobolParser.StopStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#stopStatement.
    def exitStopStatement(self, ctx:CobolParser.StopStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#stopStatementGiving.
    def enterStopStatementGiving(self, ctx:CobolParser.StopStatementGivingContext):
        pass

    # Exit a parse tree produced by CobolParser#stopStatementGiving.
    def exitStopStatementGiving(self, ctx:CobolParser.StopStatementGivingContext):
        pass


    # Enter a parse tree produced by CobolParser#stringStatement.
    def enterStringStatement(self, ctx:CobolParser.StringStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#stringStatement.
    def exitStringStatement(self, ctx:CobolParser.StringStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#stringSendingPhrase.
    def enterStringSendingPhrase(self, ctx:CobolParser.StringSendingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#stringSendingPhrase.
    def exitStringSendingPhrase(self, ctx:CobolParser.StringSendingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#stringSending.
    def enterStringSending(self, ctx:CobolParser.StringSendingContext):
        pass

    # Exit a parse tree produced by CobolParser#stringSending.
    def exitStringSending(self, ctx:CobolParser.StringSendingContext):
        pass


    # Enter a parse tree produced by CobolParser#stringDelimitedByPhrase.
    def enterStringDelimitedByPhrase(self, ctx:CobolParser.StringDelimitedByPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#stringDelimitedByPhrase.
    def exitStringDelimitedByPhrase(self, ctx:CobolParser.StringDelimitedByPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#stringForPhrase.
    def enterStringForPhrase(self, ctx:CobolParser.StringForPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#stringForPhrase.
    def exitStringForPhrase(self, ctx:CobolParser.StringForPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#stringIntoPhrase.
    def enterStringIntoPhrase(self, ctx:CobolParser.StringIntoPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#stringIntoPhrase.
    def exitStringIntoPhrase(self, ctx:CobolParser.StringIntoPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#stringWithPointerPhrase.
    def enterStringWithPointerPhrase(self, ctx:CobolParser.StringWithPointerPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#stringWithPointerPhrase.
    def exitStringWithPointerPhrase(self, ctx:CobolParser.StringWithPointerPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractStatement.
    def enterSubtractStatement(self, ctx:CobolParser.SubtractStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractStatement.
    def exitSubtractStatement(self, ctx:CobolParser.SubtractStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractFromStatement.
    def enterSubtractFromStatement(self, ctx:CobolParser.SubtractFromStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractFromStatement.
    def exitSubtractFromStatement(self, ctx:CobolParser.SubtractFromStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractFromGivingStatement.
    def enterSubtractFromGivingStatement(self, ctx:CobolParser.SubtractFromGivingStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractFromGivingStatement.
    def exitSubtractFromGivingStatement(self, ctx:CobolParser.SubtractFromGivingStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractCorrespondingStatement.
    def enterSubtractCorrespondingStatement(self, ctx:CobolParser.SubtractCorrespondingStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractCorrespondingStatement.
    def exitSubtractCorrespondingStatement(self, ctx:CobolParser.SubtractCorrespondingStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractSubtrahend.
    def enterSubtractSubtrahend(self, ctx:CobolParser.SubtractSubtrahendContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractSubtrahend.
    def exitSubtractSubtrahend(self, ctx:CobolParser.SubtractSubtrahendContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractMinuend.
    def enterSubtractMinuend(self, ctx:CobolParser.SubtractMinuendContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractMinuend.
    def exitSubtractMinuend(self, ctx:CobolParser.SubtractMinuendContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractMinuendGiving.
    def enterSubtractMinuendGiving(self, ctx:CobolParser.SubtractMinuendGivingContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractMinuendGiving.
    def exitSubtractMinuendGiving(self, ctx:CobolParser.SubtractMinuendGivingContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractGiving.
    def enterSubtractGiving(self, ctx:CobolParser.SubtractGivingContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractGiving.
    def exitSubtractGiving(self, ctx:CobolParser.SubtractGivingContext):
        pass


    # Enter a parse tree produced by CobolParser#subtractMinuendCorresponding.
    def enterSubtractMinuendCorresponding(self, ctx:CobolParser.SubtractMinuendCorrespondingContext):
        pass

    # Exit a parse tree produced by CobolParser#subtractMinuendCorresponding.
    def exitSubtractMinuendCorresponding(self, ctx:CobolParser.SubtractMinuendCorrespondingContext):
        pass


    # Enter a parse tree produced by CobolParser#terminateStatement.
    def enterTerminateStatement(self, ctx:CobolParser.TerminateStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#terminateStatement.
    def exitTerminateStatement(self, ctx:CobolParser.TerminateStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringStatement.
    def enterUnstringStatement(self, ctx:CobolParser.UnstringStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringStatement.
    def exitUnstringStatement(self, ctx:CobolParser.UnstringStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringSendingPhrase.
    def enterUnstringSendingPhrase(self, ctx:CobolParser.UnstringSendingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringSendingPhrase.
    def exitUnstringSendingPhrase(self, ctx:CobolParser.UnstringSendingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringDelimitedByPhrase.
    def enterUnstringDelimitedByPhrase(self, ctx:CobolParser.UnstringDelimitedByPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringDelimitedByPhrase.
    def exitUnstringDelimitedByPhrase(self, ctx:CobolParser.UnstringDelimitedByPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringOrAllPhrase.
    def enterUnstringOrAllPhrase(self, ctx:CobolParser.UnstringOrAllPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringOrAllPhrase.
    def exitUnstringOrAllPhrase(self, ctx:CobolParser.UnstringOrAllPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringIntoPhrase.
    def enterUnstringIntoPhrase(self, ctx:CobolParser.UnstringIntoPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringIntoPhrase.
    def exitUnstringIntoPhrase(self, ctx:CobolParser.UnstringIntoPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringInto.
    def enterUnstringInto(self, ctx:CobolParser.UnstringIntoContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringInto.
    def exitUnstringInto(self, ctx:CobolParser.UnstringIntoContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringDelimiterIn.
    def enterUnstringDelimiterIn(self, ctx:CobolParser.UnstringDelimiterInContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringDelimiterIn.
    def exitUnstringDelimiterIn(self, ctx:CobolParser.UnstringDelimiterInContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringCountIn.
    def enterUnstringCountIn(self, ctx:CobolParser.UnstringCountInContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringCountIn.
    def exitUnstringCountIn(self, ctx:CobolParser.UnstringCountInContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringWithPointerPhrase.
    def enterUnstringWithPointerPhrase(self, ctx:CobolParser.UnstringWithPointerPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringWithPointerPhrase.
    def exitUnstringWithPointerPhrase(self, ctx:CobolParser.UnstringWithPointerPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#unstringTallyingPhrase.
    def enterUnstringTallyingPhrase(self, ctx:CobolParser.UnstringTallyingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#unstringTallyingPhrase.
    def exitUnstringTallyingPhrase(self, ctx:CobolParser.UnstringTallyingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#useStatement.
    def enterUseStatement(self, ctx:CobolParser.UseStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#useStatement.
    def exitUseStatement(self, ctx:CobolParser.UseStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#useAfterClause.
    def enterUseAfterClause(self, ctx:CobolParser.UseAfterClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#useAfterClause.
    def exitUseAfterClause(self, ctx:CobolParser.UseAfterClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#useAfterOn.
    def enterUseAfterOn(self, ctx:CobolParser.UseAfterOnContext):
        pass

    # Exit a parse tree produced by CobolParser#useAfterOn.
    def exitUseAfterOn(self, ctx:CobolParser.UseAfterOnContext):
        pass


    # Enter a parse tree produced by CobolParser#useDebugClause.
    def enterUseDebugClause(self, ctx:CobolParser.UseDebugClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#useDebugClause.
    def exitUseDebugClause(self, ctx:CobolParser.UseDebugClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#useDebugOn.
    def enterUseDebugOn(self, ctx:CobolParser.UseDebugOnContext):
        pass

    # Exit a parse tree produced by CobolParser#useDebugOn.
    def exitUseDebugOn(self, ctx:CobolParser.UseDebugOnContext):
        pass


    # Enter a parse tree produced by CobolParser#writeStatement.
    def enterWriteStatement(self, ctx:CobolParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by CobolParser#writeStatement.
    def exitWriteStatement(self, ctx:CobolParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by CobolParser#writeFromPhrase.
    def enterWriteFromPhrase(self, ctx:CobolParser.WriteFromPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#writeFromPhrase.
    def exitWriteFromPhrase(self, ctx:CobolParser.WriteFromPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#writeAdvancingPhrase.
    def enterWriteAdvancingPhrase(self, ctx:CobolParser.WriteAdvancingPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#writeAdvancingPhrase.
    def exitWriteAdvancingPhrase(self, ctx:CobolParser.WriteAdvancingPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#writeAdvancingPage.
    def enterWriteAdvancingPage(self, ctx:CobolParser.WriteAdvancingPageContext):
        pass

    # Exit a parse tree produced by CobolParser#writeAdvancingPage.
    def exitWriteAdvancingPage(self, ctx:CobolParser.WriteAdvancingPageContext):
        pass


    # Enter a parse tree produced by CobolParser#writeAdvancingLines.
    def enterWriteAdvancingLines(self, ctx:CobolParser.WriteAdvancingLinesContext):
        pass

    # Exit a parse tree produced by CobolParser#writeAdvancingLines.
    def exitWriteAdvancingLines(self, ctx:CobolParser.WriteAdvancingLinesContext):
        pass


    # Enter a parse tree produced by CobolParser#writeAdvancingMnemonic.
    def enterWriteAdvancingMnemonic(self, ctx:CobolParser.WriteAdvancingMnemonicContext):
        pass

    # Exit a parse tree produced by CobolParser#writeAdvancingMnemonic.
    def exitWriteAdvancingMnemonic(self, ctx:CobolParser.WriteAdvancingMnemonicContext):
        pass


    # Enter a parse tree produced by CobolParser#writeAtEndOfPagePhrase.
    def enterWriteAtEndOfPagePhrase(self, ctx:CobolParser.WriteAtEndOfPagePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#writeAtEndOfPagePhrase.
    def exitWriteAtEndOfPagePhrase(self, ctx:CobolParser.WriteAtEndOfPagePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#writeNotAtEndOfPagePhrase.
    def enterWriteNotAtEndOfPagePhrase(self, ctx:CobolParser.WriteNotAtEndOfPagePhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#writeNotAtEndOfPagePhrase.
    def exitWriteNotAtEndOfPagePhrase(self, ctx:CobolParser.WriteNotAtEndOfPagePhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#atEndPhrase.
    def enterAtEndPhrase(self, ctx:CobolParser.AtEndPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#atEndPhrase.
    def exitAtEndPhrase(self, ctx:CobolParser.AtEndPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#notAtEndPhrase.
    def enterNotAtEndPhrase(self, ctx:CobolParser.NotAtEndPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#notAtEndPhrase.
    def exitNotAtEndPhrase(self, ctx:CobolParser.NotAtEndPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#invalidKeyPhrase.
    def enterInvalidKeyPhrase(self, ctx:CobolParser.InvalidKeyPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#invalidKeyPhrase.
    def exitInvalidKeyPhrase(self, ctx:CobolParser.InvalidKeyPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#notInvalidKeyPhrase.
    def enterNotInvalidKeyPhrase(self, ctx:CobolParser.NotInvalidKeyPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#notInvalidKeyPhrase.
    def exitNotInvalidKeyPhrase(self, ctx:CobolParser.NotInvalidKeyPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#onOverflowPhrase.
    def enterOnOverflowPhrase(self, ctx:CobolParser.OnOverflowPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#onOverflowPhrase.
    def exitOnOverflowPhrase(self, ctx:CobolParser.OnOverflowPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#notOnOverflowPhrase.
    def enterNotOnOverflowPhrase(self, ctx:CobolParser.NotOnOverflowPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#notOnOverflowPhrase.
    def exitNotOnOverflowPhrase(self, ctx:CobolParser.NotOnOverflowPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#onSizeErrorPhrase.
    def enterOnSizeErrorPhrase(self, ctx:CobolParser.OnSizeErrorPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#onSizeErrorPhrase.
    def exitOnSizeErrorPhrase(self, ctx:CobolParser.OnSizeErrorPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#notOnSizeErrorPhrase.
    def enterNotOnSizeErrorPhrase(self, ctx:CobolParser.NotOnSizeErrorPhraseContext):
        pass

    # Exit a parse tree produced by CobolParser#notOnSizeErrorPhrase.
    def exitNotOnSizeErrorPhrase(self, ctx:CobolParser.NotOnSizeErrorPhraseContext):
        pass


    # Enter a parse tree produced by CobolParser#onExceptionClause.
    def enterOnExceptionClause(self, ctx:CobolParser.OnExceptionClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#onExceptionClause.
    def exitOnExceptionClause(self, ctx:CobolParser.OnExceptionClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#notOnExceptionClause.
    def enterNotOnExceptionClause(self, ctx:CobolParser.NotOnExceptionClauseContext):
        pass

    # Exit a parse tree produced by CobolParser#notOnExceptionClause.
    def exitNotOnExceptionClause(self, ctx:CobolParser.NotOnExceptionClauseContext):
        pass


    # Enter a parse tree produced by CobolParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:CobolParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by CobolParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:CobolParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by CobolParser#plusMinus.
    def enterPlusMinus(self, ctx:CobolParser.PlusMinusContext):
        pass

    # Exit a parse tree produced by CobolParser#plusMinus.
    def exitPlusMinus(self, ctx:CobolParser.PlusMinusContext):
        pass


    # Enter a parse tree produced by CobolParser#multDivs.
    def enterMultDivs(self, ctx:CobolParser.MultDivsContext):
        pass

    # Exit a parse tree produced by CobolParser#multDivs.
    def exitMultDivs(self, ctx:CobolParser.MultDivsContext):
        pass


    # Enter a parse tree produced by CobolParser#multDiv.
    def enterMultDiv(self, ctx:CobolParser.MultDivContext):
        pass

    # Exit a parse tree produced by CobolParser#multDiv.
    def exitMultDiv(self, ctx:CobolParser.MultDivContext):
        pass


    # Enter a parse tree produced by CobolParser#powers.
    def enterPowers(self, ctx:CobolParser.PowersContext):
        pass

    # Exit a parse tree produced by CobolParser#powers.
    def exitPowers(self, ctx:CobolParser.PowersContext):
        pass


    # Enter a parse tree produced by CobolParser#power.
    def enterPower(self, ctx:CobolParser.PowerContext):
        pass

    # Exit a parse tree produced by CobolParser#power.
    def exitPower(self, ctx:CobolParser.PowerContext):
        pass


    # Enter a parse tree produced by CobolParser#basis.
    def enterBasis(self, ctx:CobolParser.BasisContext):
        pass

    # Exit a parse tree produced by CobolParser#basis.
    def exitBasis(self, ctx:CobolParser.BasisContext):
        pass


    # Enter a parse tree produced by CobolParser#condition.
    def enterCondition(self, ctx:CobolParser.ConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#condition.
    def exitCondition(self, ctx:CobolParser.ConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#andOrCondition.
    def enterAndOrCondition(self, ctx:CobolParser.AndOrConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#andOrCondition.
    def exitAndOrCondition(self, ctx:CobolParser.AndOrConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#combinableCondition.
    def enterCombinableCondition(self, ctx:CobolParser.CombinableConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#combinableCondition.
    def exitCombinableCondition(self, ctx:CobolParser.CombinableConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#simpleCondition.
    def enterSimpleCondition(self, ctx:CobolParser.SimpleConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#simpleCondition.
    def exitSimpleCondition(self, ctx:CobolParser.SimpleConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#classCondition.
    def enterClassCondition(self, ctx:CobolParser.ClassConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#classCondition.
    def exitClassCondition(self, ctx:CobolParser.ClassConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#conditionNameReference.
    def enterConditionNameReference(self, ctx:CobolParser.ConditionNameReferenceContext):
        pass

    # Exit a parse tree produced by CobolParser#conditionNameReference.
    def exitConditionNameReference(self, ctx:CobolParser.ConditionNameReferenceContext):
        pass


    # Enter a parse tree produced by CobolParser#conditionNameSubscriptReference.
    def enterConditionNameSubscriptReference(self, ctx:CobolParser.ConditionNameSubscriptReferenceContext):
        pass

    # Exit a parse tree produced by CobolParser#conditionNameSubscriptReference.
    def exitConditionNameSubscriptReference(self, ctx:CobolParser.ConditionNameSubscriptReferenceContext):
        pass


    # Enter a parse tree produced by CobolParser#relationCondition.
    def enterRelationCondition(self, ctx:CobolParser.RelationConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#relationCondition.
    def exitRelationCondition(self, ctx:CobolParser.RelationConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#relationSignCondition.
    def enterRelationSignCondition(self, ctx:CobolParser.RelationSignConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#relationSignCondition.
    def exitRelationSignCondition(self, ctx:CobolParser.RelationSignConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#relationArithmeticComparison.
    def enterRelationArithmeticComparison(self, ctx:CobolParser.RelationArithmeticComparisonContext):
        pass

    # Exit a parse tree produced by CobolParser#relationArithmeticComparison.
    def exitRelationArithmeticComparison(self, ctx:CobolParser.RelationArithmeticComparisonContext):
        pass


    # Enter a parse tree produced by CobolParser#relationCombinedComparison.
    def enterRelationCombinedComparison(self, ctx:CobolParser.RelationCombinedComparisonContext):
        pass

    # Exit a parse tree produced by CobolParser#relationCombinedComparison.
    def exitRelationCombinedComparison(self, ctx:CobolParser.RelationCombinedComparisonContext):
        pass


    # Enter a parse tree produced by CobolParser#relationCombinedCondition.
    def enterRelationCombinedCondition(self, ctx:CobolParser.RelationCombinedConditionContext):
        pass

    # Exit a parse tree produced by CobolParser#relationCombinedCondition.
    def exitRelationCombinedCondition(self, ctx:CobolParser.RelationCombinedConditionContext):
        pass


    # Enter a parse tree produced by CobolParser#relationalOperator.
    def enterRelationalOperator(self, ctx:CobolParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by CobolParser#relationalOperator.
    def exitRelationalOperator(self, ctx:CobolParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by CobolParser#abbreviation.
    def enterAbbreviation(self, ctx:CobolParser.AbbreviationContext):
        pass

    # Exit a parse tree produced by CobolParser#abbreviation.
    def exitAbbreviation(self, ctx:CobolParser.AbbreviationContext):
        pass


    # Enter a parse tree produced by CobolParser#identifier.
    def enterIdentifier(self, ctx:CobolParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CobolParser#identifier.
    def exitIdentifier(self, ctx:CobolParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CobolParser#tableCall.
    def enterTableCall(self, ctx:CobolParser.TableCallContext):
        pass

    # Exit a parse tree produced by CobolParser#tableCall.
    def exitTableCall(self, ctx:CobolParser.TableCallContext):
        pass


    # Enter a parse tree produced by CobolParser#functionCall.
    def enterFunctionCall(self, ctx:CobolParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CobolParser#functionCall.
    def exitFunctionCall(self, ctx:CobolParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CobolParser#referenceModifier.
    def enterReferenceModifier(self, ctx:CobolParser.ReferenceModifierContext):
        pass

    # Exit a parse tree produced by CobolParser#referenceModifier.
    def exitReferenceModifier(self, ctx:CobolParser.ReferenceModifierContext):
        pass


    # Enter a parse tree produced by CobolParser#characterPosition.
    def enterCharacterPosition(self, ctx:CobolParser.CharacterPositionContext):
        pass

    # Exit a parse tree produced by CobolParser#characterPosition.
    def exitCharacterPosition(self, ctx:CobolParser.CharacterPositionContext):
        pass


    # Enter a parse tree produced by CobolParser#length.
    def enterLength(self, ctx:CobolParser.LengthContext):
        pass

    # Exit a parse tree produced by CobolParser#length.
    def exitLength(self, ctx:CobolParser.LengthContext):
        pass


    # Enter a parse tree produced by CobolParser#subscript.
    def enterSubscript(self, ctx:CobolParser.SubscriptContext):
        pass

    # Exit a parse tree produced by CobolParser#subscript.
    def exitSubscript(self, ctx:CobolParser.SubscriptContext):
        pass


    # Enter a parse tree produced by CobolParser#argument.
    def enterArgument(self, ctx:CobolParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CobolParser#argument.
    def exitArgument(self, ctx:CobolParser.ArgumentContext):
        pass


    # Enter a parse tree produced by CobolParser#qualifiedDataName.
    def enterQualifiedDataName(self, ctx:CobolParser.QualifiedDataNameContext):
        pass

    # Exit a parse tree produced by CobolParser#qualifiedDataName.
    def exitQualifiedDataName(self, ctx:CobolParser.QualifiedDataNameContext):
        pass


    # Enter a parse tree produced by CobolParser#qualifiedDataNameFormat1.
    def enterQualifiedDataNameFormat1(self, ctx:CobolParser.QualifiedDataNameFormat1Context):
        pass

    # Exit a parse tree produced by CobolParser#qualifiedDataNameFormat1.
    def exitQualifiedDataNameFormat1(self, ctx:CobolParser.QualifiedDataNameFormat1Context):
        pass


    # Enter a parse tree produced by CobolParser#qualifiedDataNameFormat2.
    def enterQualifiedDataNameFormat2(self, ctx:CobolParser.QualifiedDataNameFormat2Context):
        pass

    # Exit a parse tree produced by CobolParser#qualifiedDataNameFormat2.
    def exitQualifiedDataNameFormat2(self, ctx:CobolParser.QualifiedDataNameFormat2Context):
        pass


    # Enter a parse tree produced by CobolParser#qualifiedDataNameFormat3.
    def enterQualifiedDataNameFormat3(self, ctx:CobolParser.QualifiedDataNameFormat3Context):
        pass

    # Exit a parse tree produced by CobolParser#qualifiedDataNameFormat3.
    def exitQualifiedDataNameFormat3(self, ctx:CobolParser.QualifiedDataNameFormat3Context):
        pass


    # Enter a parse tree produced by CobolParser#qualifiedDataNameFormat4.
    def enterQualifiedDataNameFormat4(self, ctx:CobolParser.QualifiedDataNameFormat4Context):
        pass

    # Exit a parse tree produced by CobolParser#qualifiedDataNameFormat4.
    def exitQualifiedDataNameFormat4(self, ctx:CobolParser.QualifiedDataNameFormat4Context):
        pass


    # Enter a parse tree produced by CobolParser#qualifiedInData.
    def enterQualifiedInData(self, ctx:CobolParser.QualifiedInDataContext):
        pass

    # Exit a parse tree produced by CobolParser#qualifiedInData.
    def exitQualifiedInData(self, ctx:CobolParser.QualifiedInDataContext):
        pass


    # Enter a parse tree produced by CobolParser#inData.
    def enterInData(self, ctx:CobolParser.InDataContext):
        pass

    # Exit a parse tree produced by CobolParser#inData.
    def exitInData(self, ctx:CobolParser.InDataContext):
        pass


    # Enter a parse tree produced by CobolParser#inFile.
    def enterInFile(self, ctx:CobolParser.InFileContext):
        pass

    # Exit a parse tree produced by CobolParser#inFile.
    def exitInFile(self, ctx:CobolParser.InFileContext):
        pass


    # Enter a parse tree produced by CobolParser#inMnemonic.
    def enterInMnemonic(self, ctx:CobolParser.InMnemonicContext):
        pass

    # Exit a parse tree produced by CobolParser#inMnemonic.
    def exitInMnemonic(self, ctx:CobolParser.InMnemonicContext):
        pass


    # Enter a parse tree produced by CobolParser#inSection.
    def enterInSection(self, ctx:CobolParser.InSectionContext):
        pass

    # Exit a parse tree produced by CobolParser#inSection.
    def exitInSection(self, ctx:CobolParser.InSectionContext):
        pass


    # Enter a parse tree produced by CobolParser#inLibrary.
    def enterInLibrary(self, ctx:CobolParser.InLibraryContext):
        pass

    # Exit a parse tree produced by CobolParser#inLibrary.
    def exitInLibrary(self, ctx:CobolParser.InLibraryContext):
        pass


    # Enter a parse tree produced by CobolParser#inTable.
    def enterInTable(self, ctx:CobolParser.InTableContext):
        pass

    # Exit a parse tree produced by CobolParser#inTable.
    def exitInTable(self, ctx:CobolParser.InTableContext):
        pass


    # Enter a parse tree produced by CobolParser#alphabetName.
    def enterAlphabetName(self, ctx:CobolParser.AlphabetNameContext):
        pass

    # Exit a parse tree produced by CobolParser#alphabetName.
    def exitAlphabetName(self, ctx:CobolParser.AlphabetNameContext):
        pass


    # Enter a parse tree produced by CobolParser#assignmentName.
    def enterAssignmentName(self, ctx:CobolParser.AssignmentNameContext):
        pass

    # Exit a parse tree produced by CobolParser#assignmentName.
    def exitAssignmentName(self, ctx:CobolParser.AssignmentNameContext):
        pass


    # Enter a parse tree produced by CobolParser#basisName.
    def enterBasisName(self, ctx:CobolParser.BasisNameContext):
        pass

    # Exit a parse tree produced by CobolParser#basisName.
    def exitBasisName(self, ctx:CobolParser.BasisNameContext):
        pass


    # Enter a parse tree produced by CobolParser#cdName.
    def enterCdName(self, ctx:CobolParser.CdNameContext):
        pass

    # Exit a parse tree produced by CobolParser#cdName.
    def exitCdName(self, ctx:CobolParser.CdNameContext):
        pass


    # Enter a parse tree produced by CobolParser#className.
    def enterClassName(self, ctx:CobolParser.ClassNameContext):
        pass

    # Exit a parse tree produced by CobolParser#className.
    def exitClassName(self, ctx:CobolParser.ClassNameContext):
        pass


    # Enter a parse tree produced by CobolParser#computerName.
    def enterComputerName(self, ctx:CobolParser.ComputerNameContext):
        pass

    # Exit a parse tree produced by CobolParser#computerName.
    def exitComputerName(self, ctx:CobolParser.ComputerNameContext):
        pass


    # Enter a parse tree produced by CobolParser#conditionName.
    def enterConditionName(self, ctx:CobolParser.ConditionNameContext):
        pass

    # Exit a parse tree produced by CobolParser#conditionName.
    def exitConditionName(self, ctx:CobolParser.ConditionNameContext):
        pass


    # Enter a parse tree produced by CobolParser#dataName.
    def enterDataName(self, ctx:CobolParser.DataNameContext):
        pass

    # Exit a parse tree produced by CobolParser#dataName.
    def exitDataName(self, ctx:CobolParser.DataNameContext):
        pass


    # Enter a parse tree produced by CobolParser#dataDescName.
    def enterDataDescName(self, ctx:CobolParser.DataDescNameContext):
        pass

    # Exit a parse tree produced by CobolParser#dataDescName.
    def exitDataDescName(self, ctx:CobolParser.DataDescNameContext):
        pass


    # Enter a parse tree produced by CobolParser#environmentName.
    def enterEnvironmentName(self, ctx:CobolParser.EnvironmentNameContext):
        pass

    # Exit a parse tree produced by CobolParser#environmentName.
    def exitEnvironmentName(self, ctx:CobolParser.EnvironmentNameContext):
        pass


    # Enter a parse tree produced by CobolParser#fileName.
    def enterFileName(self, ctx:CobolParser.FileNameContext):
        pass

    # Exit a parse tree produced by CobolParser#fileName.
    def exitFileName(self, ctx:CobolParser.FileNameContext):
        pass


    # Enter a parse tree produced by CobolParser#functionName.
    def enterFunctionName(self, ctx:CobolParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by CobolParser#functionName.
    def exitFunctionName(self, ctx:CobolParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by CobolParser#indexName.
    def enterIndexName(self, ctx:CobolParser.IndexNameContext):
        pass

    # Exit a parse tree produced by CobolParser#indexName.
    def exitIndexName(self, ctx:CobolParser.IndexNameContext):
        pass


    # Enter a parse tree produced by CobolParser#languageName.
    def enterLanguageName(self, ctx:CobolParser.LanguageNameContext):
        pass

    # Exit a parse tree produced by CobolParser#languageName.
    def exitLanguageName(self, ctx:CobolParser.LanguageNameContext):
        pass


    # Enter a parse tree produced by CobolParser#libraryName.
    def enterLibraryName(self, ctx:CobolParser.LibraryNameContext):
        pass

    # Exit a parse tree produced by CobolParser#libraryName.
    def exitLibraryName(self, ctx:CobolParser.LibraryNameContext):
        pass


    # Enter a parse tree produced by CobolParser#localName.
    def enterLocalName(self, ctx:CobolParser.LocalNameContext):
        pass

    # Exit a parse tree produced by CobolParser#localName.
    def exitLocalName(self, ctx:CobolParser.LocalNameContext):
        pass


    # Enter a parse tree produced by CobolParser#mnemonicName.
    def enterMnemonicName(self, ctx:CobolParser.MnemonicNameContext):
        pass

    # Exit a parse tree produced by CobolParser#mnemonicName.
    def exitMnemonicName(self, ctx:CobolParser.MnemonicNameContext):
        pass


    # Enter a parse tree produced by CobolParser#paragraphName.
    def enterParagraphName(self, ctx:CobolParser.ParagraphNameContext):
        pass

    # Exit a parse tree produced by CobolParser#paragraphName.
    def exitParagraphName(self, ctx:CobolParser.ParagraphNameContext):
        pass


    # Enter a parse tree produced by CobolParser#procedureName.
    def enterProcedureName(self, ctx:CobolParser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by CobolParser#procedureName.
    def exitProcedureName(self, ctx:CobolParser.ProcedureNameContext):
        pass


    # Enter a parse tree produced by CobolParser#programName.
    def enterProgramName(self, ctx:CobolParser.ProgramNameContext):
        pass

    # Exit a parse tree produced by CobolParser#programName.
    def exitProgramName(self, ctx:CobolParser.ProgramNameContext):
        pass


    # Enter a parse tree produced by CobolParser#recordName.
    def enterRecordName(self, ctx:CobolParser.RecordNameContext):
        pass

    # Exit a parse tree produced by CobolParser#recordName.
    def exitRecordName(self, ctx:CobolParser.RecordNameContext):
        pass


    # Enter a parse tree produced by CobolParser#reportName.
    def enterReportName(self, ctx:CobolParser.ReportNameContext):
        pass

    # Exit a parse tree produced by CobolParser#reportName.
    def exitReportName(self, ctx:CobolParser.ReportNameContext):
        pass


    # Enter a parse tree produced by CobolParser#routineName.
    def enterRoutineName(self, ctx:CobolParser.RoutineNameContext):
        pass

    # Exit a parse tree produced by CobolParser#routineName.
    def exitRoutineName(self, ctx:CobolParser.RoutineNameContext):
        pass


    # Enter a parse tree produced by CobolParser#screenName.
    def enterScreenName(self, ctx:CobolParser.ScreenNameContext):
        pass

    # Exit a parse tree produced by CobolParser#screenName.
    def exitScreenName(self, ctx:CobolParser.ScreenNameContext):
        pass


    # Enter a parse tree produced by CobolParser#sectionName.
    def enterSectionName(self, ctx:CobolParser.SectionNameContext):
        pass

    # Exit a parse tree produced by CobolParser#sectionName.
    def exitSectionName(self, ctx:CobolParser.SectionNameContext):
        pass


    # Enter a parse tree produced by CobolParser#systemName.
    def enterSystemName(self, ctx:CobolParser.SystemNameContext):
        pass

    # Exit a parse tree produced by CobolParser#systemName.
    def exitSystemName(self, ctx:CobolParser.SystemNameContext):
        pass


    # Enter a parse tree produced by CobolParser#symbolicCharacter.
    def enterSymbolicCharacter(self, ctx:CobolParser.SymbolicCharacterContext):
        pass

    # Exit a parse tree produced by CobolParser#symbolicCharacter.
    def exitSymbolicCharacter(self, ctx:CobolParser.SymbolicCharacterContext):
        pass


    # Enter a parse tree produced by CobolParser#textName.
    def enterTextName(self, ctx:CobolParser.TextNameContext):
        pass

    # Exit a parse tree produced by CobolParser#textName.
    def exitTextName(self, ctx:CobolParser.TextNameContext):
        pass


    # Enter a parse tree produced by CobolParser#cobolWord.
    def enterCobolWord(self, ctx:CobolParser.CobolWordContext):
        pass

    # Exit a parse tree produced by CobolParser#cobolWord.
    def exitCobolWord(self, ctx:CobolParser.CobolWordContext):
        pass


    # Enter a parse tree produced by CobolParser#literal.
    def enterLiteral(self, ctx:CobolParser.LiteralContext):
        pass

    # Exit a parse tree produced by CobolParser#literal.
    def exitLiteral(self, ctx:CobolParser.LiteralContext):
        pass


    # Enter a parse tree produced by CobolParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:CobolParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by CobolParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:CobolParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by CobolParser#numericLiteral.
    def enterNumericLiteral(self, ctx:CobolParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by CobolParser#numericLiteral.
    def exitNumericLiteral(self, ctx:CobolParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by CobolParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:CobolParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by CobolParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:CobolParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by CobolParser#cicsDfhRespLiteral.
    def enterCicsDfhRespLiteral(self, ctx:CobolParser.CicsDfhRespLiteralContext):
        pass

    # Exit a parse tree produced by CobolParser#cicsDfhRespLiteral.
    def exitCicsDfhRespLiteral(self, ctx:CobolParser.CicsDfhRespLiteralContext):
        pass


    # Enter a parse tree produced by CobolParser#cicsDfhValueLiteral.
    def enterCicsDfhValueLiteral(self, ctx:CobolParser.CicsDfhValueLiteralContext):
        pass

    # Exit a parse tree produced by CobolParser#cicsDfhValueLiteral.
    def exitCicsDfhValueLiteral(self, ctx:CobolParser.CicsDfhValueLiteralContext):
        pass


    # Enter a parse tree produced by CobolParser#figurativeConstant.
    def enterFigurativeConstant(self, ctx:CobolParser.FigurativeConstantContext):
        pass

    # Exit a parse tree produced by CobolParser#figurativeConstant.
    def exitFigurativeConstant(self, ctx:CobolParser.FigurativeConstantContext):
        pass


    # Enter a parse tree produced by CobolParser#specialRegister.
    def enterSpecialRegister(self, ctx:CobolParser.SpecialRegisterContext):
        pass

    # Exit a parse tree produced by CobolParser#specialRegister.
    def exitSpecialRegister(self, ctx:CobolParser.SpecialRegisterContext):
        pass


    # Enter a parse tree produced by CobolParser#commentEntry.
    def enterCommentEntry(self, ctx:CobolParser.CommentEntryContext):
        pass

    # Exit a parse tree produced by CobolParser#commentEntry.
    def exitCommentEntry(self, ctx:CobolParser.CommentEntryContext):
        pass



del CobolParser