from nltk.corpus import gutenberg

emma = gutenberg.sents('austen-emma.txt')


def print_sents_with_word(word):
    p = 0
    for w in emma[p]:
        p += 1
        if w == word:
            print(w)


def find_shortest_sent(word):
    p = 0
    for word in emma[p]:
        if len(emma[p]) < len(emma(p+1)):
            return emma[p]
    return None



