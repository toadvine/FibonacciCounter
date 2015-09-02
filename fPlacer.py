__author__ = 'benjamin_sanchez'
# Cleaned up and expanded for code abbey


def main():
    aCount = int(input())
    fList = fibo(1000)
    answer = []
    for x in range(aCount):
        bNum = int(input())
        count = 0
        for x in fList:
            if x == bNum:
                answer.append(count)
            count += 1
    for x in answer:
        print(x, end=" ")

def fibo(count):
    a = 0
    b = 1
    fList = list()
    fList.append(a)
    fList.append(b)
    for x in range(count):
        a += b
        fList.append(a)
        b += a
        fList.append(b)
    return fList


main()
