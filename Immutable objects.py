# valid dictionary
# integer as a key
my_dict = {1: "one", 2: "two", 3: "three"}

# valid dictionary
# tuple as a key
my_dict = {(1, 2): "one two", 3: "three"}

# invalid dictionary (fixed)
# Using a tuple instead of a list as a key
my_dict = {1: "Hello", (1, 2): "Hello hi"}

# valid dictionary
# string as a key, list as a value
my_dict = {"USA": ["Chicago", "California", "New York"]}