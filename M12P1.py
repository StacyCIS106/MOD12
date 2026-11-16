lastnames = ("Rosiles", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez")

def display_lastnames(names):
    print("Last Names:")
    for i in range(10):
        print(names[i])

def display_lastnames_reverse(names):
    print("Last Names in Reverse Order:")
    for i in range(9, -1, -1):
        print(names[i])

display_lastnames(lastnames)
display_lastnames_reverse(lastnames)