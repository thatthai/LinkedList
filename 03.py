class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkendList :
    def __init__(self,head = None):
        if head is None :
            self.head = self.tail = None
            self.size = 0
        else :
            self.head = head
            self.tail = None
            self.size = 1

    def append(self, data):
        p = Node(data)
        if self.head is None:
            self.head = p
            self.size += 1
        else :
            t = self.head
            while t.next is not None :
                t = t.next
            t.next = p
            self.tail = p
            self.tail.previous = t
            self.size += 1

    def __str__(self):
        s = ''
        t = self.head
        while t is not None:
            s += str(t.data)
            t = t.next
        print(s)
    
    def reverse(self) :
        s = ''
        t = self.head
        while t is not None:
            s += str(t.data)
            t = t.next
        print(s[::-1])

    def atNode(self,pos):
        t = self.head
        position = 0
        if pos >= self.size or pos < 0 :
            return "Out of Range"
        else :
            while position != pos and t.next is not None :
                t = t.next
                position += 1
            return t

    def crush(self):
        s = self.atNode(0)
        count = 1
        combo = 0
        i = 1
        while i < self.size :
            if s.data == self.atNode(i).data :
                count += 1
            else :
                s = self.atNode(i)
                count = 1
            #ถ้าครบ 3 ตัว
            if count == 3 :
                combo += 1
                if s == self.head and self.atNode(i).next is None:
                    self.head = None
                    self.size -= 3
                    count = 1
                    i = 0
                    
                elif self.head != s and self.atNode(i).next is None:
                    t = self.head
                    while t.next is not None :
                        if t.next == s:
                            t.next = None
                            self.size -= 3
                            i = 0
                            count = 1
                            break
                        t = t.next
                elif self.head == s :
                        self.head = self.atNode(i+1)
                        self.size -= 3
                        i = 0
                        count = 1
                else :
                    t = self.head
                    while t.next is not None:
                        if t.next == s :
                            t.next = self.atNode(i+1)
                            self.atNode(i+1).previous = t
                            self.size -= 3
                            i = 0
                            count = 1
                            break
                        t = t.next
                s = self.atNode(0)
                    
            i += 1
        if self.size == 0 :
            print(self.size)
            print("Empty")
            if combo > 1 :
                print("Combo : " + str(combo) + " ! ! !")
        else :
            print(self.size)
            self.reverse()
            if combo > 1 :
                print("Combo : " + str(combo) + " ! ! !")

##main##
L = LinkendList()
inp = input('Enter Input : ').split()
for item in inp :
    L.append(item)
##crush!!
L.crush()

