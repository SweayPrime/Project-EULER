def divisors(nb, extremum = False):
    divisors = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors

triangle = 3
i = 2
nb_divisors = 0
while nb_divisors < 500:

    i += 1
    triangle += i

    nb_divisors = len(divisors(triangle, True))
print(triangle)