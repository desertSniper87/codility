def solution(A):
    A.sort()
    l = len(A)

    if l < 3:
        return 0

    for i in range(l - 1, 1, -1):
        if A[i - 1] + A[i - 2] > A[i]:
            return 1
    return 0

if __name__ == '__main__':
    s = [10,1,2,8,5,20]; print(solution(s))
    s = [1,2,3]; print(solution(s))
    s = [1,3,3]; print(solution(s))