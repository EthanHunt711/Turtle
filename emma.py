from nltk.corpus import gutenberg

emma = gutenberg.sents('austen-emma.txt')


def print_sents_with_word(word):
    for s in emma:
        if word in s:
            print(s)


def find_shortest_sent(word):
    min_sen = []
    for s in emma:
        if word in s:
            min_sen.append(s)
            if len(min_sen) > 0:
                return min(min_sen)
        return None


def conc3(words):
    con_sen = []
    for i, s in enumerate(emma):
        if words in s:
            con_sen.append(s)
    for l in con_sen:
        print(f'{l[l.index(words)-3:l.index(words)+4]}')


def conc3_n(word):
    for sent in emma:
        if word in sent:
            index = sent.index(word)
            print(f'{sent[index-3:index+4]}')




