score_comp = []

score = int(input("Enter score: "))

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


    


print(score)
print(score_comp)