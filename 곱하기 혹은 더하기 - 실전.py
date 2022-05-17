s = ''
result = 0
for num in s:
    print(num)
    # 이렇게 해버리면 첫 번째 숫자가 0이면 무슨 짓을 해서도 답은 0밖에 되지 않음
    if num == 0 or num == 1:
        result += int(num)
    else:
        result *= int(num)


data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)