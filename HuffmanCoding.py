def heappush(heap, n) :
    heap.append(n)		    
    i = len(heap)-1			
    while i != 1 :          
        pi = i//2           
        if n >= heap[pi]:   
            break
        heap[i] = heap[pi]	
        i = pi			    
    heap[i] = n			    

def heappop(heap) :
    size = len(heap) - 1    
    if size == 0 :         
       return None

    root = heap[1]		    
    last = heap[size]	    
    pi = 1                  
    i = 2                   

    while (i <= size):	    
        if i<size and heap[i] > heap[i+1]: 
            i += 1          
        if last <= heap[i]: 
            break
        heap[pi] = heap[i]  
        pi = i              
        i *= 2

    heap[pi] = last	       
    heap.pop()		        
    return root			    


def make_tree(freq) :
    heap = [0]
    for n in freq :
        heappush(heap, n)
    for i in range(1, len(freq)) :
        e1 = heappop(heap)      
        e2 = heappop(heap)
        heappush(heap, e1 + e2)
        print(("(%d + %d)" %(e1, e2)))


sum1 = 0
sum2 = 0

while True:
    label = {'k': 10, 'o': 5, 'r': 2, 'e': 15, 'a': 18, 't': 4, 'c': 7, 'h': 11}

    all_codes = {'k': '010' , 'o': '011', 'r': '10011', 'e': '00', 'a': '11', 't': '10010', 'c': '011', 'h': '101'}

    freq = []   # 입력한 글자의 빈도수를 저장하는 배열
    code = []   # 입력한 글자의 비트 열을 저장하는 배열

    result = {}
    #chars = ['k','o','r','e','a','t','c','h']
    #freqs = [10, 5, 2, 15, 18, 4, 7, 11]

    word = input("Please a word : ")

    # 입력한 글자의 빈도수 저장
    for char in word:
        if char in label :
            freq.append(label[char])
    
    if char not in label:
        print('illegal character')
        continue

    # 입력한 글자의 비트 열 저장
    for char in word:
        if char in label:
            code.append(all_codes[char])
    
    # 입력한 글자와 비트 열을 하나의 딕셔너리로 지정
    result = dict(zip(freq, code))
    
    #인코딩 후 비트 수
    for key, value in result.items():
        sum1 += key * len(value)
    
    #인코딩 전 비트 수
    for i in range(len(freq)):
        sum2 += freq[i] * 7

    #압축률 계산
    compressibility = (sum1 / sum2) * 100

    #허프만 트리
    make_tree(freq)

    #비트 열 출력
    print('결과 비트 열 : ', end="")
    for i in range(len(code)):
        print(code[i], end="")
                   
    print('')    
    print(f"압축률 : {compressibility:.2f}%")

    break

    