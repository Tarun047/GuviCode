#!/usr/bin/python3
from collections import Counter
def main():
    n = int(input())
    a = Counter([int(x) for x in input().split()])
    #print(a)
    ans = []
    for x in a:
        if a[x]>1:
            ans.append(str(x))
    if not ans:
        print("unique")
    else:
        print(' '.join(ans))


try:
    main()
except:
    print("Invalid Input")
