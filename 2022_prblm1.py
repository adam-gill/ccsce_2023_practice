result = []



print("Enter data in the same manner as the example input:");

num_phrases = int(input())

for i in range(num_phrases):
    res = ""
    replacers = {}

    phrase = input()
    substitution_string = input().lower()

    for k in range(len(substitution_string) - 1):
        replacers[substitution_string[k]] = substitution_string[k+1]


    if len(substitution_string) % 2 == 1:
        res = "Wut"
        result.append(res)
        continue

    for c in phrase:
        if replacers.get(c.lower()) is not None:
            if c.isupper():
                res += replacers[c.lower()].upper()
            else:
                res += replacers[c]
        else:
            res += c
    
    result.append(res)

print("\n**********************\n")
for i in result:
    print(i)
