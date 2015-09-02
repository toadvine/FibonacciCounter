__author__ = 'benjamin_sanchez'
import time

start = time.time()
print("We're going to calculate 1000 Fibonacci numbers now...")
a = 0
b = 1
answer = list()
answer.append(a)
answer.append(b)
for x in range(1000):
    a += b
    answer.append(a)
    b += a
    answer.append(b)
end = time.time()
print("It took this long to calculate 1000 iterations: ", (end - start))
print(answer)
