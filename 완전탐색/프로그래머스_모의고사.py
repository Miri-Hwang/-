one_answers = []
two_answers = []
three_answers = []


def solution(answers):
    # 정답
    answer = answers
    # 수포자 답안지
    n = len(answer)
    # 채점표
    counts = [0, 0, 0]

    # 1번 답안 작성
    for i in range(1, 2001):
        for j in range(1, 6):
            if len(one_answers) != n:
                one_answers.append(j)

    # 2번 답안 작성
    for i in range(1, 1251):
        for j in range(1, 6):
            if j != 2 and len(two_answers) != n:
                two_answers.append(2)
                if len(two_answers) != n:
                    two_answers.append(j)

    # 3번 답안 작성
    for i in range(1, 1001):
        for j in [3, 1, 2, 4, 5]:
            if len(three_answers) == n:
                break
            else:
                three_answers.append(j)
                if len(three_answers) != n:
                    three_answers.append(j)

    # 개별 점수 확인
    for i in range(n):
        if answer[i] == one_answers[i]:
            counts[0] += 1

        if answer[i] == two_answers[i]:
            counts[1] += 1

        if answer[i] == three_answers[i]:
            counts[2] += 1

    # 등수
    counts_set = set(counts)
    final = []
    # 중복 점수가 없을 때
    if len(counts_set) == len(counts):
        final.append(counts.index(max(counts))+1)
        return final

    elif len(counts_set) != 1:
        for i in range(3):
            if max(counts_set) == counts[i]:
                final.append(i+1)
        return final

    elif len(counts_set) == 1:
        final = [1, 2, 3]
        return final
    else:
        final = [1, 2, 3]
        return final


print(three_answers, solution([1, 2, 3, 5, 8, 6, 9]))
