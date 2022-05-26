# 스택 = 박스 쌓기 (선입후출, 후입선출)
# 파이썬에서 스택 이용시 리스트 사용하기 - append(), pop() 
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])