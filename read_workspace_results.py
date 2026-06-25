import json

notebook_path = "notebooks/wagers-balancing/wagers-balancing.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in [15, 16]:
    if i < len(nb['cells']):
        cell = nb['cells'][i]
        print(f"\n=================== CELL {i} ({cell['cell_type'].upper()}) ===================")
        print("SOURCE:")
        print("".join(cell['source']))
        print("OUTPUTS:")
        for out in cell.get('outputs', []):
            if 'text' in out:
                print(out['text'])
            elif 'data' in out and 'text/plain' in out['data']:
                print(out['data']['text/plain'])
            elif 'data' in out and 'text/html' in out['data']:
                print(out['data']['text/html'][:1000]) # Truncate html if too long
