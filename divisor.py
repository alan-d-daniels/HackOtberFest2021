def divisor(a):
    num=a
    print('Divisors of',num)
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=' ')
divisor(6)