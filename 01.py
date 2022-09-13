class Node:
    def __init__(self, data, next = None) :
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next

class LinkedList:
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail =  None
            self.size = 0
        else :
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None :
                t = t.next
                self.size += 1
                self.tail = t

    def append(self, data):
        p = Node(data) #สร้าง Node ใหม่
        if self.head == None: #ถ้า linked-list ไม่มี Node เลย ให้ head เป็นตัวนี้
            self.head = p
        else : #ถ้าไม่ใช่ linked-list ว่าง
            t = self.head #กำหนด t เป็นหัว
            while t.next != None: #ทำจนกว่า t.next หรือที่อยู่ของ Node จะเท่ากับ None หรือก็คือไม่มี Node ถัดไป
                t = t.next
            t.next = p #t.next ตัวนี้เท่ากับ None คือไม่มีตัวถัดไปเลยให้ชี้ไปหา Node p
        self.size += 1 #เพิ่ม Size มา 1 เพราะมีเพิ่มมา 1  Node

    def addHead(self, head) :
        self.head = head
        t = self.head
        while t.next != None:
            t = t.next
        

    def insertAfter(self, i, q) : #q is node
        p = Node(i)
        p.next = q.next
        q.next = p

    def deleteAfter(self,q):
        q.next = q.next.next
        self.size -= 1

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p

    def remove(self, data):
        if self.head is None:
            return ''
        if self.head.data == data :
            self.head = self.head.next
            self.size -= 1
            return ""
        else :
            p = self.head
            while p.next is not None and p.next.data != data :
                p = p.next
        p.next = p.next.next
        self.size -= 1

    def search(self, data):
        p = self.head
        while p is not None:
            if p.data == data :
                return p
            p = p.next
        return None

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        s = ''
        p = self.head
        while p is not None:
            s += str(p.data)
            p = p.next
        return s

L = LinkedList()
inp = input(' *** Locomotive ***\nEnter Input : ').split()
print("Before : " + ' <- '.join(inp))
for item in inp :
    L.append(item)

for i in range(L.__len__()):
    if L.nodeAt(i).data == '0':
        L.addHead(L.nodeAt(i))
        break
    else :
        L.append(L.nodeAt(i).data)

print("After : "+" <- ".join(L.__str__()))



