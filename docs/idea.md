Using ANTLR with Python to parse COBOL files, define business rules, and create a control flow graph involves several steps. ANTLR can be used to generate the lexer and parser for COBOL code, and then a custom visitor pattern in Python can be used to interpret business rules and construct a control flow graph (CFG).

Here’s a general approach:

1. **Define a COBOL Grammar**: First, you'll need a grammar for COBOL, which can be found on [ANTLR grammars repository](https://github.com/antlr/grammars-v4). Download the COBOL grammar (`Cobol85.g4` for COBOL-85, for example).

2. **Generate Python Files with ANTLR**: Use the ANTLR tool to generate Python files from the COBOL grammar.

3. **Implement a Custom Visitor**: Create a visitor class in Python that walks through the parsed COBOL syntax tree. This visitor will analyze `IF`, `PERFORM`, and other control-flow statements to build the control flow graph and evaluate business rules.

4. **Construct the Control Flow Graph**: Using libraries like `networkx` (for graphs) or similar, build a CFG based on the parsed structure.

### Step-by-Step Example

Here's a sample setup assuming you have the COBOL grammar and the ANTLR tool installed.

#### 1. Generate the Python Parser Files

Run the following command in a terminal to generate Python code from the COBOL grammar (`Cobol85.g4`):

```bash
antlr4 -Dlanguage=Python3 Cobol85.g4 -o cobol_parser
```

This will create the Python files in the `cobol_parser` directory, including `Cobol85Lexer.py` and `Cobol85Parser.py`.

#### 2. Install Required Libraries

```bash
pip install antlr4-python3-runtime networkx
```

#### 3. Write the Python Script

The script below parses a COBOL file and uses a visitor to build a control flow graph:

```python
import networkx as nx
from antlr4 import *
from cobol_parser.Cobol85Lexer import Cobol85Lexer
from cobol_parser.Cobol85Parser import Cobol85Parser
from cobol_parser.Cobol85ParserVisitor import Cobol85ParserVisitor

class CobolCFGVisitor(Cobol85ParserVisitor):
    def __init__(self):
        # Initialize the control flow graph
        self.cfg = nx.DiGraph()
        self.current_node = None

    def visitProcedureDivision(self, ctx):
        # Entry point for COBOL procedure division
        self.current_node = "Start"
        self.cfg.add_node(self.current_node)
        return self.visitChildren(ctx)

    def visitParagraph(self, ctx):
        # Each paragraph is a node in the CFG
        paragraph_name = ctx.IDENTIFIER().getText()
        self.cfg.add_node(paragraph_name)
        
        # Link current node to this paragraph
        if self.current_node:
            self.cfg.add_edge(self.current_node, paragraph_name)
        self.current_node = paragraph_name

        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx):
        # Node for IF statement, add conditional branch
        if_condition = f"IF ({ctx.condition().getText()})"
        self.cfg.add_node(if_condition)
        self.cfg.add_edge(self.current_node, if_condition)
        self.current_node = if_condition

        # Process the 'THEN' branch
        then_branch = f"THEN-{self.current_node}"
        self.cfg.add_node(then_branch)
        self.cfg.add_edge(if_condition, then_branch)
        self.current_node = then_branch
        self.visit(ctx.thenPart())

        # Process the 'ELSE' branch if present
        if ctx.elsePart():
            else_branch = f"ELSE-{self.current_node}"
            self.cfg.add_node(else_branch)
            self.cfg.add_edge(if_condition, else_branch)
            self.current_node = else_branch
            self.visit(ctx.elsePart())

        return None  # Return None to prevent double visits

    def visitPerformStatement(self, ctx):
        # Handle PERFORM statements, linking to called paragraphs
        perform_node = f"PERFORM {ctx.IDENTIFIER().getText()}"
        self.cfg.add_node(perform_node)
        self.cfg.add_edge(self.current_node, perform_node)
        self.current_node = perform_node
        return self.visitChildren(ctx)

    def visitStopStatement(self, ctx):
        # Add end node
        stop_node = "STOP"
        self.cfg.add_node(stop_node)
        self.cfg.add_edge(self.current_node, stop_node)
        self.current_node = stop_node
        return None

def build_cfg(cobol_code):
    # Setup ANTLR input stream and lexer/parser
    input_stream = InputStream(cobol_code)
    lexer = Cobol85Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)

    # Parse the COBOL file and generate the CFG
    tree = parser.program()
    visitor = CobolCFGVisitor()
    visitor.visit(tree)
    
    return visitor.cfg

# Sample COBOL code
cobol_code = """
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TestProgram.
       PROCEDURE DIVISION.
       PARA-1.
           IF X > 10
               PERFORM PARA-2
           ELSE
               PERFORM PARA-3.
       PARA-2.
           DISPLAY 'Greater than 10'.
       PARA-3.
           DISPLAY 'Less or equal to 10'.
           STOP RUN.
"""

# Build the control flow graph
cfg = build_cfg(cobol_code)

# Print the CFG as edges
print("Control Flow Graph Edges:")
for edge in cfg.edges:
    print(edge)
```

### Explanation

1. **`CobolCFGVisitor` Class**: This visitor traverses the COBOL syntax tree:
   - `visitProcedureDivision`: Starts the CFG construction.
   - `visitParagraph`: Each paragraph becomes a node in the CFG.
   - `visitIfStatement`: Adds conditional nodes and branches for `IF-THEN-ELSE` statements.
   - `visitPerformStatement`: Links paragraphs based on `PERFORM` statements.
   - `visitStopStatement`: Adds a terminal node.

2. **Building the CFG**: The `build_cfg` function parses the COBOL code and returns a `networkx` graph representing the CFG.

3. **Sample Output**: The edges of the CFG show the flow between different COBOL paragraphs and conditional statements.

### Extending for Business Rules

To add business rules, define functions within the visitor to match specific COBOL patterns or variables. For instance, you could add rule checks inside `visitIfStatement` to evaluate complex conditions or custom rules based on specific COBOL variables.

This setup gives you a basic CFG and is extensible to handle more complex business rules and control flow constructs in COBOL.