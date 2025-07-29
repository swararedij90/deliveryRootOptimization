# step3_optimization.py
import pandas as pd
import matplotlib.pyplot as plt
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD
import os

# --- Setup Paths ---
os.makedirs("outputs", exist_ok=True)

# Load distance matrix
distance_df = pd.read_csv("data/distance_matrix.csv", index_col=0)

# Locations (same as Step 1)
locations = {
    "Warehouse": (0, 0),
    "Customer_1": (2, 3),
    "Customer_2": (5, 4),
    "Customer_3": (1, 7),
    "Customer_4": (6, 1),
    "Customer_5": (8, 3),
}

# --- Optimization Problem ---
prob = LpProblem("DeliveryRouteOptimization", LpMinimize)

# Decision variables: x[i][j] = 1 if traveling from i to j
x = {}
for i in distance_df.index:
    for j in distance_df.columns:
        if i != j:
            x[(i, j)] = LpVariable(f"x_{i}_{j}", cat="Binary")

# Objective: Minimize total travel distance
prob += lpSum(distance_df.loc[i, j] * x[(i, j)] for i, j in x)

# Constraints: Each customer is visited once
for k in distance_df.index:
    if k != "Warehouse":
        prob += lpSum(x[(i, k)] for i in distance_df.index if i != k) == 1
        prob += lpSum(x[(k, j)] for j in distance_df.columns if j != k) == 1

# Warehouse must start and end the route
prob += lpSum(x[("Warehouse", j)] for j in distance_df.columns if j != "Warehouse") == 1
prob += lpSum(x[(i, "Warehouse")] for i in distance_df.index if i != "Warehouse") == 1

# Solve using CBC solver
prob.solve(PULP_CBC_CMD(msg=0))

# --- Extract selected edges ---
selected_edges = [(i, j) for (i, j) in x if x[(i, j)].value() == 1]

# --- Build the route sequence ---
route = ["Warehouse"]
current = "Warehouse"
while True:
    next_stop = [j for (i, j) in selected_edges if i == current]
    if not next_stop:
        break
    current = next_stop[0]
    route.append(current)
    if current == "Warehouse":
        break

print("Optimized Route:", " → ".join(route))

# --- Plot the Optimized Route ---
plt.figure(figsize=(8, 6))
for name, (x_coord, y_coord) in locations.items():
    plt.scatter(x_coord, y_coord, color="blue", s=120, zorder=3)
    plt.text(x_coord + 0.2, y_coord + 0.2, name, fontsize=10, weight='bold')

for i, j in selected_edges:
    x_coords = [locations[i][0], locations[j][0]]
    y_coords = [locations[i][1], locations[j][1]]
    plt.plot(x_coords, y_coords, color="red", linewidth=2, marker="o", zorder=2)

plt.title("Optimized Delivery Route", fontsize=14, weight='bold')
plt.xlabel("X Coordinate (km)")
plt.ylabel("Y Coordinate (km)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save output
plt.savefig("outputs/optimized_route.png", dpi=300)
plt.show()

print("Optimized route saved as outputs/optimized_route.png")
