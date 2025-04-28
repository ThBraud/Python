def fibonacci(n):
    a = 0
    b = 1
    n-=2
    while n > 0:
        n-= 1
        c = a + b 
        print (n, c)
        a=b
        b=c
    return c 
fibonacci(10)


