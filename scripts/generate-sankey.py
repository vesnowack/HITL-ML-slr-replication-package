"""Sankey diagram of how primary studies connect across all four RQs:
role (RQ1) -> action (RQ2) -> quality attribute (RQ3) -> metric (RQ4).

Run from this directory: python3 generate-sankey.py
Requires: plotly, kaleido
"""
import csv
import itertools
from pathlib import Path

import plotly.graph_objects as go

FILES = [
    ('../data-extraction/rq1-roles.csv', 'role'),
    ('../data-extraction/rq2-interactions.csv', 'action'),
    ('../data-extraction/rq3-quality-attributes.csv', 'quality_attribute'),
    ('../data-extraction/rq4-evaluation-metrics.csv', 'metric'),
]
STAGE_NAMES = ['Role', 'Action', 'Quality attribute', 'Metric']
STAGE_COLORS = ['#4C78A8', '#F58518', '#54A24B', '#7F7F7F']


def load_stage(path, col):
    """citation_key -> list of category strings, split on commas, as
    literally recorded in the extraction CSV (title-cased for display)."""
    per_paper = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            cell = (row[col] or '').strip()
            cats = [c.strip().title() for c in cell.split(',') if c.strip()]
            per_paper[row['citation_key']] = cats
    return per_paper


stages = [load_stage(path, col) for path, col in FILES]
all_papers = set(stages[0].keys())
for s in stages[1:]:
    all_papers &= set(s.keys())

paper_categories = {p: [stage[p] for stage in stages] for p in all_papers}

node_labels, node_colors, node_index = [], [], {}
for stage_i, stage in enumerate(stages):
    labels_this_stage = sorted({c for cats in stage.values() for c in cats})
    for label in labels_this_stage:
        node_index[(stage_i, label)] = len(node_labels)
        node_labels.append(label)
        node_colors.append(STAGE_COLORS[stage_i])

link_counts = {}
skipped = []
for p, cats_per_stage in paper_categories.items():
    if any(len(cats) == 0 for cats in cats_per_stage):
        skipped.append(p)
        continue
    for combo in itertools.product(*cats_per_stage):
        for stage_i in range(len(stages) - 1):
            key = (stage_i, combo[stage_i], combo[stage_i + 1])
            link_counts[key] = link_counts.get(key, 0) + 1

if skipped:
    print(f"Skipped {len(skipped)} paper(s) missing a category in some RQ dimension: {skipped}")


def hex_to_rgba(hex_color, alpha):
    hex_color = hex_color.lstrip('#')
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    return f'rgba({r},{g},{b},{alpha})'


sources, targets, values, link_colors = [], [], [], []
for (stage_i, llabel, rlabel), count in link_counts.items():
    sources.append(node_index[(stage_i, llabel)])
    targets.append(node_index[(stage_i + 1, rlabel)])
    values.append(count)
    link_colors.append(hex_to_rgba(STAGE_COLORS[stage_i], 0.4))

fig = go.Figure(go.Sankey(
    arrangement='snap',
    textfont=dict(color='black', size=16),
    node=dict(label=node_labels, color=node_colors, pad=15, thickness=18,
              line=dict(color='black', width=0.5)),
    link=dict(source=sources, target=targets, value=values, color=link_colors),
))
fig.update_layout(font_size=16, width=1400, height=600, margin=dict(l=10, r=10, t=10, b=10))

out_html = Path('../figures/sankey_rq_combinations_reproduction.html')
fig.write_html(str(out_html))
print(f"Wrote {out_html}")

out_png = Path('../figures/sankey_rq_combinations_reproduction.png')
try:
    fig.write_image(str(out_png), scale=2)
    print(f"Wrote {out_png}")
except Exception as e:
    print(f"Could not export static PNG ({e}); open {out_html} in a browser instead, "
          f"or install a working kaleido (`pip install 'plotly[kaleido]'`).")
