# 실패
N = int(input())
X, Y = 1, 1
direction = 'RRRUDD'
# 이렇게 하면 공간밖이어도 나갔다가 다시 들어오게 됨. (3,4) 대신 (2,4)가 출력됨
while (X, Y >=1) and (X, Y <=N):
    for dir in direction:
        if dir == 'R':
            Y+=1
        if dir == 'L':
            Y-=1
        if dir == 'U':
            X-=1
        if dir == 'D':
            X+=1
    break


# 답안 예시
# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)