def solution(message, K):
    l = len(message)
    if l < K:
        return message

    message_split = message[:K+1]
    rightmost_space_position = message_split.rfind(' ')
    return message_split[:rightmost_space_position].strip()




if __name__ == '__main__':
    m = 'Why not'; k = 100; print(solution(m, k))
    m = 'Codility We test coders'; k = 14; print(solution(m, k))
    m = 'The quick brown fox jumps over the lazy dog'; k = 39; print(solution(m, k))
    m = 'To crop or not to crop'; k = 21; print(solution(m, k))
    m = ''; k = 21; print(solution(m, k))
    m = 'You can use rfind() '; k = 14; print(solution(m, k))