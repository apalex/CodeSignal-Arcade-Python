def solution(ids, k):
    digitSum = lambda q: sum(int (x) for x in str(q))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
