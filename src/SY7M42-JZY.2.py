def solution(persons, seats):
    if not persons:
        return 0

    s = [[s, p, s - p] for s, p in zip(seats, persons)]
    vacancy = sum(i[2] for i in s)

    s.sort(key=lambda x: x[2])

    # print(s)
    # print(vacancy)

    l = len(seats)
    cars = l

    i = 0
    j = l - 1

    while i < l - 1 and j > 0:
        if s[j][2] >= 1:
            m = min(s[i][1], s[j][2])
            s[i][1] -= m
            i += 1
        else:
            j -= 1

    return len(list(filter(lambda x: x[1]> 0, s)))





if __name__ == '__main__':
    # P = [1, 4, 1]; S = [1,5,1]; print(solution(P, S))
    P = [4,4,2,4]; S = [5,5,2,5]; print(solution(P, S))
    P = [0,0,0,0]; S = [5,5,2,5]; print(solution(P, S))
    P = [2,3,4,2]; S = [2,5,7,2]; print(solution(P, S))
    P = [3,3,5]; S = [3,4,10]; print(solution(P, S))
