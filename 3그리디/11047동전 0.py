N, K = map(int, input().split())
# 10번 엔터로 새로운 값들 받아서 list로 저장하기
coins = [int(input()) for _ in range(N)]
coins.sort(reverse = True)
count = 0
for coin in coins:
    # 등호가 들어가서는 안 돼!!!
    if coin > K:
        continue
    else:
        count += K // coin
        K %= coin
    if K == 0:
        break

print(count)