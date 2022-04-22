# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re

def solution(N):
    # write your code in Python 3.6
    b = f'{N:>0b}'
    try:
        return max(map(len, re.findall(r'(?=(1[0]+1))', b))) - 2
    except ValueError:
        return 0

if __name__ == '__main__':
    print(solution(32))
    print(solution(1041))
    print(solution(529))
    print(solution(20))
