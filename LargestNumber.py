#!/usr/bin/python3
def dig(num):
    return (str(num)[0],sum([int(x) for x in str(num)]),-len(str(num)))
def main():
    n = int(input())
    a = sorted([int(x) for x in input().split()],key=dig,reverse=True)
    print(a)
    print(''.join(map(str,a)))

try:
    main()
except:
    print("Invalid Input")
