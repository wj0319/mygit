
class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem 
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

# 코드 8.2: 이진트리의 전위순회
def preorder(n) :
    if n is not None :
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

# 코드 8.3: 이진트리의 중위순회
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

# 코드 8.4: 이진트리의 후위순회
def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')



def display(self, msg = 'BTSMap :', order=0):
      while True :
        order = int(input("[순회 방식 선택] 1.Inorder  2.Preorder  3.Postorder  4. stop => "))

        if order == 1:
            print('\n  In-Order : ', end='')
            inorder(root)
            print()

        elif order == 2:
            print('\n  Pre-Order : ', end='')
            preorder(root)
            print()

        elif order == 3:
            print('\n Post-Order : ', end='')
            postorder(root)
            print()

        elif order == 4:
            exit()

        else:
            print("\n  Wrong Number")
            print()
            continue
            
        print()
        break


if __name__ == "__main__":
    print("\n======= 이진트리 테스트 ===================================") 
    d = TNode('D', None, None)
    e = TNode('E', None, None)
    b = TNode('B', d, e)
    f = TNode('F', None, None)
    c = TNode('C', f, None)
    root = TNode('A', b, c)
    
    while True:
        display(root)
