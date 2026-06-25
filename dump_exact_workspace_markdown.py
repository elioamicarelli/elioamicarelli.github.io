import json

path = "notebooks/wagers-balancing/wagers-balancing.ipynb"
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        print(f"\n=================== CELL {i} (MARKDOWN) ===================\n")
        print("".join(cell['source']))
