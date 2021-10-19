def conc(starts, ends):
    final_array = []
    for s in starts:
        for e in ends:
            new_word = s + e
            final_array.append(new_word)
    return final_array


def no_fours(words):
    changed = False
    out_l = []
    for w in words:
        if len(w) == 4:
            w = w.strip(w[-1])
            changed = True
        w
        out_l.append(w)
    return out_l, changed


def combine_dicts(d1, d2):
    new_d = {}
    for k_1 in d1.keys():
        if k_1 in d2.keys():
            new_d.update({k_1: d1.get(k_1) + d2.get(k_1)})
        else:
            new_d.update({k_1: d1.get(k_1)})
    for k_2 in d2.keys():
        if k_2 not in d1.keys():
            new_d.update({k_2: d2.get(k_2)})
    return new_d


def collatz(n):
    if n >= 0:
        if n % 2 == 0:
            m = n//2
        else:
            m = int((3*n) + 1)
    return m


def count_collatz(n):
    i = 0
    while n != 1:
        n = collatz(n)
        i += 1
    return i
