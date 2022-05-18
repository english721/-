while True:
    n = input() # 이 부분에서 변수를 선언해줘야 함 - while문에서 input()!=0 이런식으로 하면 뭔가 이상함
    if n == '0':
        break

    if n == n[::-1]:
        print('yes')
    else:
        print('no')

# while input() == '0':
#     input()