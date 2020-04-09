grades = [int(input()) for _ in range(int(input()))]
newGrade = []
finalGrade = []
for i in range(len(grades)):
    a = 5 - (grades[i] % 5)
    if grades[i]==38:
        newGrade.append(2)
    if grades[i] <= 40:
        newGrade.append(0)
    if grades[i] > 40:
        if a < 3:
            newGrade.append(a)
        else:
            newGrade.append(0)
print(grades)
print(newGrade)
for j in range(len(grades)):
    finalGrade.append(grades[j] + newGrade[j])
print(finalGrade)
