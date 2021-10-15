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


def conc3(word):
    for sent in emma:
        if word in sent:
            for i, w in enumerate(sent):
                if w == word:
                    if i > 2:
                        print(f'{sent[i - 3:i + 4]}')
                    else:
                        print(f'{sent[i - i:i + 4]}')




