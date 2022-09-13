class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList :
    def __init__(self,head = None):
        if head is None :
            self.head = None
            self.tail = None
            self.size = 0
        else :
            self.head = head
            self.tail = None
            self.size = 1

    def append(self,data) :
        p = Node(data)
        t = self.head
        if self.size == 0 :
            self.head = p
            self.size += 1
        else :
            while t.next is not None :
                t = t.next
            t.next = p
            self.tail = p
            self.size += 1


def createLL(LL):
    L = LinkedList()
    for item in LL :
        L.append(item)
    return L
def printLL(head):
    t = head.head
    s = ''
    while t.next is not None :
        s += str(t.__str__()) + ' '
        t = t.next
    
    return s + str(t.__str__())

def SIZE(head):
    t = head.head
    size = 0
    while t.next is not None:
        size += 1
        t = t.next
    size += 1
    return size

def scarmble(head, b, r, size):
    # Code Here
    #BottomUp
    p = head.head
    stop = int(size*(b/100))
    for i in range(stop-1):
        p = p.next
    head.tail.next = head.head
    head.head = p.next
    head.tail = p
    head.tail.next = None
    print("BottomUp {0:0.3f} % : {1}".format(b,printLL(head)))

    #Riffle
    temp = LinkedList()
    t = head.head
    stop = int(size*(r/100))
    if stop > 1 :
        for i in range(stop) :
            t = t.next
        while t is not None :
            temp.append(t.value)
            t = t.next
        s = head.head
        index = 0
        while s.next.value != temp.head.value :
            s = s.next
        head.tail = s
        s.next = None
        k = temp.head
        f = head.head
        while k is not None :
            if f.next is not None :
                c = Node(k.value)
                c.next = f.next
                f.next = c
                f = f.next.next
                k = k.next
            else :
                c = Node(k.value)
                f.next = c
                f = f.next
                k = k.next
            
    print("Riffle {0:0.3f} % : {1}".format(r,printLL(head)))
    #Deriffle
    
    if stop > 1 :
        s = head.head
        if temp.size <= size//2:
            index = temp.size
        else :
            index = size - temp.size
        for i in range(index) :
            s.next = s.next.next
            s = s.next
        t = head.tail
        s = temp.head
        if temp.size > 1 :
            while s.next is not None :
                t.next = s
                s = s.next
                t = t.next
        else :
            t.next = s
        head.tail = t.next
    print("Deriffle {0:0.3f} % : {1}".format(r,printLL(head)))
    #Debottomup
    p = head.head
    stop = size - int(size*(b/100))
    for i in range(stop-1):
        p = p.next
    head.tail.next = head.head
    head.head = p.next
    head.tail = p
    head.tail.next = None
    print("Debottomup {0:0.3f} % : {1}".format(b,printLL(head)))
    
inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)