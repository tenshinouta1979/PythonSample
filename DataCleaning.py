# Importing the necessary libraries
import pandas as pd
import numpy as np

# Let's assume we have a DataFrame with some missing values and some inconsistent data
data = {
    'Name': ['John', 'Anna', np.nan, 'Mike', 'Laura'],
    'Age': [34, np.nan, np.nan, 45, 'Unknown'],
    'Gender': ['M', 'F', np.nan, 'M', 'F']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Step 1: Handling Missing Values
# We can use the fillna() function to fill the NaN values with a specific value
df['Name'] = df['Name'].fillna('Unknown')
df['Gender'] = df['Gender'].fillna('Not Specified')

# For 'Age', let's assume we want to fill NaN values with the mean age
# First, we need to convert 'Age' to numeric, replacing non-numeric values with NaN
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

print("\nDataFrame after handling missing values:")
print(df)

# Step 2: Handling Inconsistent Data
# We can use the replace() function to replace inconsistent data with a consistent format
df['Gender'] = df['Gender'].replace(['M', 'F'], ['Male', 'Female'])

print("\nDataFrame after handling inconsistent data:")
print(df)
