N = int(input())
numbers = []
for i in range(N):
    numbers += map(int, input().split()) # int로 바꿔줘야 함. 안 해서 틀렸음. 
numbers.sort()
for i in range(N):
    print(numbers[i])