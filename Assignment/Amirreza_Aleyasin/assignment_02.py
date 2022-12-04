# Task 01 – String Length
import random
import math

inp = input("Please enter a string to get it's length: ")


def custom_len(x):
    count = 0
    for i in x:
        count += 1
    return count


print(custom_len(inp))


# Task 2

def gen_rand(min, max, count):
    list_rand = [random.randrange(min, max) for i in range(count)]
    return list_rand


def custom_max(x):
    temp_max = 0
    for i in x:
        if i >= temp_max:
            temp_max = i
    return temp_max


rand_list = gen_rand(1, 100, 10)
print(rand_list)
print(custom_max(rand_list))


# Task 3


def char_freq(x):
    dict1 = {}
    for i in x:
        if i != " ":
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
    return dict1


print(char_freq("santa clause"))

# Task 4
tup_list = [tuple(gen_rand(1, 100, 3)) for i in range(10)]
print(type(tup_list))

sorted_tup_list = sorted(tup_list, key=lambda tup: tup[2])
print(sorted_tup_list)

# Task 5 & 6

string = str(input("please enter some brackets: "))


def check_bracks(str):
    bracks_left = ["(", "[", "{"]
    bracks_right = [")", "]", "}"]
    cache = []
    for i in str:
        if i in bracks_left:
            cache.append(i)

        elif i in bracks_right:
            # which brack is it?
            indx = bracks_right.index(i)
            # if index(cache[-1]) == index(brack_left[i])
            if cache:
                if cache[-1] == bracks_left[indx]:
                    cache.pop()
                else:
                    continue

    if not cache:
        state = "correct input."
    else:
        state = "Incorrect input"
    return state


print(check_bracks(string))


# Task 7

def queue():
    run_loop = True
    queue_list = []#["Initial String"]
    while run_loop:
        #if "Initial String" in queue_list:
        #    queue_list.clear()
        user_data = str(input("Please input your name to get in line"
                      "\n You can call in the next person by typing in the word 'Next' \n : "))
        if user_data == "Next":
            if queue_list:
                print("next person is :", queue_list[0])
                queue_list.pop(0)
            else:
                run_loop = False
        else:
            queue_list.append(user_data)
    return


queue()


# Task 8


def unlimited_power(x, n):
    if n == 0:
        return 1
    else:
        return x * unlimited_power(x, n - 1)


print(unlimited_power(2, 8))


# Task 9

#we have reached a threshold then:
    #we calculate the unlimited power of (x, n), divided by factorial(n)

def taylor_series(x, threshold=0.000001):
    temp = 1
    n = 0
    expon = 0
    state = True
    while state:
        temp = unlimited_power(x, n) / math.factorial(n)
        expon = expon + temp
        n += 1
        if temp < threshold:
            state = False
    return expon


print(taylor_series(3))
print(math.exp(3))
