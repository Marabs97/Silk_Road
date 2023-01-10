'''
Task 01 – Lambda functions
Python supports lambda functions as a handy way to define small, anonymous, i.e., unnamed, functions inline. The basic syntax for lambda functions is:
lambda parameter1, parameter2, ... : expression
Use a lambda function only to retain the even values in an array of integers. Test your function with an input array of your choosing. Print the input array and the filtered output array to stdout.
'''

import numpy as np

array = np.array(range(100))

even = list(filter(lambda x: x % 2 == 0, array))
print(even)

'''
Task 02 – List comprehensions
Python supports list comprehension. The basic syntax of list comprehensions is:
L = [<elem> for <elem> <Condition>] 
Use list comprehensions to write a Python function remove_long_words() that:

accepts a sentence s and an integer n as input parameters
uses the split() function of String objects to split the sentence into words
stores the individual words in a list
removes all words that are longer than n characters from the list, thereby creating a new list
prints the list to stdout
'''


def remove_long_words(s, n):
    words = s.split()
    L = [x for x in words if len(x) <= n]
    return L


sentence = "Hello, this is a sentence with a REALREALLONGWORDTOBEREMOVED"
print(remove_long_words(sentence, 10))

'''
## Task 03 – Unity Test
The following algorithm in Python converts numbers in decimal representation to binary.
1. Develop a unit test that checks for values in the interval \[-1,3\] whether the algorithm returns the
expected results.
2. Adjust the algorithm, so it passes the unit test developed in 1). Rename the function to
*decimal_to_binary_correct()*
'''

import math


def decimal_to_binary_correct(n):
    # function to convert decimal integers to binary
    state = True
    x = []
    if n < 0:
        state = False
        n = abs(n)
    while n > 0:
        x.append(n % 2)
        n = math.floor(n / 2)

    rev = x[::-1]

    if not state:  # if negative

        rev.insert(0, '-')
        print("negative", rev)

    xs = "".join(map(str, rev))

    return xs


v = bin(420).replace("0b", "0")
print(decimal_to_binary_correct(420), v)

'''
Task 05 – Logging
The logging module in Python provides functionality for logging and debugging purposes. Use the logging module to extend the error handling for the function that you implemented to establish a HTTP connection (Task 4). All exceptions thrown by your function shall be logged as errors.

To accomplish the task:

write a Python function init_log(file_name, file_mode, level, format, date_format) that initializes a custom log file to which all debugging information and errors are appended using a format that includes the date, time, level and the message of the logging event
log occurring errors by calling logging.error(...)
close the log after completing your task by calling logging.shutdown()
If you choose not to complete Tasks 4, test the logging functionality with a few examples of your own.
'''

import logging


class CustomLog2:
    logfile = None

    def __init__(self, logfile):
        self.logfile = logfile
        self.config(logfile)

    def config(self, logfile):
        logging.basicConfig(level=logging.DEBUG, filemode='a', filename=logfile,
                            format='%(name)s - %(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


def init_log(filename):
    config = CustomLog2(filename)
    return config


'''
Task 04 – HTTP Request
Working with HTTP connections is essential for many data gathering tasks. The Python library urllib provides all functionality we need. Write a Python function open_url(url) that:

uses urllib to establish a HTTP connection to an arbitrary website
retrieves and prints the first 200 characters of the html resource, i.e. the html source code, of the chosen website
handles the exceptions thrown by the urllib.request function
'''

from urllib import request


def open_url(url):
    logs = CustomLog2("Task5_log.txt")

    try:
        link = request.urlopen(url)
        content = link.read()
        decoded = content.decode('utf8')
        link.close()
        logger1 = logging.getLogger("app area 1 (try)")
        logger1.info("OK. code running well")
        return decoded[:200]

    except OSError as err:
        print("OS Error: {0}".format(err))
        logger2 = logging.getLogger("expected errors")
        logger2.error("we have an error in OSError")
    except TypeError:
        print("object of inappropriate type")
        logger3 = logging.getLogger("expected errors")
        logger3.error("we have an error in TypeError")
    except ValueError:
        print("inappropriate value")
        logger4 = logging.getLogger("expected errors")
        logger4.error("we have an error in ValueError")
    except:
        print("Unexpected Error.")
        logger5 = logging.getLogger("unexpected errors")
        logger5.error("we have an unexpected error")

    logging.shutdown()


print(open_url('http://www.python.org'))

'''
Task 06 – Download File
In Task 4, you used the urllib library to establish a http connection. You can also use the urllib library to perform simple file downloads.

Write a Python function download_file(url, path) that:

checks whether the input URL points to a .txt file
if the input URL points to a .txt file, uses the urllib library to download and write the text file to the given path on your machine
logs an error “No text file found at given URL, download aborted!” to the log file created in Task 5 if the input URL does not point to a .txt file.
properly handles exceptions
Use the download_file() function to download William Shakespeare’s drama Macbeth as a plain text file from: Macbeth
'''

import os.path


def download_file(url, path):
    url_str = str(url)
    local_file = os.path.join(path, url_str[-10:-3] + '.txt')
    if not os.path.isdir(path):
        conf = input(f'entered path does not exist, do you want to create this path?  {path} \n'
                     f'type Yes if you want')
        if conf == 'Yes':
            os.mkdir(path)
        else:
            print("download aborted!")
            quit()
    try:
        if url_str[-4:] == '.txt':
            request.urlretrieve(url, local_file)
        else:
            raise "No text file found at given URL, download aborted!"

    except:
        raise "Unexpected error happened!"


download_file('https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt',
              "path")
