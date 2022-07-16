# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    l = len(A)
    ret_arr = [-1 for _ in range(l)]

    for i in range(l):
        ret_arr[(i+K)%l] = A[i]
    return ret_arr

A = [3, 8, 9, 7, 6]
K = 3

print(solution(A, K))