def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def gcd2(a, b):
    if a == 0:
        return b
    return gcd2(b % a, a)

# print(gcd(28, 12))

print(gcd2(24*79, 24*50))
