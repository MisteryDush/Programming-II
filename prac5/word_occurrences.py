text = input("Text: ").split()
words = {}
for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
for word in sorted(words.keys()):
    print(f'{word:13} : {words[word]}')
