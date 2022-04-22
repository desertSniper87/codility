def solution(A):
    l = len(A)
    A.sort()

    t = sum (A) / 2     # Target Pollution reduction and currently remaining target
    filters = 0

    i = l-1
    while i >= 0:
        filters += 1
        reduction = A[i] / 2
        A[i] = reduction

        t -= reduction
        if t <= 0:
            return filters

        if A[i-1] > A[i]:
            i -= 1

    return filters


if __name__ == '__main__':
    A = [5, 19, 8, 1]; print(solution(A))
    A = [10, 10]; print(solution(A))
    A = [3, 0, 5]; print(solution(A))
    A = []; print(solution(A))
    A = [100, 5558, 6995, 471]; print(solution(A))
    A = [1, 1]; print(solution(A))
    A = [1, 1, 1, 1, 1, 1, 1, 1, 1]; print(solution(A))
    A = [1 for _ in range(30000)]; print(solution(A))
