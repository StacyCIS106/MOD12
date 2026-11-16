file_content = """Rosiles, 85
Smith, 92
Johnson, 78
Williams, 90
Brown, 88
Jones, 95
Garcia, 80
Miller, 87
Davis, 91
Rodriguez, 89
"""

with open("exam_scores.txt", "w") as file:
    file.write(file_content)

lastnames = []
exam_scores = []
with open("exam_scores.txt", "r") as file:
    for line in file:
        lastname, score_str = line.split(",")
        lastnames.append(lastname.strip())
        exam_scores.append(int(score_str.strip()))

def display_lastnames(names, scores):
    print("Last Names and Exam Scores:")
    for i in range(len(names)):
        print(f"{names[i]}: {scores[i]}")

def display_lastnames_reverse(names, scores):
    print("Last Names in Reverse Order:")
    for i in range(len(names) - 1, -1, -1):
        print(f"{names[i]}: {scores[i]}")

def display_high_low_scores(names, scores):
    high_score = max(scores)
    low_score = min(scores)
    high_index = scores.index(high_score)
    low_index = scores.index(low_score)
    print(f"Highest Score: {names[high_index]} with {high_score}")
    print(f"Lowest Score: {names[low_index]} with {low_score}")

display_lastnames(lastnames, exam_scores)
display_lastnames_reverse(lastnames, exam_scores)
display_high_low_scores(lastnames, exam_scores)