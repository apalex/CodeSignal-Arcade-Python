def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        x, *res, y = res
    return res
