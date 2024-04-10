# Basic operations
x=2
y=3
z=5

print(x+y) # 5
print(x-y) # -1
print(x*y) # 6
print(x/y) # 0.6666666666666666
print(x//y) # 0
print(x**y) # 8
print(x%y) # 2

repr('hello') # 'hello'
str('hello') # 'hello'
print('hello') # hello

print(1>2) # False
print(5.0==5) # True
print(5.0!=5) # False
print(5.0 is 5) # False
print(5.0 is not 5) # True

# x<y<z === x<y and y<z
print(x<y<z) # True

print(1==2<3) # False
print(1==2 and 2<3) # False

import math
print(math.sqrt(16)) # 4.0

print(math.floor(2.9)) # 2
print(math.floor(-2.9)) # -3

print(math.ceil(2.1)) # 3
print(math.ceil(-2.1)) # -2

print(math.trunc(2.9)) # 2 towards 0
print(math.trunc(-2.9)) # -2 towards 0

print(2+3j) # (2+3j) Complex number
print((2+3j)*2) # (4+6j) 

print(0o20) # 16
print(0xFF) # 255
print(0b1000) # 8
print(oct(16)) # 0o20
print(hex(255)) # 0xff
print(bin(8)) # 0b1000
print(int('20',8)) # 16

# Bitwise operations

print(5&3) # 1
print(5|3) # 7
print(5^3) # 6
print(~5) # -6
print(5<<1) # 10
print(5>>1) # 2

import random

print(random.random()) # 0.0<=x<1.0
print(random.randint(1,10)) # 1<=x<=10
print(random.randrange(1,10)) # 1<=x<10
print(random.choice([1,2,3,4,5])) # 1,2,3,4,5
print(random.choices([1,2,3,4,5],k=2)) # 2 random choices
print(random.shuffle([1,2,3,4,5])) # None


print(0.1+0.1+0.4) # 0.6000000000000001
print(0.1+0.1+0.1-0.3) # 5.551115123125783e-17 (0.00000000000000005551115123125783)

from decimal import Decimal

print(Decimal('0.1')+Decimal('0.1')+Decimal('0.4')) # 0.6
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')) # 0.0


from fractions import Fraction

print(Fraction(2,4)) # 1/2
print(Fraction(1,3)+Fraction(1,3)+Fraction(1,3)) # 1


# Set operations

a={1,2,3,4,5}

print(a | {3,4,5,6,7}) # {1, 2, 3, 4, 5, 6, 7}
print(a & {3,4,5,6,7}) # {3, 4, 5}
print(a - {3,4,5,6,7}) # {1, 2}
print(a ^ {3,4,5,6,7}) # {1, 2, 6, 7}
print(type(a)) # <class 'set'>
print(type({})) # <class 'dict'>


# Boolean operations

print(True and False) # False
print(True or False) # True
print(not True) # False
print(True==1) # True
print(False==0) # True
print(True is 1) # False
print(True+3) # 4



