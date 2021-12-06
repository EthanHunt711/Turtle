from nltk.corpus import gutenberg


def firstdict(corpus):
    firsts = {}
    for sent in corpus:
        first_word = sent[0].lower()
        if first_word.isalpha():
            if first_word in firsts:
                firsts[first_word] += 1
            else:
                firsts[first_word] = 1
    return firsts


def find_surprising(filename):
    corpus = gutenberg.sents(filename)
    freq1 = firstdict(corpus)
    for sent in corpus:
        if surprising(sent, freq1):
            print(sent)


def surprising(sent, freq1):
    surp = False
    if len(sent) >= 3:
        if sent[0] in freq1.keys():
            for word in sent[1:]:
                if word in freq1.keys():
                    if freq1[sent[0]] < freq1[word]:
                        surp = True
                    else:
                        surp = False
    return surp


find_surprising('austen-emma.txt')
find_surprising('blake-poems.txt')
