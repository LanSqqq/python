def gcd(a,b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a,b)
a=int(input())
b=int (input())
print(gcd( x,y))