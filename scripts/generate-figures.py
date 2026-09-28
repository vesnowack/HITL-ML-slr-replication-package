"""Generate the by-year and venue-type distribution figures from
`../primary-studies.csv`, writing them into `../figures/`.

Run from this directory: python3 generate-figures.py
Requires: pandas, matplotlib
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../primary-studies.csv')

# ---- Bar chart: publications per year ----
year_counts = df['year'].value_counts().sort_index()
all_years = range(int(year_counts.index.min()), int(year_counts.index.max()) + 1)
year_counts_full = year_counts.reindex(all_years, fill_value=0)

plt.figure(figsize=(8, 4))
plt.bar(all_years, year_counts_full.values, color='#265C8A', width=0.8, zorder=3)
for y in [2, 4, 6, 8, 10]:
    plt.axhline(y=y, color='lightgray', linewidth=0.8, zorder=1)
plt.xticks(all_years, rotation=0, fontsize=13)
plt.yticks(fontsize=15)
plt.xlabel('')
plt.ylabel('')
plt.tight_layout()
plt.savefig('../figures/article_numbers.png', dpi=300)
plt.close()

# ---- Pie chart: venue type distribution (Conference, Symposium, Journal) ----
venue_filtered = df[df['venue_type'].isin(['C', 'S', 'J'])]
venue_counts = venue_filtered['venue_type'].value_counts()

label_map = {'C': 'Conference', 'S': 'Symposium', 'J': 'Journal'}
labels = [label_map[v] for v in venue_counts.index]
color_map = {'C': '#7fa6d5', 'S': '#88c999', 'J': '#f4a15d'}
pie_colors = [color_map[v] for v in venue_counts.index]

plt.figure(figsize=(5, 5))
ax = venue_counts.plot(
    kind='pie', labels=labels, autopct='%1.1f%%', startangle=90,
    counterclock=False, colors=pie_colors, textprops={'fontsize': 12},
)
plt.ylabel('')
plt.setp(ax.texts, size=16)
plt.tight_layout()
plt.savefig('../figures/article_distribution.png', dpi=300)
plt.close()

print("Wrote ../figures/article_numbers.png and ../figures/article_distribution.png")
