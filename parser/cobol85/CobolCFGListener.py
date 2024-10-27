# Generated from parser/cobol85/Cobol85.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Cobol85Parser import Cobol85Parser
else:
    from Cobol85Parser import Cobol85Parser

# This class defines a complete listener for a parse tree produced by Cobol85Parser.
class CobolCFGListener(ParseTreeListener):

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.business_rules = {}
        self.id = 0
        self.func_of_cxt = {"DisplayStatementContext":self.extractDisplayStatement}

    def find_parent(self, current_ctx, target_ctx):
        """
        Utility function to recursively find specific type of parent context.
        """
        p = current_ctx.parentCtx
        if p is None:
            return None
        if isinstance(p,target_ctx):
            return p
        else:
            return self.find_parent(p, target_ctx)

    def find_child(self, ctx: ParserRuleContext, target_context_type: type) -> ParserRuleContext:
        """
        Utility function to recursively find the first child node of a given context type.
    
        :param ctx: The current parse tree node (context).
        :param target_context_type: The type of the target context to find.
        :return: The first child node of the target context type, or None if not found.
        """
        # Base case: if the current context is of the target type, return it
        if isinstance(ctx, target_context_type):
            return ctx
    
        # Recursively search in the children
        for child in ctx.children:
            if isinstance(child, ParserRuleContext):
                result = self.find_child(child, target_context_type)
                if result is not None:
                    return result
    
        # If no matching child is found, return None
        return None

    def get_all_tokens(self, context:ParserRuleContext):
        tokens = []
        
        # If the context has children, traverse each one
        if context.children:
            for child in context.children:
                # If child is a terminal node (i.e., a token), append its text
                if hasattr(child, 'getText'):
                    tokens.append(child.getText())
                # If child is a non-terminal node (a rule context), recurse on it
                if isinstance(child, ParserRuleContext):
                    tokens.extend(self.get_all_tokens(child))
        return tokens

    def add_end_node(self):
        self.id+=1
        node = {"id": str(self.id), "data": {"label": "stop"}}
        self.nodes.append(node)
        self.edges.append({"id": str(self.id), "source": str(self.id-1), "target": str(self.id), "label": "sequential next"})

    def extractDisplayStatement(self, ctx:Cobol85Parser.DisplayStatementContext):
        label = "DISPLAY"
        displayOperand = ctx.displayOperand()
        for do in displayOperand:
            label += " " + do.getText()
        return label

    def enterProcedureDivision(self, ctx:Cobol85Parser.ProcedureDivisionContext):
        self.id +=1
        # Start processing procedure division for control flow
        self.nodes.append({"id": str(self.id), "data": {"label": "start"}})

    def enterAcceptStatement(self, ctx:Cobol85Parser.AcceptStatementContext):
        self.id +=1
        node = {"id": str(self.id), "data": {"label": f"ACCEPT {ctx.identifier().getText()}\n"}}
        self.nodes.append(node)
        self.edges.append({"id": str(self.id), "source": str(self.id-1), "target": str(self.id), "label": "sequential next"})

    def enterDivideStatement(self, ctx:Cobol85Parser.DivideStatementContext):
        self.id +=1
        # Start custom label
        label = "DIVIDE"
        # check identifier
        identifier = ctx.identifier()
        if identifier:
            label += " " + identifier.getText()
        else:
            label += " " + ctx.literal().getText()
        # check divideByGivingStatement
        divideByGivingStatement = ctx.divideByGivingStatement()
        if divideByGivingStatement:
            label += " " + "BY"
            identifier = divideByGivingStatement.identifier()
            if identifier:
                label += " " + identifier.getText()
            else:
                label += " " + divideByGivingStatement.literal().getText()
        # divideRemainder
        divideRemainder = ctx.divideRemainder()
        if divideRemainder:
            label += " " + "REMINDER" + " " + divideRemainder.identifier().getText()
        label += "\n"
        # End custom label
        node = {"id": str(self.id), "data": {"label": label}}
        self.nodes.append(node)
        self.edges.append({"id": str(self.id), "source": str(self.id-1), "target": str(self.id), "label": "sequential next"})

    def enterIfStatement(self, ctx: Cobol85Parser.IfStatementContext):
        
        self.id +=1
        start_if_id = self.id
        end_ifthen_id = end_ifelse_id = None
        node = {"id": str(self.id), "data": {"label": f"IF {ctx.condition().getText()}\n"}}
        self.nodes.append(node)
        self.edges.append({"id": str(self.id), "source": str(self.id-1), "target": str(self.id), "label": "sequential next"})
        
        # ifThen
        ifThen = ctx.ifThen()
        if ifThen:
            # statement
            statement = ifThen.statement()
            if statement:
                for i,st in enumerate(statement):
                    if i == 0:
                        self.id +=1
                        node = {"id": str(self.id), "data": {"label": \
                                 f"{self.func_of_cxt[type(st.getChild(0)).__name__](st.getChild(0))}\n"}}
                        self.nodes.append(node)
                        self.edges.append({"id": str(self.id), "source": str(start_if_id), "target": str(self.id), "label": "true"})
                        end_ifthen_id = self.id
                    else:
                        self.id +=1
                        node = {"id": str(self.id), "data": {"label": \
                                 f"{self.func_of_cxt[type(st.getChild(0)).__name__](st.getChild(0))}\n"}}
                        self.nodes.append(node)
                        self.edges.append({"id": str(self.id), "source": str(self.id-1), "target": str(self.id), "label": "sequential next"})
                        end_ifthen_id = self.id
                        
        # ifElse
        ifElse = ctx.ifElse()
        if ifElse:
            # statement
            statement = ifElse.statement()
            if statement:
                for i,st in enumerate(statement):
                    if i == 0:
                        self.id +=1          
                        node = {"id": str(self.id), "data": {"label": \
                                 f"{self.func_of_cxt[type(st.getChild(0)).__name__](st.getChild(0))}\n"}}
                        self.nodes.append(node)
                        self.edges.append({"id": str(self.id), "source": str(start_if_id), "target": str(self.id), "label": "false"})
                        end_ifelse_id = self.id
                    else:
                        self.id +=1
                        node = {"id": str(self.id), "data": {"label": \
                                 f"{self.func_of_cxt[type(st.getChild(0)).__name__](st.getChild(0))}\n"}}
                        self.nodes.append(node)
                        self.edges.append({"id": str(self.id), "source": str(self.id-1), "target": str(self.id), "label": "sequential next"})
                        end_ifelse_id = self.id

        # Add end_if node
        if end_ifthen_id:
            self.id +=1
            node = {"id": str(self.id), "data": {"label": "End If"}}
            self.nodes.append(node)
            self.edges.append({"id": str(self.id), "source": str(end_ifthen_id), "target": str(self.id), "label": "sequential next"})
            if end_ifelse_id:
                self.edges.append({"id": str(self.id), "source": str(end_ifelse_id), "target": str(self.id), "label": "sequential next"})