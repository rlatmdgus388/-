# 크기가 5칸인 큐의 생성과 데이터 3개 입력
queue = [None, None, None, None, None]
front = rear = -1

rear += 1
queue[rear] = "화사"

rear += 1
queue[rear] = "솔라"

rear += 1
queue[rear] = "문별"

print("--- 큐 상태 ---")
print('[출구] <--', end=' ')
for i in range(0, len(queue), 1) :
    print(queue[i], end = ' ')
print('<--[입구]')


# 큐에서 데이터 3개 추출
queue = ["화사", "솔라", "문별", None, None]
front = -1
rear = 2

print("---큐 상태---")
print("[출구] <--", end = ' ')
for i in range(0, len(queue)) :
    print(queue[i], end = ' ')