# step2_visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the distance matrix
distance_df = pd.read_csv("data/distance_matrix.csv", index_col=0)

# Find shortest and longest distances (excluding 0)
non_zero_distances = distance_df.replace(0, float('inf'))
shortest_distance = non_zero_distances.min().min()
longest_distance = distance_df.max().max()

shortest_pair = non_zero_distances.stack().idxmin()  # (Origin, Destination)
longest_pair = distance_df.stack().idxmax()          # (Origin, Destination)

# Plot heatmap
plt.figure(figsize=(9, 7))
sns.heatmap(distance_df, annot=True, fmt=".1f", cmap="YlOrRd", cbar_kws={'label': 'Distance (km)'})

# Highlight cells
origin_labels = distance_df.index.tolist()
dest_labels = distance_df.columns.tolist()

def highlight_cell(pair, color):
    i = origin_labels.index(pair[0])
    j = dest_labels.index(pair[1])
    plt.gca().add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor=color, linewidth=3, linestyle="--"))

highlight_cell(shortest_pair, 'green')  # Shortest
highlight_cell(longest_pair, 'red')     # Longest

# Add labels
plt.text(
    dest_labels.index(shortest_pair[1]) + 0.5,
    origin_labels.index(shortest_pair[0]) + 0.5,
    "Shortest", color="green", fontsize=10, ha="center", va="center", weight="bold"
)
plt.text(
    dest_labels.index(longest_pair[1]) + 0.5,
    origin_labels.index(longest_pair[0]) + 0.5,
    "Longest", color="red", fontsize=10, ha="center", va="center", weight="bold"
)

# Title & Save
plt.title("Delivery Distance Heatmap", fontsize=16, weight='bold')
plt.xlabel("Destination", fontsize=12)
plt.ylabel("Origin", fontsize=12)
plt.tight_layout()

# Save outputs
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/distance_heatmap_upgraded.png", dpi=300)
plt.savefig("outputs/distance_heatmap_report.pdf")
plt.show()

print("Heatmap saved as outputs/distance_heatmap_upgraded.png and PDF.")
