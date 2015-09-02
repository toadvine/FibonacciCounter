__author__ = 'benjamin_sanchez'
import time  # needed for timing
# This script is for confirming this worked and performance isn't a concern

start = time.time()  # timing
print("We're going to calculate 1000 Fibonacci numbers now...")
a = 0
b = 1
fList = list()
fList.append(a)
fList.append(b)
for x in range(1000):
    a += b
    fList.append(a)
    b += a
    fList.append(b)
end = time.time()  # timing
print("It took this long to calculate 1000 iterations: ", (end - start))
print(fList)

