from nltk.corpus import gutenberg

emma = gutenberg.sents('austen-emma.txt')


def firstdict(corpus):
    firsts = {}
    for sent in corpus:
        first_word = sent[0].lower()
        if first_word in firsts:
            firsts[first_word] += 1
        else:
            firsts[first_word] = 1
    return firsts


def find_surprising(filename):
    corpus = gutenberg.sents(filename)
    freq1 = firstdict(corpus)
    for sent in corpus:
        if surprising():
            print(sent)


def surprising(corpus):
    short_sen = []
    for sen in corpus:
        if len(sen) <= 3:
            short_sen.append(sen)
    return True


find_surprising(emma)
