def max_chain(words):
    words = sorted(words, key=len)
    word_dict = {}
    for word in words:
        word_dict[word] = 1

    for word in words:
        for i in range(len(word)):
            delete_word_elem = word[:i] + word[i + 1:]
            if delete_word_elem in word_dict:
                word_dict[word] = max(word_dict[word], word_dict[delete_word_elem] + 1)

    max_word = max(word_dict)

    return max_word if len(max_word) == 1 else max(word_dict.values())


with open('../test/wchain2.in', 'r') as file:
    next(file)
    words = [line.strip() for line in file.readlines()]

result = max_chain(words)

with open('../test/wchain.out', 'w') as file:
    file.write(str(result))
