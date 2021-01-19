# 이것이 코딩테스트다(나동빈 저)
# 6-1.py 선택 정렬 소스코드
# 추가 공부 내용 : https://1y9u9j2in.tistory.com/152


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # i : 0,1,2, ...,9

    for j in range(i+1, len(array)):
        # j : 1, 2, ... , 9
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]


print(array)
