import math

class l02():
    def e01():
        a1, a2 = [int(input()) for x in range(2)]

        print(a1+a2)


    def e02():
        a1, a2, a3 = [int(input()) for x in range(3)]

        print(a1*a2*a3)


    def e03():
        a1, a2, a3 = [int(input()) for x in range(3)]

        print([a1, a2, a3].count(0))


    def e04():
        a1, a2, a3, a4 = [int(input()) for x in range(4)]

        s = 0
        for a in a1, a2, a3, a4:
            if a % 2 == 0:
                s += a

        print(s)


    def e05():
        a, b = [int(input()) for x in range(2)]

        if a < b:
            print(a)
        elif b < a:
            print(b)
        else:
            print('Su rovnake.')


    def e06():
        i = [int(input()) for x in range(4)]

        print(max(i))


    def e07():
        x = int(input())
        if x % 2 == 1:
            a = [int(input()) for x in range(5)]
            if x == a[2]:
                s = 0
                p = 1
                for c in a:
                    s += c
                    p *= c
                print(s, p, sep='\n')


    def e08():
        for i in range(1,100,2):
            if i == 99:
                print(i)
            else:
                print(i, end=', ')


    def e09():
        print(sum(range(0,101,2)))


    def e10():
        n = int(input())

        print(sum(range(1,n+1,2)))


    def e11():
        print(sum([int(input()) for x in range(100)]))


    def e12():
        print(max([int(input()) for x in range(5)]))


    def e13():
        x = float(input())
        n = int(input())

        print(x**n)


    def e14():
        n = int(input())
        c = 0
        for i in range(n):
            if int(input())>50:
                c += 1
        
        print(c)


    def e15():
        a = int(input())
        b = int(input())

        s = 0
        p = 1
        for i in range(a, b+1):
            s += i
            p *= i

        print(s, p, sep='\n')


    def e16():
        n = int(input())

        if n == 3:
            p = 3
        elif n < 3:
            p = 'Take cisla neexistuju.'
        else:
            p = 1
            for i in range(3,n,3):
                p *= i

        print(p)


    def e17():
        n = int(input())
        a = [int(input()) for i in range(n)]

        print(min(a))
        print(max(a))


    def e18():
        a = float(input())

        e = a/(3**(1/2))

        print(e)
        print(e**3)
        print(6*(e**2))


    def e19():
        n = int(input())
        a = 0
        for i in range(n):
            a += float(input())/n

        print(a)


    def e20():
        a = int(input())
        p = True

        if a == 2 or a == 3:
            p = True
        elif a % 2 == 0 or a % 3 == 0:
            p = False
        else:
            for d in range(5, math.floor(a**(1/2))+1, 6):
                if a % d == 0 or a % (d+2) == 0:
                    p = False
                    break

        print(p)


    def e21():
        n = int(input())

        p = [x for x in range(2,n+1)]
        i = 0
        while p[i] <= n**(1/2):
            j = i+1
            while p[j-1] != p[-1]:
                if p[j] % p[i] == 0:
                    del p[j]
                else:
                    j += 1
            i += 1

        print(*p, sep=', ')
            

    def e22():
        n = int(input())
        s = 42
        while n != 42:
            s += n
            n = int(input())

        print(s)


# Na spustenie kódu konkrétnej úlohy volajte funkciu triedy "l02" s prefixom "e"
# a číslom úlohy v dvojcifernom formáte, bez parametrov. Napríklad teda pre
# úlohu 5 to bude "l02.e05()".
