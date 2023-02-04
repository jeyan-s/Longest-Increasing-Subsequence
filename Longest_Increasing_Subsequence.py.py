from bisect import bisect_left as search

def solve(n, lst):
    lis = []
    k = 0
    for x in lst:
        index = search(lis, x)
        if index == k:
            lis.append(x)
            k += 1
        else:
            lis[index] = x
        print(x)
    return len(lis)

n = int(input())
lst = list(map(int, input().split()))
rslt = solve(n, lst)
