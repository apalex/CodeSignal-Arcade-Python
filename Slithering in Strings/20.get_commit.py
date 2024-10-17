def solution(commit):
    return ''.join(x for x in commit if x.isalnum()).replace('0', '')
