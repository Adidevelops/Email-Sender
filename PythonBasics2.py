#Modules in python
# import math for mathematical functions
# import random for random number generation
# import os for operating system functions
# import sys for system functions
# import time for time functions
# import datetime for date and time functions
# import re for regular expressions
# import urllib.request for url functions
# import json for json functions
#import json for json functions
#import sqlite3 for database functions
#import statistics for statistics functions
#import requests for HHTP requests and web scraping functions
#import HTTp for HHTP requests and web scraping functions
import math
import sys
import argparse
from functools import reduce
def operations (a,b):
    return (math.sqrt(a**2+b**2))

# print(operations(2,2))
# name = sys.argv[1]                   #Takes the argument from the command line and stores it in name
# print ("Hello " + name)

# parser=argparse.ArgumentParser(description="Add a number")
# parser.add_argument("a",type=int,help="first number")
# parser.add_argument("b",type=int,help="second number")
# args=parser.parse_args()

# print(math.sqrt(args.a*args.b))

# Lambda Functions          they are anonymous functions which can be defined without a name
multiply = lambda a,b:a*b
print(multiply(2,2))

# Map, filter, reduce
# Map() function is useed to perform a partical operation or a function on a list . it returns an object
roomA=[1,343,4,55,6,3]
double = lambda a:a*2
result = list(map(double,roomA))
result1=list(map(lambda a:a**2,roomA))
print(result,result1)

# Filter() function is used to filter out the elements of the list based on a condition , A filtered list is returned based on the condition
roomB=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda a:a%2!=0,roomB))) #filter(checkifOdd,roomB)

# Reduce() function is used to reduce the elements of the list to a single value

expenses = [
  ('breakfast', 50),
  ('lunch', 100),
]
result = reduce(lambda a,b:a[1]+b[1],expenses)
print(result)

# Recursion is a function that calls itself infinite number of times. Example: Factorial
def factorial(n):
    if n==0:
        return 1 
    else:
        return n*factorial(n-1)
print(factorial(10))

#Decorators in python are functions that take another function as an argument and extends the behavior of the function without explicitly changing it
# basically used for logging , cache , authentication , etc.
# Exception handling in python is used by using try and except blocks also can raise exceptions and handle them
try :
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# pip - Python Index Package is used for installing third party modules in python 
# pip install requests