# ProjectEulerCozumleri

## Problem 1
Bu tarz problemlerde sonuç n(bu soruda 1000), a(bu soruda 3) ve b(bu soruda 5)'e tek tek böldükten sonra sonuçtan EKOK(a,b)'yi çıkararak elde ederiz.
EKOK bulmak için öncelikle EBOB bulmamız gerekir. Bunun için Euclidean Algorithm kullanırız.
```
def gcd(a, b): # Greatest Common Divider
    if a == 0:
        return b
    return gcd(b % a, a)
```
İki sayının çarpımını EBOB'larına bölersek EKOK'u elde ederiz.
```
def lcm(a, b): # Least Common Muliple
    return a * b // gcd(a, b)
```
Sonucumuz.
```
n = 1000
print(n // 3 + n // 5 - n // lcm(3, 5))
```

## Problem 2
Serinin 1. terimini 1, 2. terimini 2 alarak, Fibonacci dizisindeki çift sayıların toplamını basit bir while döngüsü ile bulabiliriz.
```
total = 2 # Baslangictaki b değerini saymadıgı için 2'den baslatiriz
a = 1
b = 2
while b < 4000000:
    a, b = b, a + b
    if b % 2 == 0: total += b
print(total)
```

## Problem 3
Bu problem için öncelikle bir asal sayı kontrol algoritmasına ihtiyacımız var.
```
def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return True
```
Ardından en büyük asal böleni bulabilecek bir algoritmaya ihtiyacımız var. Bunun için bir sayıyı bölünebildiği kadar en küçük asaldan başlayarak teker teker bölerek ilerlemeliyiz, ta ki kalan sayı 1 olana kadar.
```
def largest_prime(n):
    if is_prime(n): return n
    m = 0
    cP = 2
    while n != 1:
        while n % cP == 0: n //= cP
        m = cP
        cP += 1
        while not is_prime(cP) and n % cP != 0: cP += 1
    return m
```
Sonucumuzuz.
```
def largest_prime(n):
    if is_prime(n): return n
    m = 0
    cP = 2
    while n != 1:
        while n % cP == 0: n //= cP
        m = cP
        cP += 1
        while not is_prime(cP) and n % cP != 0: cP += 1
    return m
```

## Problem 4
Bunun için iç içe geçmiş iki tane for döngüsü ile brute force uygulayabiliriz.
```
m = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if str(i * j) == str(i * j)[::-1]:
            if m < i * j: m = i * j
print(m)
```

## Problem 5
Bunun için Problem 1'de kullandığımız GCD ve LCM algoritmalarını kullanabiliriz. Eğer 1'den 20'ye kadar olan sayıları sırasıyla EKOK'unu alırsak 1'den 20'ye kadar olan sayılara bölünen en küçük sayıyı, yani EKOK'larını bulabiliriz.
```
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return a * b // gcd(a, b)

n = 2
for i in range(3, 21): n = lcm(i, n)
print(n)
```
