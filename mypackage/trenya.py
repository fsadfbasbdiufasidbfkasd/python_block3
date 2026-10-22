def analyze_grades(filename):
    count = 0
    total = 0
    max_grade = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line != "":
            
                count += 1
                total += int(line)
                max_grade.append(int(line))

    max_grade = max(max_grade)        
    average = total / count
    return {
        "count": count,
        "average": average,
        "max": max_grade
    }

with open("grades.txt", "w", encoding="utf-8") as f:
    f.write("5\n4\n\n3\n5\n2\n")

result = analyze_grades("grades.txt")

print(result)

