# Q: Standardize dataset using Z-score normalization

import numpy as np

# Create dataset (rows = samples, columns = features)
data = np.array([
    [25, 50000, 80],
    [30, 60000, 85],
    [35, 65000, 90],
    [40, 70000, 95],
    [45, 80000, 100]
])

# Step 1: Calculate mean of each column
mean = np.mean(data, axis=0)

# Step 2: Calculate standard deviation
std = np.std(data, axis=0)

# Step 3: Apply Z-score formula
z_score = (data - mean) / std

print("Standardized Data:\n", z_score)
