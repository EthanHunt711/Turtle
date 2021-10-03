def digit_sum(d):
    total = 0
    for i in str(d):
        total = int(i) + total
    return total


def is_harshad(n):
    if n % digit_sum(n) == 0:
        return True
    return False


for i in range(1, 201):
    if is_harshad(i):
        print(i)