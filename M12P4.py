file_content = """Stacy, 0.31
Alyssa, 0.25
Jenny, 0.35
Simon, 0.28
Marcy, 0.30
Kyle, 0.22
Alex, 0.29
Jordan, 0.33
Taylor, 0.27
Morgan, 0.32"""
with open("players_scores.txt", "w") as file:
    file.write(file_content)

def display_player_names(names, averages):
    print("Player Names:")
    for i in range(len(names)):
        print(f"{names[i]}: {averages[i]}")

def search_player(names, averages, target):
    found = False
    for i in range(len(names)):
        if names[i].lower() == target.lower():
            print(f"{names[i]}: {averages[i]}")
            found = True
    return found


player_names = []
player_averages = []
infile = open("players_scores.txt", "r")

for line in infile:
    data = line.split(",")
    player_names.append(data[0].strip())
    player_averages.append(float(data[1].strip()))

infile.close()

display_player_names(player_names, player_averages)

answer = "yes"
while answer == "yes":
    target_name = input("Enter a player's name to search: ")
    search_player(player_names, player_averages, target_name)
    answer = input("Do you want to search for another player? (yes/no): ")