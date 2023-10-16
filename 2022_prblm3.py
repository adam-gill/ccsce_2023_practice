print("Enter in the game scores on each line to calculate their possibilites, and a negative score to exit.")

scores = [2, 3, 6, 7, 8]
result = []

while True:
    res = ""
    score_comp = []

    score = int(input())
    if score < 0: break
    if score == 1: 
        result.append("0")
        continue

    possibilities = [0] * (score + 1)
    possibilities[0] = 1

    for s in scores:
        for i in range(s, score + 1):
            possibilities[i] += possibilities[i - s]

    while score != 0:
        if score >= 8 and ((score - 8) != 1): 
            score -= 8
            score_comp.insert(0, 8)
        elif score >= 7 and ((score - 7) != 1):
            score -= 7
            score_comp.insert(0, 7)
        elif score >= 6 and ((score - 6) != 1):
            score -= 6
            score_comp.insert(0, 6)
        elif score >= 3 and ((score - 3) != 1):
            score -= 3
            score_comp.insert(0, 3)
        else:
            score -= 2
            score_comp.insert(0, 2)

    if possibilities[len(possibilities) - 1] == 0:
        result.append("0")
    else:
        result.append(f"{possibilities[len(possibilities) - 1]} {score_comp}")

for i in result:
    print(i)