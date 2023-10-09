result = []



print("Enter data in the same manner as the example input:");

num_phrases = int(input())

for i in range(num_phrases):
    res = ""
    words = []
    done = False

    phrase = input() 

    words = phrase.split()

    words.sort(key=lambda x: len(x))

    for k in range(len(words) - 1):
        if len(words[k]) == len(words[k + 1]):
            res = f"{words[k + 1]} and {words[k]} are the same length" 
            result.append(res)
            done = True
            break

    if done: continue

    for k in range(len(words) - 1):
        letter_set1 = {letter for letter in words[k] if letter.isalpha()}
        letter_set2 = letter_set = {letter for letter in words[k +1] if letter.isalpha()}

        if (letter_set1 <= letter_set2): # checks if letter_set1 is a subset of letter_set2
            continue
        else:
            missing = letter_set1 - letter_set2 # gets difference of sets
                                                # {t, a, c, k} - {t, r, a, c, e} = {k}
                                                
                                                # ^ what is in first set but not in second set

            res = f"{words[k + 1]} is missing {missing.pop()} (needed for {words[k]})"
            result.append(res)
            done = True
            break
    
    if done: continue

    result.append("yes")


for i in result:
    print(i)
    



        





