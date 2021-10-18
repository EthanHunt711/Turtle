def conc(starts, ends):
    final_array = []
    for s in starts:
        for e in ends:
            new_word = s + e
            final_array.append(new_word)
    return final_array


def no_fours(words):
    for w in words:
        if len(w) == 4:
            w = w.strip(w[-1])
    return w