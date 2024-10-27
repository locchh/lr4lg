# Build CFG

To automatically generate a control flow graph (CFG) for COBOL code, you can use a combination of tools and techniques involving parsing, control-flow analysis, and visualization libraries. Here's an outline of an approach using ANTLR and Python, which aligns with your experience in working with ANTLR.

### Steps to Automatically Generate a CFG

1. **Set Up COBOL Grammar with ANTLR**:
   - Use an ANTLR grammar for COBOL (several are available online) or adapt an existing one for your specific needs.
   - The grammar will parse the COBOL code and break it down into its syntactic components (such as `DIVIDE`, `IF`, `DISPLAY` statements).

2. **Create a Custom Visitor in Python**:
   - Use ANTLR's visitor pattern to traverse the parse tree.
   - Implement logic in the visitor to recognize key control flow structures (e.g., branches, conditional statements).
   - For example, when encountering an `IF` statement, create nodes for the condition check, true branch, and false branch.

3. **Build the CFG Structure in Python**:
   - As the visitor processes each COBOL statement, build a control flow structure.
   - Represent each statement as a node and connect nodes based on control flow (e.g., link the `IF` condition to its true and false branches).
   - You can use Python data structures like dictionaries or specialized libraries (e.g., `networkx`) to store nodes and edges.

4. **Visualize the CFG**:
   - Use a graph visualization library like `Graphviz` or `networkx` to display the generated CFG.
   - These libraries allow you to specify nodes and edges and render the graph as an image.

### Example of the Implementation

Here's a basic outline of how this process might look in Python:

#### Step 1: Parse the COBOL Code

Define a COBOL grammar in ANTLR and use it to generate a parse tree. For example, suppose the grammar recognizes statements like `DIVIDE`, `IF`, and `DISPLAY`.

#### Step 2: Implement a Visitor for Control Flow Analysis

```python
from antlr4 import *
from MyCobolParser import MyCobolParser  # Generated from ANTLR grammar
from MyCobolVisitor import MyCobolVisitor  # Custom visitor
import networkx as nx
import matplotlib.pyplot as plt

class CFGVisitor(MyCobolVisitor):
    def __init__(self):
        self.cfg = nx.DiGraph()  # Directed graph for CFG
        self.node_counter = 0

    def add_node(self, label):
        node_name = f"n{self.node_counter}"
        self.cfg.add_node(node_name, label=label)
        self.node_counter += 1
        return node_name

    def visitDivideStatement(self, ctx: MyCobolParser.DivideStatementContext):
        node = self.add_node("DIVIDE NUM BY 2")
        return node

    def visitIfStatement(self, ctx: MyCobolParser.IfStatementContext):
        # Create nodes for the IF condition and branches
        cond_node = self.add_node("IF REMAIN = 0")
        true_branch = self.add_node("DISPLAY 'NUM IS EVEN'")
        false_branch = self.add_node("DISPLAY 'NUM IS ODD'")
        
        # Add edges for the true/false branches
        self.cfg.add_edge(cond_node, true_branch)
        self.cfg.add_edge(cond_node, false_branch)
        return cond_node

    def visitStopRunStatement(self, ctx: MyCobolParser.StopRunStatementContext):
        node = self.add_node("STOP RUN")
        return node
```

#### Step 3: Visualize the CFG

After processing the code, visualize the CFG using `networkx` and `matplotlib`.

```python
def visualize_cfg(cfg):
    pos = nx.spring_layout(cfg)
    labels = nx.get_node_attributes(cfg, 'label')
    nx.draw(cfg, pos, with_labels=True, labels=labels, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
    plt.show()

# Example usage:
visitor = CFGVisitor()
# Assume `parse_tree` is the parsed tree of COBOL code
visitor.visit(parse_tree)
visualize_cfg(visitor.cfg)
```

### Tools Required

- **ANTLR**: For parsing COBOL syntax. You’ll need to install ANTLR and generate Python files for the COBOL grammar.
- **networkx** and **matplotlib**: For constructing and visualizing the CFG graph.

This approach will allow you to automatically generate and visualize a CFG for COBOL code, provided that the grammar and visitor correctly interpret COBOL control structures. Let me know if you'd like more specific guidance on any part of the setup!

# Complex statements

To handle more complex COBOL statements like `IF`, `WHILE`, and `PERFORM`, you can expand your ANTLR visitor and CFG construction logic to account for nested structures, loops, and branching conditions. Each of these control structures introduces additional nodes and edges in the CFG and may require special handling for entry and exit points. Here’s how you can approach each type of statement:

### 1. Handling `IF` Statements (with Nested or Compound Conditions)

For `IF` statements with multiple branches, nested conditions, or `ELSE IF` clauses, you can:
- Create a **condition node** to evaluate the `IF` condition.
- Create **true and false branch nodes** for the branches.
- Link the **exit nodes** of each branch back to a common merge point.

For nested `IF` statements, recursively process each `IF` as a subgraph and integrate it into the main CFG.

```python
def visitIfStatement(self, ctx: MyCobolParser.IfStatementContext):
    cond_node = self.add_node(f"IF {ctx.condition().getText()}")
    
    # True branch
    true_branch = self.add_node("True Branch")
    self.cfg.add_edge(cond_node, true_branch)
    self.visit(ctx.true_branch())

    # False branch (if available)
    if ctx.false_branch():
        false_branch = self.add_node("False Branch")
        self.cfg.add_edge(cond_node, false_branch)
        self.visit(ctx.false_branch())
    
    return cond_node
```

### 2. Handling `WHILE` Statements (or Conditional Loops)

`WHILE` statements create loops in the CFG, meaning:
- The **condition node** should loop back to itself if the condition is true.
- Add an **exit edge** for when the condition is false, leading out of the loop.

To implement this:
1. Create a node for the loop’s condition check.
2. Add an edge from the condition node to the body of the loop.
3. Add an edge from the loop body back to the condition node, creating a cycle.
4. Add an edge from the condition node to an exit node if the condition is false.

```python
def visitWhileStatement(self, ctx: MyCobolParser.WhileStatementContext):
    cond_node = self.add_node(f"WHILE {ctx.condition().getText()}")
    
    # Loop body node
    body_node = self.add_node("Loop Body")
    self.cfg.add_edge(cond_node, body_node)
    
    # Visit loop body recursively
    self.visit(ctx.loop_body())
    
    # Link loop back to condition node for next check
    self.cfg.add_edge(body_node, cond_node)
    
    # Exit node if condition fails
    exit_node = self.add_node("Exit Loop")
    self.cfg.add_edge(cond_node, exit_node)
    
    return cond_node
```

### 3. Handling `PERFORM` Statements (Including `PERFORM UNTIL`)

The `PERFORM` statement in COBOL can act like a function call or a loop, depending on its form:
- **Simple `PERFORM`**: Adds a direct edge to the target procedure or code block.
- **`PERFORM UNTIL`**: Similar to a `WHILE` loop, where the CFG has a condition node, body nodes, and exit nodes.
- **`PERFORM ... THRU`**: Calls a sequence of paragraphs, each treated as a separate node.

#### Example: Handling `PERFORM UNTIL`

```python
def visitPerformUntilStatement(self, ctx: MyCobolParser.PerformUntilStatementContext):
    cond_node = self.add_node(f"PERFORM UNTIL {ctx.condition().getText()}")
    
    # Loop body node
    body_node = self.add_node("Perform Body")
    self.cfg.add_edge(cond_node, body_node)
    
    # Visit the body of the PERFORM statement
    self.visit(ctx.perform_body())
    
    # Link loop back to condition node for repeated checks
    self.cfg.add_edge(body_node, cond_node)
    
    # Exit node for when the UNTIL condition is met
    exit_node = self.add_node("Exit Perform")
    self.cfg.add_edge(cond_node, exit_node)
    
    return cond_node
```

### 4. Handling Nested and Sequential Statements

For complex nested structures or sequences of statements, recursively handle each statement, creating separate subgraphs as needed. You can combine these subgraphs to form the overall CFG.

#### Example: Combining Nodes for a Sequence of Statements

In COBOL, code often contains sequential `PERFORM`, `IF`, or `WHILE` statements. You can process these by:
1. Visiting each statement in sequence.
2. Linking each node’s exit to the entry node of the next.

### Summary

With these techniques, you can systematically build CFGs for more complex COBOL structures. The goal is to adapt the visitor to capture all possible control paths, especially for nested and iterative constructs, to accurately represent the flow in your CFG. Let me know if you need further guidance on a particular statement or CFG structure!

# Nested

Handling nested statements, such as an `IF` statement inside another `IF` or a `WHILE` loop, requires a recursive approach in your visitor implementation. Each nested statement should be treated as a subgraph that connects appropriately with its surrounding control structures. Here’s a strategy for handling these cases in your CFG generation process:

### Key Steps for Nested Statements

1. **Recursive Visitor Pattern**:
   - Use recursion in your visitor methods to handle nested structures.
   - When encountering a nested `IF` or `WHILE`, call the visitor for that statement, allowing it to build a subgraph for the nested part.

2. **Connecting Nodes**:
   - Connect the **exit node** of the inner statement back to the outer statement, ensuring the correct flow.
   - Maintain a **stack** or a **last-visited node reference** to keep track of the CFG nodes, making it easier to link nodes at different nesting levels.

### Example: `IF` Statement Inside Another `IF` Statement

To handle an `IF` inside another `IF`, you can create a conditional node for the outer `IF` and link the true and false branches accordingly. When you encounter a nested `IF` in the true or false branch, you recursively create its CFG.

Here’s an example implementation in Python:

```python
def visitIfStatement(self, ctx: MyCobolParser.IfStatementContext):
    # Outer IF condition node
    outer_cond_node = self.add_node(f"IF {ctx.condition().getText()}")

    # True branch of the outer IF
    true_branch_node = self.add_node("True Branch")
    self.cfg.add_edge(outer_cond_node, true_branch_node)
    
    # Check if there’s a nested IF in the true branch
    if ctx.true_branch_contains_if():
        nested_if_node = self.visit(ctx.true_branch_if())
        self.cfg.add_edge(true_branch_node, nested_if_node)
    else:
        # Process the non-IF statements in the true branch
        self.visit(ctx.true_branch())

    # False branch of the outer IF
    if ctx.false_branch():
        false_branch_node = self.add_node("False Branch")
        self.cfg.add_edge(outer_cond_node, false_branch_node)
        
        if ctx.false_branch_contains_if():
            nested_if_node = self.visit(ctx.false_branch_if())
            self.cfg.add_edge(false_branch_node, nested_if_node)
        else:
            # Process the non-IF statements in the false branch
            self.visit(ctx.false_branch())
    
    return outer_cond_node
```

### Example: `IF` Statement Inside a `WHILE` Statement

When you have an `IF` statement inside a `WHILE` loop, the `WHILE` loop condition node will have a body that includes the `IF` statement.

Here’s how to handle this in your visitor:

```python
def visitWhileStatement(self, ctx: MyCobolParser.WhileStatementContext):
    # WHILE condition node
    cond_node = self.add_node(f"WHILE {ctx.condition().getText()}")
    
    # Loop body node
    body_node = self.add_node("Loop Body")
    self.cfg.add_edge(cond_node, body_node)
    
    # Visit loop body, which may contain an IF statement
    if ctx.body_contains_if():
        nested_if_node = self.visit(ctx.body_if_statement())
        self.cfg.add_edge(body_node, nested_if_node)
    else:
        # Process non-IF statements in the loop body
        self.visit(ctx.loop_body())

    # Link the loop body back to the condition node for repeated checks
    self.cfg.add_edge(body_node, cond_node)

    # Exit node for when the WHILE condition is false
    exit_node = self.add_node("Exit Loop")
    self.cfg.add_edge(cond_node, exit_node)
    
    return cond_node
```

### Maintaining Flow with Nested Statements

To ensure correct flow in more deeply nested structures, maintain:
- **A reference to the last node of each branch** (e.g., the last statement inside a true branch or loop body). This allows you to connect nodes across different levels of nesting.
- **Backtracking connections** for loops and outer conditions, ensuring that nested statements within loops properly exit back to the loop condition or outer condition when finished.

### Summary

Using recursion and carefully connecting nodes at each level of nesting enables you to handle complex nested statements. With this approach, each nested structure is built as a subgraph within the CFG, keeping the overall flow correct. Let me know if you’d like to see a specific nested structure in more detail or if there are other types of nesting you’re dealing with!