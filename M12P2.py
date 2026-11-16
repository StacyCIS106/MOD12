lastnames = ("Rosiles", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez")
exam_scores = (85, 92, 78, 90, 88, 95, 80, 87, 91, 89)
def display_lastnames(names):
    print("Last Names and Exam Scores:")
    for i in range(10):
        print(f"{names[i]}: {exam_scores[i]}")

def display_lastnames_reverse(names):
    print("Last Names in Reverse Order:")
    for i in range(9, -1, -1):
        print(f"{names[i]}: {exam_scores[i]}")

display_lastnames(lastnames)
display_lastnames_reverse(lastnames)