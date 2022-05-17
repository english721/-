N = int(input())
times = list(map(int, input().split()))
answer = 0

times.sort()
for i in range(N):
    answer += (N-i)*times[i]
print(answer)
