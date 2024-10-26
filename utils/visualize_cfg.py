"""
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

    # Add nodes
    for node in data['nodes']:
        dot.node(node['id'], node['data']['label'])

    # Add edges
    for edge in data['edges']:
        dot.edge(edge['source'], edge['target'], label=edge['label'])

    # Save and render the graph
    dot.render('cfg', format='png', cleanup=True)  # Saves as 'cfg.png'

if __name__ == '__main__':

    data = read_json_file(sys.argv[1])

    visualize_graph(data)