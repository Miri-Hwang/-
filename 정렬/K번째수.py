# 프로그래머스
# https://programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        newarray = sorted(array[i-1:j])
        answer.append(newarray[k-1])
        print(newarray)
    return answer


print(solution(array, commands))
