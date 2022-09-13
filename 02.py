'''
 * กลุ่มที่  : 22010118
 * 64010298 ไททัศน์ กันทา
 * chapter : 5	item : 2	ครั้งที่ : 0007
 * Assigned : Tuesday 30th of August 2022 09:44:25 AM --> Submission : Thursday 1st of September 2022 01:28:01 AM	
 * Elapsed time : 2383 minutes.
 * filename : 02.py
'''
class Node :
    def __init__(self, data, next = None, previous = None) :
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        else :
            s = ''
            p = self.head
            while p is not None:
                s += str(p.data) + " "
                p = p.next
            return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        
        cur = self.tail
        s = ''
        while cur != None:
            s += str(cur.data) + " "
            cur = cur.previous
        return s

    def isEmpty(self) :
        return self.head == None

    def append(self, data):
        p = Node(data)
        if self.head == None :
            self.head = p
            self.size = 1
        else :
            t = self.head
            self.tail = p
            while t.next != None :
                t = t.next
            t.next = self.tail
            self.tail.previous = t
            self.size += 1

    def addHead(self, data) :
        p = Node(data)
        if self.head == None :
            self.head = self.tail = p
            self.size += 1
        else :
            p.next = self.head
            self.head.previous = p
            self.head = p
            t = self.head
            while t.next is not None:
                t = t.next
            self.tail = t
            self.size += 1

    def insert(self ,pos, data) :
        if pos < 0:
            pos = self.size + pos
        p = Node(data)
        position = 0
        if pos == 0 or self.head == None or (pos*-1) > self.size - 1 :
            self.addHead(data)
        elif pos > self.size :
            self.append(data)
        else :
            t = self.head
            s = self.head
            while t != None :
                if position == pos - 1:
                    break
                t = t.next 
                position += 1
            
            position = 0
            while s != None :
                if position == pos:
                    break
                s = s.next 
                position += 1
            
            t.next = p
            p.next = s
            s.previous = p
            p.previous = t
            self.size += 1
            
    def search(self, data) :
        p = self.head
        while p is not None :
            if p.data == data :
                return 'Found'
            p = p.next
        return 'Not Found'
    
    def index(self, data):
        pos = 0
        t = self.head
        while t is not None :
            if t.data == data :
                return pos
            pos += 1
            t = t.next
        return -1
    def __len__(self):
        return self.size

    def pop(self, pos) :
        position = 0
        if pos >= self.size or pos < 0:
            return "Out of Range"
        else :
            if self.size > 1:
                t = self.head
                s = self.head
                while t != None :
                    if position == pos - 1:
                        break
                    t = t.next 
                    position += 1
            
                position = 0
                while s != None :
                    if position == pos:
                        break
                    s = s.next 
                    position += 1
            
                t.next = s.next
                self.size -= 1
                return 'Success'
            else :
                self.head = None
                self.size -= 1
                return 'Success'
            
    

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.__len__(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L.__str__())
print("Linked List Reverse :", L.reverse())
#print(L.tail.previous)


            

    