from collections import Counter
import re


filename = 'article.txt'

def word_stats(filename, n):
    words = re.findall(r'\w+',open(filename).read().lower())
    #print (words)
    #total_words= Counter(words)
    #print (total_words)
    common_words = (Counter(words).most_common(n))
    print (common_words)
    #for list in common_words:
        #print(list)
    for i in range(n):
        # print(n)
        # print(len(common_word))
        if n > len(common_words):
            print('Your input exceeds the number of words in the text file. Try again.')
            break
        else:
            print('"{}", "{}"'.format(common_words[i][0], common_words[i][1]))

word_stats(filename,10)