N = int(input())
houses = list(map(int, input().split()))
answer = 0
houses.sort()
answer = houses[(N-1)//2]
print(answer)