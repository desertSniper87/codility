# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    for i in range(max(A), min(A), -1):
        if i not in A and i > 0:
            return i

    return max(A) + 1 if max(A) > 0 else 1



if __name__ == '__main__':
    print(solution([1, 3, 6, 4, 1, 2]))
