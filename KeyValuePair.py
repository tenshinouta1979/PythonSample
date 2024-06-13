#https://docs.python.org/3/library/functions.html

# Create a dictionary representing a person's information
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Access values by their keys
print("Name:", person["name"])  # Output: "Alice"
print("Age:", person["age"])    # Output: 30
print("\n")

# Add a new key-value pair
person["occupation"] = "Engineer"

# Modify an existing value
person["age"] = 31

# Remove a key-value pair
del person["city"]

# Iterate through the dictionary
for key, value in person.items():
    print(f"{key}: {value}")
