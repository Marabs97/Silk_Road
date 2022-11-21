import time

# Task 1
ni = input("Please write your name: ")
print("Task 1: \nHello ", ni, "Welcome to assignment 1")


# Task 2
word = input("Task 2: \nPlease enter a word to be printed in reverse :")
char = ""
for i in word:
    char = i + char

print("Reversed word :", char)

# Task 3
fi_list = [0]

f1 = input("Task 3: \nPlease enter Fibonacci loop count: ")
f = int(f1)


def fibo(fibcount):
    n = 0
    n1 = 0
    n2 = 1
    while n < fibcount:
        if n <= 1:
            n3 = n
        else:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        print(n3)
        #    fi_list[n] = n3
        n = n + 1


fibo(f)
# print(fi_list)


# Task 4
upperbound = input("Task 4: enter the upper bound number (integer) to get the lower bound. "
                   "\n(except numbers that are dividable by 3)"
                   "\n:")
list1 = []
for i in range(int(upperbound)):
    if (i % 3) != 0:
        list1.append(i)

print(list1)



# Task 5

def trifunc(t1, t2, t3):
    val = True
    tri_sides = [t1, t2, t3]
    tri_sides.sort()
    print("Entered sides are :", tri_sides)
    if tri_sides[2] <= (tri_sides[0] + tri_sides[1]) or (tri_sides[0] == tri_sides[1] and tri_sides[0] == tri_sides[2]):
        print("Numbers Validated")
        val = False
        if tri_sides[0] == tri_sides[1] and tri_sides[0] == tri_sides[2]:
            print("this is a equilateral triangle.")
        elif tri_sides[0] == tri_sides[1] or tri_sides[0] == tri_sides[2] or tri_sides[1] == tri_sides[2]:
            print("this is a isosceles triangle.")
        else:
            print("this is a scalene triangle.")
    else:
        print("please enter valid numbers: ")
        val = True

    return val, tri_sides


validate = True
print("Please input side lengths of the triangle: ")
while validate:
    side1 = int(input())
    side2 = int(input())
    side3 = int(input())
    validate, tri_sides = trifunc(side1, side2, side3)



# Task 6

x = float(input("Task 6: \nPlease enter decimal number to be converted to Octal number: "))
limput = int(input("Please input the limit for decimal calculation: "))

listZ = []
listA = []


def dec_to_oct(d, lim):
    d2 = d
    while d > 8:
        rem = d % 8
        listA.append(int(rem))
        d = int(d / 8)

    listA.append(d)
    listA.reverse()

    le = 1
    while le < lim:
        decimal = float(float(d2) - int(d2))
        d2 = decimal * 8
        z = int(d2)
        listZ.append(z)
        le = le + 1

    def conv(integers):
        strings = [str(integer) for integer in integers]
        a_string = "".join(strings)
        an_integer = int(a_string)
        return an_integer

    num = conv(listA)
    r = (conv(listZ))
    dec = r / 10 ** len(listZ)

    fin = num + dec

    return fin


print(dec_to_oct(x, limput))

time.sleep(5)
