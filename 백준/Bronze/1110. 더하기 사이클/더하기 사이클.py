def change(n):
    global _c
    n_ten = 0

    if n < 10:
        new_n = n + n * 10

    elif n < 100:
        new_n = n % 10 + n // 10

    _c += 1
    return n % 10 * 10 + new_n % 10


_n_init = int(input())

_n_present = 0
_c = 0
_n_present = change(_n_init)

while _n_init != _n_present:
    _n_present = change(_n_present)

print(_c)