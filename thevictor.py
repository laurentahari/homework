newdic = input('Enter file:')
victors = open(newdic, 'r')
words = {}
for line in victors:
    for word in line.split():
        words[word] = words.get(word,0) + 1
top_15 = sorted (list(words.items()), key=lambda x:x[1], reverse = True)
count = 0
for word, freq in top_15:
    if (count < 15):
        print (word, freq)
    count = count + 1
