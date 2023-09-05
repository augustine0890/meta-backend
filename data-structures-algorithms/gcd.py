# Find the greatest common denominator of two numbers using Euclid's algorithm.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(60, 96)) # should be 12
print(gcd(20, 8)) # should be 4