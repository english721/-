K, N = map(int, input().split())
lines = []
for i in range(K):
    lines.append(int(input()))

start, end = 1, max(lines)  # start를 0으로 하면 ZeroDivisionError발생
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for line in lines:
        total += line // mid
    
    if total < N:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
        
print(answer)

