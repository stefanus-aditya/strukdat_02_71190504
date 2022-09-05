import random
import timeit

def generate_list(n):
    bts_atas = n*100
    randomlist = random.sample(range(0,bts_atas),n)
    randomlist.sort()
    return randomlist

def fibonacci(x):
    bil1=1
    bil2=1
    for i in range (1,x):
        print(bil2)
        if ((i+1) % 5 == 0):
            print()
        c = bil2
        bil2 = bil2 + bil1
        bil1 = c

def fibonaci_rekursif(n):
    if n <= 1:
        return n
    else:
        return(fibonaci_rekursif(n-1) + fibonaci_rekursif(n-2))

x=10
print(fibonacci(x))

for i in range(1,10+1):
    data = generate_list(i)
    start = timeit.default_timer()
    hasil = fibonaci_rekursif(i)
    end = timeit.default_timer()
    print('fibonaci Ke - ', i, '= ', hasil,': ', end-start,' second')