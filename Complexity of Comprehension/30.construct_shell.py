def solution(n):
    return [[0 for x in range(y+1)] for y in range (n-1)] + [[0 for x in range(y+1)] for y in range (n)][::-1]
