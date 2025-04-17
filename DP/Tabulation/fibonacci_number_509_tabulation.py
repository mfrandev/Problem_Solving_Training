def fib(self, n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    tab = [0] * (n + 1) # n + 1 because of 0-indexing
    tab[1] = 1
    for i in range(2, len(tab)):
        tab[i] = tab[i - 1] + tab[i - 2]
    return tab[len(tab) - 1]
