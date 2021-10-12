from nltk.corpus import gutenberg

emma = gutenberg.sents('austen-emma.txt')


def print_sents_with_word(word):
    for m in emma:
        if word in m:
            print(m)


def find_shortest_sent(word):
    p = 0
    for word in emma[p]:
        if len(emma[p]) < len(emma(p+1)):
            return emma[p]
    return None


print_sents_with_word('the')
