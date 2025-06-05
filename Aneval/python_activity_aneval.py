# GROUP 1: CREW-INAMERS


# Treasure Trail
# Data Structured Used: LINK LIST
print("Treasure Trail")
clues = [10, 20, 30]

for clue in clues:
    print(clue)

print("\n")



# Magic Word Reverser
# Data Structured Used: STACK
print("Magic Word Reverser")
secret_word = input("The wizard whispers a secret word: ")
reversed_word = secret_word[::-1]
print("The magic revealed:", reversed_word)

print("\n")



# Theme Park Ride Line
# Data Structured Used: QUEUES
print("Theme Park Ride Line")
ride_line = [5, 10, 15]
print("Line formed:", ride_line)
ride_line.pop(0)  # First friend boards
print("Still waiting:", ride_line)

print("\n")


# Pirate’s Loot Count
# Data Structured Used: HASH TABLE
print("Pirate’s Loot Count")
loot = ["gold", "silver", "gold", "diamond", "silver", "gold"]
loot_count = {}

for item in loot:
    if item in loot_count:
        loot_count[item] += 1
    else:
        loot_count[item] = 1

print("Loot counts:", loot_count)


# Family Tree
# Data Structured Used: TREES
print("Family Tree")
family_tree = {
    "Ryan": ["Bob", "Carol"],
    "Harly": ["Adan"],
    "Clear": ["Nique"],
    "Michael": ["Eva"],
    "Kenji": ["Fillepe"]
}

for parent, children in family_tree.items():
    if children:
        print(f"{parent} is parent of {', '.join(children)}")
    else:
        print(f"{parent} has no children")


# City Map
# Data Structured Used: LINK LIST
print("City Map")
# Graph represented as adjacency list
city_map = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"]
}

def can_travel(city_map, start, end, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        return True
    visited.add(start)
    for neighbor in city_map.get(start, []):
        if neighbor not in visited:
            if can_travel(city_map, neighbor, end, visited):
                return True
    return False

start_city = input("Enter starting city: ")
end_city = input("Enter destination city: ")

if can_travel(city_map, start_city, end_city):
    print(f"You can travel from {start_city} to {end_city}.")
else:
    print(f"You cannot travel from {start_city} to {end_city}.")