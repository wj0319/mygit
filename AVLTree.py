from BinaryTree import *
from BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)

# 코드 9.14: AVL 트리의 LL회전     
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

# 코드 9.15: AVL 트리의 RR회전     
def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")


def delete_avl(root):
    if root is None:
        return None

    # 최소값을 찾기
    parent, node = None, root
    while node.left is not None:
        parent = node
        node = node.left

    # 최소값 삭제
    if parent is None:
        root = root.right
    else:
        # 최소값을 부모의 왼쪽 자식에서 삭제하고 오른쪽 자식으로 대체
        parent.left = node.right

    # 삭제 후 균형을 맞추기 위해 reBalance 호출
    return reBalance(root)

from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)




# 코드 9.20: AVL 트리 테스트 프로그램
if __name__ == "__main__":
    node = [7,8,9,2,1,5,3,6,4]
    # node = [0,1,2,3,4,5,6,7,8,9]

    print('-------------- 트리 생성 --------------')
    root = None
    for i in node :
        n = BSTNode(i)
        if root == None :
            root = n
        else :
           root = insert_avl(root, n)

        print("AVL(%d): "%i, end='')
        levelorder(root)
        print()

    print('-'*39)
    print('현재의 트리 : ', end='')
    levelorder(root)
    print()
    root = delete_avl(root)
    print('최소값 삭제 후 트리 : ', end='')
    levelorder(root)
    print()
    print('-'*39)
