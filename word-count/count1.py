from collections import Counter


def word_stats(filename, n):

    with open(filename) as file:
        file_content = file.read()

    # separate the list into words
    str_list = file_content.lower().split()

    # Strip ending punctuation
    for word in range(len(str_list)):
        str_list[word] = str_list[word].strip('.,:;"?!%^*$')

    # count words
    c = Counter(str_list)
    answerlist = c.most_common(n)
    print (answerlist)

    for i in range(n):
        # print(n)
        # print(len(answerlist))
        if n > len(answerlist):
            print(
            'Your input exceeds the number of words in the text file. Try again.')
            break
        else:
            print('"{}", "{}"'.format(answerlist[i][0], answerlist[i][1]))


word_stats('article.txt', 10)  # in case n=10


