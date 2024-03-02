def count_words_in_file():
    file = open("text.txt", "r")
    content = file.read()

    words = content.split()

    return len(words)


print(count_words_in_file())
