# 크기가 5인 스텍의 초기 상태(비어있는 상태)
stack = [None, None, None, None, None]
top = -1

# 크기가 5인 스텍의 생성과 데이터 3개 입력
stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = "커피"

top += 1
stack[top] = "녹차"

top += 1
stack[top] = "꿀물"

print("--- 스택 상태 ---")
for i in range(len(stack) - 1, -1, -1):
    print(stack[i])
    
# 스택에서 데이터 3개 추출
stack = ["커피", "녹차", "꿀물", None, None]
top = 2

print("--- 스택 상태 ---")
for i in range(len(stack) - 1, -1, -1):
    print(stack[i])
    
print("---------")
for i in range(3):
    data = stack[top]
    stack[top] = None
    top -= 1
    print("pop -->", data)
print("---------")

print("--- 스택 상태 ---")
for i in range(len(stack) - 1, -1, -1):
    print(stack[i])
    

