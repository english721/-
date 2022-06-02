import sys
input = sys.stdin.readline

# input 받을 때 꼭 써주자!

N, M = map(int, input().split())
trees = list(map(int, input().split())) 
answer = 0

start, end = 0, max(trees)
while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree >= mid:
            total += tree-mid
    if total < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)