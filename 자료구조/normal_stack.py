# 데이터 삽입 (push)    
def push(data) :
    global SIZE, stack, top
    if (top >= len(stack) - 1) :
        print("스텍이 꽉 찼습니다.")
        return
    
    top += 1
    stack[top] = data


# 데이터 추출 (pop)
def pop() :
    global SIZE, stack, top
    if (top == -1) :
        print("스텍이 비었습니다.")
        return None
    
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


# 스텍의 top 위치의 데이터를 확인하는 함수
def peek() :
    global SIZE, stack, top
    if (top == -1) :
        print("스텍이 비어있습니다")
        return None
    return stack[top]


SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

