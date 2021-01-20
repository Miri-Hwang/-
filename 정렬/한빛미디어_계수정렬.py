# 이것이 코딩테스트다(나동빈 저)
# 6-6.py 계수 정렬 소스코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0]*(max(array)+1)  # [0,0,0,0,0,0,0,0,0,0]


for i in range(len(array)):  # i = 0,1,2,3,4,...,10
    count[array[i]] += 1

# count = [2,2,2,1,1,2,1,1,1,2]

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
