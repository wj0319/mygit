from ArrayList import ArrayList
import pickle

# 배열구조의 리스트를 이용한 라인 편집기 프로그램
list = ArrayList(1000)
while True :
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, m-단어추출, l-파일읽기, s-저장, q-종료=> ")

    if command == 'i' :
        pos = int( input("  입력행 번호: ") )
        str = input("  입력행 내용: ")
        list.insert(pos, str)

    elif command == 'd' :
        pos = int( input("  삭제행 번호: ") )
        list.delete(pos)

    elif command == 'r' :
        pos = int( input("  변경행 번호: ") )
        str = input("  변경행 내용: ");
        list.replace(pos, str)

    elif command == 'p' :
        print('Line Editor')
        for line in range (list.size) :
            print('[%2d] '%line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q' : exit()

    elif command == 'l' :
        filename = input("  읽어들일 파일 이름: ")
        #filename = 'test.txt'
        infile = open(filename , "r")
        lines = infile.readlines();
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()

    elif command == 's' :
        filename = input("  저장할 파일 이름: ")
        #filename = 'test.txt'
        outfile = open(filename , "w")
        len = list.size
        for i in range(len) :
            outfile.write(list.getEntry(i)+'\n')
        outfile.close()

    elif command == 'm' :
        #공백문자로 단어 구분
        str = input(" 입력할 내용 : ")
        sentence = str.split(' ')
        dic = {}
        for word in sentence:
            #단어가 알파벳 또는 숫자로만 구성된 경우
            if word.isalnum():
                 #딕셔너리에 이미 있는 단어일 경우
                if word in dic:
                    dic[word] += 1
                #딕셔너리에 없는 단어일 경우
                else:
                    dic[word] = 1
            
        for word in dic:
            print('',word,':', dic[word])
        
        #dic.txt에 저장
        with open('dic.txt','wb') as f:
            pickle.dump(dic, f)