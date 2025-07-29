# step1_locations.py
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

# --- Step 1: Define Warehouse and Customer Locations ---
locations = {
    "Warehouse": (0, 0),
    "Customer_1": (2, 3),
    "Customer_2": (5, 4),
    "Customer_3": (1, 7),
    "Customer_4": (6, 1),
    "Customer_5": (8, 3)
}

# Save locations to CSV for Step 2
loc_df = pd.DataFrame([(name, x, y) for name, (x, y) in locations.items()],
                      columns=["Location", "X", "Y"])
loc_df.to_csv("data/locations.csv", index=False)

# --- Step 1 Visualization ---
coords = np.array(list(locations.values()))
plt.figure(figsize=(8, 6))
plt.scatter(coords[:, 0], coords[:, 1], c='blue', s=100, label='Locations')

# Add labels to each point
for name, (x, y) in locations.items():
    plt.text(x + 0.2, y + 0.2, name, fontsize=10)

# Draw dotted connections (optional)
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        plt.plot([coords[i][0], coords[j][0]],
                 [coords[i][1], coords[j][1]], 'k--', alpha=0.3)

plt.title("Delivery Locations Map (Step 1)", fontsize=14, weight="bold")
plt.xlabel("X Coordinate (km)")
plt.ylabel("Y Coordinate (km)")
plt.grid(True)
plt.savefig("data/locations_map.png", dpi=300)
plt.show()

print("Step 1 completed: Locations saved to data/locations.csv and map saved as data/locations_map.png")
