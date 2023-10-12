if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

for name, marks in student_marks.items():
    if name == query_name:
        res = sum(marks) / len(marks)
print(format(res, ".2f"))
