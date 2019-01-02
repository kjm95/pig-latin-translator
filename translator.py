vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def piglatin(word):
    if len(word) == 1:
        return word + "way"
    else:
        if word[0] in vowels:
            return word + "ay"
        else:
            word = word[1:] + word[0]
            return piglatin(word)

while True:
    sentence = input("Type your sentence:")
    if sentence == "x":
        break

    split_sentence = sentence.split()

    translated_sentence = [piglatin(word) for word in split_sentence]

    print(" ".join(translated_sentence))
