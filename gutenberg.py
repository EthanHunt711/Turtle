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
        if surprising(sent, freq1) is True:
            print(f"{' '.join(sent[:-1])}{sent[-1]}")


def surprising(sent, freq1):
    surprising_sent = False
    freq_list = []
    if len(sent) >= 3:
        if sent[0].isalpha():
            for word in sent:
                if word.isalpha():
                    freq_list.append(freq1.get(word.lower(), 0))
            if freq_list[0] < min(freq_list[1:]):
                surprising_sent = True
            else:
                surprising_sent = False
    return surprising_sent


find_surprising('austen-emma.txt')
# find_surprising('chesterton-ball.txt')
