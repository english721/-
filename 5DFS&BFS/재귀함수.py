def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 재귀의 최대 깊이를 초과했다.

# 재귀 함수의 종료
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

# 재귀함수의 수행은 스택 자료구조 이용
# 그렇기 때문에 종료한다는 메세지는 가장 나중에 들어간 99번째부터 시작하는 것임. 