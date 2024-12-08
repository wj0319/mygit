from queue import Queue
from collections import deque
import random
import math


cnt = 0
cnt_move = 0

merge_cnt = 0
merge_cnt_move = 0

quick_cnt = 0
quick_cnt_move = 0

rad_cnt_move = 0

# 코드 7.1: 선택 정렬 알고리즘        참고 파일: ch07/basic_sort.py
def selection_sort(A) :
    global cnt
    global cnt_move

    n = len(A)
    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            if (A[j]<A[least]) :
                least = j
                cnt_move += 1
                
        A[i], A[least] = A[least], A[i]	    # 배열 항목 교환
        cnt = int((n*(n-1))/2)
    
        
# 코드 7.2: 삽입 정렬 알고리즘        참고 파일: ch07/basic_sort.py
def insertion_sort(A):
    global cnt
    global cnt_move
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0:
            cnt += 1
            if A[j] <= key:
                break  # 조건을 만족하면 더 이상 비교하지 않음
            A[j + 1] = A[j]
            j -= 1
            cnt_move += 1  # 데이터 이동 카운트
        A[j + 1] = key


# 코드 7.3: 버블 정렬 알고리즘        참고 파일: ch07/basic_sort.py
def bubble_sort(A):
    global cnt
    global cnt_move
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        cnt += 1  # 비교 연산 증가
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
                cnt_move += 1  # 데이터 이동 증가
        
        if not bChanged: break 

# 코드 12.1: 셸 정렬에 사용되는 삽입정렬 
# gap 만큼 떨어진 요소들을 삽입 정렬. 정렬의 범위는 first에서 last 
def sortGapInsertion(A, first, last, gap) :
    for i in range(first+gap, last+1, gap) :
        key = A[i]
        j = i - gap
        while j >= first and key<A[j] :
            A[j + gap] = A[j]
            j = j - gap
        A[j + gap] = key

# 코드 12.2: 셸 정렬 알고리즘
def shell_sort(A) :
    global cnt
    global cnt_move
    n = len(A)
    gap = n//2
    while gap > 0 :
        if (gap % 2) == 0 : gap += 1	# gap이 짝수이면 1을 더함
        cnt += 1 
        for i in range(gap) :
            sortGapInsertion(A, i, n - 1, gap)
            cnt_move += 1
        #print('     Gap=', gap, A)
        gap = gap//2

# 코드 12.4: 배열을 최대힙으로 바꾸는 heapify 함수
def heapify(arr, n, i):
    global cnt, cnt_move
    largest = i         # Initialize largest as root
    l = 2 * i + 1       # left = 2*i + 1
    r = 2 * i + 2       # right = 2*i + 2

    # 비교 연산 횟수 증가
    if l < n:
        cnt += 1
        if arr[i] < arr[l]:
            largest = l

    # 비교 연산 횟수 증가
    if r < n:
        cnt += 1
        if arr[largest] < arr[r]:
            largest = r

    if largest != i:
        # 데이터 이동 횟수 증가
        arr[i], arr[largest] = arr[largest], arr[i]
        cnt_move += 3  # swap involves 3 moves
        heapify(arr, n, largest)

def heapSort(arr):
    global cnt, cnt_move
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
        
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        cnt_move += 3  # swap involves 3 moves
        heapify(arr, i, 0)
        

sorted = [0]*100

def merge_sort(A, left, right):
    global merge_cnt
    global merge_cnt_move

    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)  # 왼쪽 부분 배열 정렬
        merge_sort(A, mid + 1, right)  # 오른쪽 부분 배열 정렬
        merge(A, left, mid, right)  # 병합 과정

def merge(A, left, mid, right):
    global sorted
    global merge_cnt
    global merge_cnt_move

    k = left  # 정렬된 배열의 인덱스
    i = left  # 왼쪽 부분 배열의 인덱스
    j = mid + 1  # 오른쪽 부분 배열의 인덱스

    # 두 부분 배열을 병합
    while i <= mid and j <= right:
        merge_cnt += 1  # 비교 연산 발생
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i += 1
        else:
            sorted[k] = A[j]
            j += 1
        k += 1
        merge_cnt_move += 1  # 데이터 이동 발생

    # 왼쪽 배열이 남아 있는 경우
    while i <= mid:
        sorted[k] = A[i]
        i += 1
        k += 1
        merge_cnt_move += 1  # 데이터 이동 발생

    # 오른쪽 배열이 남아 있는 경우
    while j <= right:
        sorted[k] = A[j]
        j += 1
        k += 1
        merge_cnt_move += 1  # 데이터 이동 발생

    # 병합된 결과를 원본 배열에 복사
    A[left:right + 1] = sorted[left:right + 1]
    merge_cnt_move += (right - left + 1)  # 복사 연산 발생
    

# 코드 12.8: 퀵 정렬
# 퀵 정렬 알고리즘을 이용해 배열의 left ~ right 항목들을 오름차순으로 정렬하는 함수
def quick_sort(array, start, end):
    global quick_cnt, quick_cnt_move
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end:
            quick_cnt += 1  # 비교 연산 카운트
            if array[left] > array[pivot]:
                break
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start:
            quick_cnt += 1  # 비교 연산 카운트
            if array[right] < array[pivot]:
                break
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
            quick_cnt_move += 2  # 데이터 이동 2번 (교환)
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
            quick_cnt_move += 2  # 데이터 이동 2번 (교환)
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def radix_sort(A):
    global rad_cnt_move
    rad_cnt_move = 0
    DIGITS = len(str(max(A)))
    BUCKETS = 10
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):  # 자릿수에 따라 큐에 삽입
            queues[(A[i] // factor) % BUCKETS].put(A[i])
            rad_cnt_move += 1  # 데이터를 큐에 삽입할 때 이동 카운트

        i = 0
        for b in range(BUCKETS):  # 버킷에서 꺼내어 리스트로 합친다
            while not queues[b].empty():
                A[i] = queues[b].get()
                rad_cnt_move += 1  # 큐에서 꺼내어 배열에 저장할 때 이동 카운트
                i += 1
        factor *= 10					    # 그 다음 자리수로 간다.

if __name__ == "__main__":
    data = list(map(int, input("Please input a data list : ").split(',')))
    print('-'*70)
    print("\t\t  [Target Sorting Algorithm List]")
    print()
    print("\tSelection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE),")
    print("\tHeap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")
    print('-'*70)
    while(1) :
        algorithm = input("Select sorting algorithm : ")

        if algorithm == "SEL":  #O
            selection_sort(data)
            print('-'*70)
            print("Sorted : ", end='')
            for i in range(len(data)):
                if i < len(data) - 1:
                    print(data[i], end=', ')
                else:
                    print(data[i])
            print("Number of Comparisons :",cnt)
            print("Number of Data movements :", cnt_move)
            print('-'*70)
            break

        elif algorithm == "INS":    #O
            insertion_sort(data)
            print('-'*70)
            print("Sorted : ", end='')
            for i in range(len(data)):
                if i < len(data) - 1:
                    print(data[i], end=', ')
                else:
                    print(data[i])
            print("Number of Comparisons :",cnt)
            print("Number of Data movements :", cnt_move)
            print('-'*70)
            break

        elif algorithm == "BUB":    #O
            bubble_sort(data)
            print('-'*70)
            print("Sorted : ", end='')
            for i in range(len(data)):
                if i < len(data) - 1:
                    print(data[i], end=', ')
                else:
                    print(data[i])
            print("Number of Comparisons :",cnt)
            print("Number of Data movements :", cnt_move)
            print('-'*70)
            break

        elif algorithm == "SHE":    #o
            shell_sort(data)
            print('-'*70)
            print("Sorted : ", end='')
            for i in range(len(data)):
                if i < len(data) - 1:
                    print(data[i], end=', ')
                else:
                    print(data[i])
            print("Number of Comparisons :",cnt)
            print("Number of Data movements :", cnt_move)
            print('-'*70)
            break

        elif algorithm == "HEA":
            heapSort(data)
            print('-'*70)
            print("Sorted : ", end='')
            for i in range(len(data)):
                if i < len(data) - 1:
                    print(data[i], end=', ')
                else:
                    print(data[i])
            print("Number of Comparisons :", cnt_move)
            print("Number of Data movements :", i)
            print('-'*70)
            break

        elif algorithm == "MER":    #O
            merge_sort(data, 0, len(data)-1)
            print('-'*70)
            print("Sorted : ", end='')
            for i in range(len(data)):
                if i < len(data) - 1:
                    print(data[i], end=', ')
                else:
                    print(data[i])
            print("Number of Comparisons :", merge_cnt)
            print("Number of Data movements :", merge_cnt_move)
            print('-'*70)
            break

        elif algorithm == "QUI":    #O
            quick_sort(data, 0, len(data)-1)
            print('-'*70)
            print("Sorted : ", end='')
            for i in range(len(data)):
                if i < len(data) - 1:
                    print(data[i], end=', ')
                else:
                    print(data[i])
            print("Number of Comparisons :", quick_cnt)
            print("Number of Data movements :", quick_cnt_move)
            print('-'*70)
            break

        elif algorithm == "RAD":    #o
            radix_sort(data)
            print('-'*70)
            print("Sorted : ", end='')
            for i in range(len(data)):
                if i < len(data) - 1:
                    print(data[i], end=', ')
                else:
                    print(data[i])
            print("Number of Comparisons : 0")      
            print("Number of Data movements :", rad_cnt_move)
            # rad_cnt_move : 큐에 삽입, 추출을 각각 이동 횟수로 계산함.
            print('-'*70)
            break

        else :
            print("Wrong Algorithm. Please try again.")
            continue