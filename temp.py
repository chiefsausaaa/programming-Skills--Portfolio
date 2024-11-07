# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# The name we are searching for
search_name = "Sam"

# Search for "Sam" in the list
found = False
for name in names:
    if name == search_name:
        found = True
        break

# Output the result
if found:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")