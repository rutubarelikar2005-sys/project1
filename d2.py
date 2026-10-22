# Ass 2 :NumPy Array Operations and Pandas DataFrame

import numpy as np
import pandas as pd

# Create NumPy array
data = np.array([12, 25, 36, 48, 59, 62, 75, 84, 91, 100])

print("Array:") 
print(data)
 
# Sum
print("\nSum =", np.sum(data))

# Mean
print("Mean =", np.mean(data))

# Standard Deviation
print("Standard Deviation =", np.std(data))

# Convert into DataFrame
df = pd.DataFrame(data, columns=["Numbers"])

print("\nFirst Five Records") 
print(df.head())
 