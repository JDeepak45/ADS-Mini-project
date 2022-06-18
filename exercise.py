import gc
from multiprocessing import reduction
#exercisey
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):

        if self.last != None:
            return self.last

        newNode = Node(data)

        self.last = newNode

        self.last.next = self.last
        return self.last

    def addFront(self, data):

        if self.last == None:
            return self.addToEmpty(data)

        newNode = Node(data)

        newNode.next = self.last.next

        self.last.next = newNode

        return self.last

    def addEnd(self, data):
        if self.last == None:
            return self.addToEmpty(data)

        newNode = Node(data)

        newNode.next = self.last.next
        self.last.next = newNode

        self.last = newNode

        return self.last

    def addAfter(self, data, item):

        if self.last == None:
            return None

        newNode = Node(data)
        p = self.last.next
        while p:

            if p.data == item:

                newNode.next = p.next
                p.next = newNode

                if p == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print(item, "The given node is not present in the list")
                break

    def deleteNode(self, last, key):

        if last == None:
            return

        if (last).data == key and (last).next == last:

            last = None

        temp = last
        d = None

        if (last).data == key:
            while temp.next != last:
                temp = temp.next

            temp.next = (last).next
            last = temp.next

        while temp.next != last and temp.next.data != key:
            temp = temp.next

        if temp.next.data == key:
            d = temp.next
            temp.next = d.next

        return last

    def traverse(self):
        if self.last == None:
            print("The list is empty")
            return

        newNode = self.last.next
        while newNode:
            print(newNode.data, end=" ")
            newNode = newNode.next
            if newNode == self.last.next:
                break

	

#exercise function


def exercise(bmi,bmr):
    
    print("\n\n\t\t\t\t\tJOGGING or CYCLING or SKIPPING")
    print("\nBased on BMI")
    if bmi<18:
        print("under weight")
    elif bmi>=18 and bmi<=24:
        print("Healthy")
    else:
        print("Over weight")
    print("\nMaintanence Factor : ",1800)
    ex=input("\nENTER 1 for joggin 2 for cycling 3 for skipping")
    exer=abs((bmr-1700)+(bmr-2000))
    val=0
    if ex=='1':
        joggin=75
        val=exer//joggin
        print("Jog for atleast ",val,"km today")

    elif ex=='2':
        cycle=100
        val=exer//cycle
        print("Do cycling for atleast ",val,"km today")

    else:
        # per min
        skip=20
        val=exer//skip
        print("Skipping for atleast ",val,"mins today")
    
    return val
#food
def food(bmi,bmr):
    # node creation

    class Node:

        def __init__(self, data,calorie):
            self.data = data
            self.calorie=calorie
            self.next = None
            self.prev = None


    class DoublyLinkedList:

        def __init__(self):
            self.head = None
        def insert_front(self, data,cal):
            new_node = Node(data,cal)
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        def insert_after(self, prev_node, data,cal):
            if prev_node is None:
                print("previous node cannot be null")
                return
            new_node = Node(data,cal)
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node
            if new_node.next:
                new_node.next.prev = new_node
        def insert_end(self, data,cal):
            new_node = Node(data,cal)
            if self.head is None:
                self.head = new_node
                return
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

            return
        def deleteNode(self, dele):
            if self.head is None or dele is None:
                return
            if self.head == dele:
                self.head = dele.next
            if dele.next is not None:
                dele.next.prev = dele.prev
            if dele.prev is not None:
                dele.prev.next = dele.next
            gc.collect()
        def display_list(self, node):

            while node:
                print(node.data,node.calorie)
                last = node
                node = node.next
        #search
        def search(self,head,data):
            temp=head
            while temp:
                if temp.data==data:
                    return temp.calorie
                    
                temp = temp.next
            if temp==None:
                print("The given data doesnt exist:")
                return 0
            

    # initialize an empty node
    d_linked_list = DoublyLinkedList()
    m_linked_list = DoublyLinkedList()
    l_linked_list = DoublyLinkedList()

    d_linked_list.insert_end("Chaapati",71)
    d_linked_list.insert_end("Dosai",100)
    d_linked_list.insert_end("Idli",39)
    d_linked_list.insert_end("bread",70)
    d_linked_list.insert_end("dhal",120)
    d_linked_list.insert_end("chicken",250)
    d_linked_list.insert_end("mutton",154)
    d_linked_list.insert_end("chenna",719)
    d_linked_list.insert_end("soya",300)
    d_linked_list.insert_end("egg",78)


    #lunch
    l_linked_list.insert_end("chicken",250)
    l_linked_list.insert_end("mutton",154)
    l_linked_list.insert_end("fish",200)
    l_linked_list.insert_end("meals",150)
    l_linked_list.insert_end("veg_side_dish",120)
    l_linked_list.insert_end("egg",78)



    # morning
    m_linked_list.insert_end("chenna",719)
    m_linked_list.insert_end("chease",402)
    m_linked_list.insert_end("chease",402)
    m_linked_list.insert_end("Chaapati",71)
    m_linked_list.insert_end("Dosai",100)
    m_linked_list.insert_end("Idli",39)
    m_linked_list.insert_end("oats",300)
    m_linked_list.insert_end("dhal",120)



    print()
    food=input("\t\t\t\t\t  DIET PLAN\n\n\t\t\t\t\tBreakfast(1)\n\t\t\t\t\t  Lunch(2)\n\t\t\t\t\t dinner(3)\nEnter options(1,2,3):")
    

    print("Calories are described for 100grms")

    print("ENTER CALORIE INTAKE:",2000)
    q=0
    print()
    tt='y'
    items=[]
    ee='n'
    #2300d_linked_list.display_list(d_linked_list.head)
    print("ENTER THE FOODS U WANT IN AND THE COUNT for a day :")
    while q<2000 and tt=="y" and ee=='n':
        
        if food=='1':
            print("Breakfast")
            m_linked_list.display_list(m_linked_list.head)        
        elif food=="2":
            print("Lunch")
            l_linked_list.display_list(l_linked_list.head)
        else:
            print("Dinner")
            d_linked_list.display_list(d_linked_list.head)    
        v=input()
        qty=int(input("How many:="))
        
        if food==1:
            s=m_linked_list.search(m_linked_list.head,v)
        elif food==2:
            s=l_linked_list.search(l_linked_list.head,v)
        else:
            s=d_linked_list.search(d_linked_list.head,v)
        temp=q+(s*qty)
        if temp>bmr:
            t=input("Remove an food from list(Y/N): ")
            if t=='y':
                k=input()
                if food=='1':
                    s=m_linked_list.search(k)
                elif food=="2":
                    s=l_linked_list.search(k)
                else:
                    s=d_linked_list.search(k)
                print()
                ty=input("How much you wana remove: ")
                q-=s*ty
            else:
                tt=input("if Insuffiecency in nutrient(Y/N): ")
                
        else:
            q+=s*qty
            items.append(v)
        print("calories=",[q,qty])
        ee=input("Wanna stop (y/n):")
        food=input("\nbreakfast lunch dinner(1,2,3):")
    print("TOTAL CALORIE OF FOOD:=",q)
    print("food list:- ",items)  
class TreeNode:
    def __init__(self, data,password,bmr):
        self.data = data
        self.password=password
        self.bmr=bmr
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        # x is root
        if x.parent == None:
            self.root = y
        # x is left child
        elif x == x.parent.left:
            x.parent.left = y
        # x is right child
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        # x is root
        if x.parent == None:
            self.root = y
        # x is right child
        elif x == x.parent.right:
            x.parent.right = y
        # x is left child
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, n):
        # node is not root
        while n.parent != None:
            # node is child of root, one rotation
            if n.parent == self.root:
                if n == n.parent.left:
                    self.rightRotate(n.parent)
                else:
                    self.leftRotate(n.parent)

            else:
                p = n.parent
                g = p.parent  # grandparent

                if n.parent.left == n and p.parent.left == p:  # both are left children
                    self.rightRotate(g)
                    self.rightRotate(p)

                elif n.parent.right == n and p.parent.right == p:  # both are right children
                    self.leftRotate(g)
                    self.leftRotate(p)

                elif n.parent.right == n and p.parent.left == p:
                    self.leftRotate(p)
                    self.rightRotate(g)

                elif n.parent.left == n and p.parent.right == p:
                    self.rightRotate(p)
                    self.leftRotate(g)

    def insert(self, n):
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        n.parent = y

        if y == None:  # newly added node is root
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n

        self.splay(n)

    def bstSearch(self, n, x, y):
        if x == n.data and y==n.password:
            self.splay(n)
            print("Logged In")
            return n. bmr
        elif x < n.data:
            return self.bstSearch(n.left, x)
        elif x > n.data:
            return self.bstSearch(n.right, x)
        else:
            return None

    def preOrder(self, n):
        if n != None:
            print(n.data,n.password,n.bmr)
            self.preOrder(n.left)
            self.preOrder(n.right)


if __name__ == '__main__':

    tree = SplayTree()
    cll = CircularLinkedList()

    u="yes"
    print("\t\t\t\tWELCOME TO SSN MINI FITNESS APP")
    while(u=="yes"):
        new=input("IF NEW USER (Y/N): ")
        if new=='y':
            user_name=input("ENTER NAME: ")
            password=input("ENTER PASSWORD: ")
            recheck=input("ENTER PASSWORD AGAIN: ")
            while password!=recheck:
                print("WRONG PASSWORD")
                password=input("ENTER PASSWORD: ")
                recheck=input("ENTER PASSWORD AGAIN: ")
            heigh=int(input("ENTER HEGHT(cm): "))
            weight=int(input("ENTER WEIGHT(kg): "))
            age=int(input("ENTER AGE: "))
            bmi=weight//(heigh*heigh*0.0001)
            sex=input("ENTER SEX (MALE/FEMLAE): ")
            print("YOUR BMI IS ",bmi)
            pound_weight=int(weight*2.20462)

            if sex=="female":
                bmr=int(655+(9.563*weight )+(1.850*heigh)-(4.676*age))
            else:
                bmr=int(66.47+(13.75*weight) + (5.003*heigh)-(6.755*age))
            print("YOUR BMR: ",bmr)
            a = TreeNode(user_name,password,bmr)
            tree.insert(a)
            f=input("Diet plan(d) / Exercise(e)")
            if f=='d':
                food(bmi,bmr)
            else:
                goma=exercise(bmi,bmr)
                if goma!=0:
                    cll.addFront(goma)
                    vk=input("Wanna trace your routine:(y/n):")
                    if vk=='y':
                            cll.traverse()

        else:
            
            user_name=input("ENTER NAME: ")
            password=input("ENTER PASSWORD: ")
            bmr=tree.bstSearch(tree.root, user_name,password)
            if bmr==None:    
                print("Wrong password or wrong user name")
                user_name=input("ENTER NAME: ")
                password=input("ENTER PASSWORD: ")
                bmr=tree.bstSearch(tree.root, user_name,password)
            f=input("Diet plan(d) / Exercise(e)")
            if f=='d':
                food(bmi,bmr)
            else:
                goma=exercise(bmi,bmr)
                if goma!=0:
                    cll.addFront(goma)
                    vk=input("Wanna trace your routine:(y/n):")
                    if vk=='y':
                            cll.traverse()
        u=input("\n\n\t\t\t\tif you want to contniue (yes/no):")

