
print("Enter in the game scores on each line to calculate their possibilites, and a negative score to exit.")

scores = [2, 3, 6, 7, 8]
result = []

while True:
    res = ""
    score_comp = []

    score = int(input())

    if score < 0: break

    possibilities = [0] * score + 1
    possibilities[0] = 1

    for s in scores:
        for i in possibilities:
            possibilities[i] += possibilities[s - i]

    
    

