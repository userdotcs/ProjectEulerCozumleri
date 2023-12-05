def gcd(a, b): # Greatest Common Divider
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b): # Least Common Muliple
    return a * b // gcd(a, b)

n = 1000
print(n // 3 + n // 5 - n // lcm(3, 5))