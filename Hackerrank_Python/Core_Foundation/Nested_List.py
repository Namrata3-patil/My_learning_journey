# PROBLEM: Find student(s) with the second-lowest grade from a list of names and scores.
# SOLUTION: Isolate unique grades, sort ascending to find the second-lowest value, filter matching students, and print their names alphabetically.

if __name__ == '__main__':
    students = []
    
    # 1. Read input data and build a nested list of [name, score]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # 2. Extract scores, remove duplicates via set(), sort ascending, and grab index 1
    scores = sorted(list(set([student[1] for student in students])))
    second_lowest = scores[1]

    # 3. Filter the original list to get names matching the second-lowest score
    names = [student[0] for student in students if student[1] == second_lowest]

    # 4. Sort the filtered names alphabetically and print each line by line
    for name in sorted(names):
        print(name)
