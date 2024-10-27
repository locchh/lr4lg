"""
Usage:
python utils/visualize_cfg.py input/DIVIDE_CFG.json
"""

import sys
import json
from graphviz import Digraph

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def visualize_graph(data):
    dot = Digraph(comment='Control Flow Graph')

    # Set the graph to top-to-bottom layout
    dot.attr(rankdir='TB')  # TB = Top to Bottom

    # Add nodes with enhanced styling
    for node in data['nodes']:
        dot.node(
            node['id'], 
            node['data']['label'], 
            shape='box',               # Set shape to box for clear boundaries
            style='filled,rounded',     # Rounded box for readability
            fillcolor='lightblue',      # Light blue color for visibility
            fontcolor='black',          # Font color for contrast
            fontsize='12'
        )

    # Add edges with styling
    for edge in data['edges']:
        dot.edge(
            edge['source'], 
            edge['target'], 
            label=edge['label'], 
            color='gray',               # Edge color
            fontcolor='blue',           # Font color for label
            fontsize='10',
            style='dashed' if edge['label'] == 'conditional' else 'solid'
        )

    # Save and render the graph as PNG
    dot.render('cfg', format='png', cleanup=True)  # Saves as 'cfg.png'

if __name__ == '__main__':
    data = read_json_file(sys.argv[1])
    visualize_graph(data)
