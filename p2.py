




a=1
b=1
sum=0
while b <= 4000000:
    t=b
    b=a+b
    a=t

    if b%2 == 0:
        sum=sum+b
print(sum)

