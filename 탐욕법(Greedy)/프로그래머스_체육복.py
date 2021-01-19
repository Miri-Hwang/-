def solution(n, lost, reserve):
    reserves = []
    # 여분이 있는 학생 중 도난 당한 학생 배열
    holding = []
    count = n

    #  여분이 있는 학생 중 도난 당한 학생을 찾자
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            holding.append(lost[i])

    # 도난 당한 학생 목록에서 여분 있는 학생을 빼자
    for i in range(len(holding)):
        if holding[i] in lost:
            lost.remove(holding[i])

    # 여분 있는 학생이 빌려줄 수 있는 학생의 번호 배열
    for i in reserve:
        if i == 1:
            reserves.append(i+1)
        elif i == n:
            reserves.append(i-1)

        else:
            reserves.append(i+1)
            reserves.append(i-1)

    # 전체 학생 수 - 체육복을 빌리지 못한 학생 수 (최종)
    for i in lost:
        if i in reserves:
            reserves.remove(i)
            if i+2 in reserves:
                reserves.remove(i+2)
            elif i-2 in reserves:
                reserves.remove(i-2)
        else:
            count -= 1

    return count


print(solution(5, [1, 2, 4, 5], [2, 3, 4]))
