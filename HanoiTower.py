import time

def hanoi_tower(n, fr, tmp, to) :
    global cnt
    cnt += 1
    if (n == 1) :
        print("원판 1: %s --> %s" % (fr, to))
    else :
        hanoi_tower(n - 1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)


cnt = 0
n = int(input("높이를 입력하세요. : "))
start = time.time()
hanoi_tower(n, 'A', 'B', 'C')
end = time.time()

print("함수 호출 횟수 : %d" %cnt)
print("실행 시간 :", end - start,"초")
