"""
python utils/visualize_brs.py input/DIVIDE_BRs.json
"""
import sys
import json
import graphviz


json_path = sys.argv[1]

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def visualize_graph(business_rule_name, rule_data):
    dot = graphviz.Digraph(comment=business_rule_name)

    # Customize overall graph appearance
    dot.attr(rankdir='TB', size='10,10', bgcolor='lightgrey')

    # Add nodes with styles
    for node in rule_data['nodes']:
        dot.node(node['id'], 
                 label=node['data']['label'], 
                 shape='box',          # Box shape for nodes
                 style='filled',       # Filled nodes
                 fillcolor='lightblue' if 'EVALUATE' in node['data']['label'] else 'lightyellow',  # Color based on label
                 fontcolor='black')    # Font color

    # Add edges with styles
    for edge in rule_data['edges']:
        dot.edge(edge['source'], edge['target'], 
                 label=edge['label'],
                 color='black',        # Edge color
                 style='dashed' if 'false' in edge['label'].lower() else 'solid')  # Dashed for false edges

    return dot

def main():
    # Load the JSON data
    cfg_data = read_json_file(json_path)

    # Generate and save visualizations for each business rule
    for rule_name, rule_data in cfg_data['business_rules'].items():
        dot = visualize_graph(rule_name, rule_data)
        dot.render(f'brs_{rule_name}', format='png', cleanup=True)

if __name__ == "__main__":
    main()
