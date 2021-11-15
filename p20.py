"""


n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""
def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
def digit_sum(n):
    sum=0
    for i in str(n):
        print(i)
        sum=sum+int(i)
    return sum

print(digit_sum(fac(100)))
