words_for_counting = {}

number_of_words = input("Text: ")
words = number_of_words.split()
for word in words:
    frequency = words_for_counting.get(word, 0)
    words_for_counting[word] = frequency + 1

words = list(words_for_counting.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, words_for_counting[word]))

