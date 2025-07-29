# step2_matrices.py
import numpy as np
import pandas as pd
import random
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Delivery locations
locations = [
    ("Warehouse", 0, 0),
    ("Customer_1", 2, 3),
    ("Customer_2", 5, 4),
    ("Customer_3", 1, 7),
    ("Customer_4", 6, 1),
    ("Customer_5", 8, 3)
]

# Step 2: Distance Matrix with Travel Time & Delays
n = len(locations)
distance_matrix = np.zeros((n, n))
time_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        xi, yi = locations[i][1], locations[i][2]
        xj, yj = locations[j][1], locations[j][2]
        distance = np.sqrt((xi - xj)**2 + (yi - yj)**2)  # Euclidean distance (km)
        distance_matrix[i, j] = round(distance, 2)

        # Estimate travel time (speed = 40 km/h) in minutes
        base_time = (distance / 40) * 60  # minutes
        delay = random.randint(0, 10)  # random delay (0-10 mins)
        time_matrix[i, j] = round(base_time + delay, 1)

# Save as CSV
labels = [loc[0] for loc in locations]
df_dist = pd.DataFrame(distance_matrix, index=labels, columns=labels)
df_time = pd.DataFrame(time_matrix, index=labels, columns=labels)

df_dist.to_csv("data/distance_matrix.csv")
df_time.to_csv("data/time_matrix.csv")

print("\nDistance Matrix (km):")
print(df_dist)
print("\nTravel Time Matrix (minutes):")
print(df_time)
print("\nSaved to data/distance_matrix.csv and data/time_matrix.csv")
