def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear == SIZE -1) :
        return True
    else:
        return False
    
    
def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == -1) :
        return True
    else :
        return False
    
    
def enQUeue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print("큐가 꽉 찼습니다.")
        return
    
    rear += 1
    queue[rear] = data
    

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return
    
    front += 1
    data = queue[front]
    queue[front] = None
    
    return data


def peek() :                  # fornt + 1 위치의 데이터 확인
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return
    
    return queue[rear + 1]


SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == "__main__" :
    select = input("삽입(I)/ 추출(E)/ 확인(V)/ 종료(X) 중 하나를 선택: ")
    
    while (select != 'X' and select != 'x') :
        if (select == 'I' or select == 'i') :
            data = input("입력할 데이터: ")
            enQUeue(data)
            print("큐 상태: ", queue)
            
        elif (select == 'E' or select == 'e') :
            data = deQueue()
            print("추출된 데이터: ", data)
            print("큐 상태: ", queue)
            
        elif (select == 'V' or select == 'v') :
            data = peek()
            print("맨 앞 데이터: ", data)
           
        else :
            print("잘 못된 입력. 다시 입력하시오.")
            
        select = input("삽입(I)/ 추출(E)/ 확인(V)/ 종료(X) 중 하나를 선택: ")
        
    print("프로그램 종료")

    