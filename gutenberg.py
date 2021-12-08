from nltk.corpus import gutenberg


def firstdict(corpus):
    firsts = {}
    for sent in corpus:
        first_word = sent[0].lower()
        #if first_word.isalpha():
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
            print(f"{' '.join(sent[:-1])}{sent[-1]}")


def surprising(sent, freq1):
    surp = False
    if len(sent) >= 3:
        if sent[0] in freq1.keys():
            for word in sent[1:]:
                #if word.isalpha():
                if freq1[sent[0]] > freq1.get(word, 0):
                    surp = False
                else:
                    surp = True
    return surp


find_surprising('austen-emma.txt')
# find_surprising('blake-poems.txt')
