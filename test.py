str = "mono moons moroseness someones overnumerousness moo enormousnes"

words = str.split()

print(words)

words.sort(key=lambda x: len(x))

print(words)