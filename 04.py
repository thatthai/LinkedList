class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList :
    def __init__(self, head = None):
        if head == None :
            self.head = None
            self.tail = None
            self.temp = None
            self.size = 0
        else :
            self.head = head
            self.tail = None
            self.temp = None
            self.size = 1

    def __str__(self):
            s = ''
            t = self.head
            while t.next is not None:
                s += str(t.data) + "->"
                t = t.next
            s += str(t.data)
            print(s)

    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
            self.size += 1
        else :
            t = self.head
            while t.next is not None :
                t = t.next
            t.next = p
            self.tail = p
            self.size += 1
    
    def set_next(self,current_node,next_node) :
        current_value = 0
        next_value = 0
        if self.size == 0 :
            print("Error! {list is empty}")
        elif self.size <= current_node :
            print("Error! {index not in length}:",str(current_node))
        elif self.size <= next_node :
            L.append(next_node)
            print("index not in length, append :",str(next_node))
        else :
            index = 0
            t = self.head
            n = None
            #หาตัวที่จะถูกชี้
            while t.next is not None :
                if index == next_node :
                    break
                index += 1
                t = t.next
            n = self.temp = t
            next_value = t.data
            #สั่งให้ตัวที่ชี้ไป
            index = 0
            p = self.head
            while p.next is not None :
                if index == current_node :
                    break
                p = p.next
                index += 1
            p.next = n
            current_value = p.data
            print("Set node.next complete!, index:value = {0}:{1} -> {2}:{3}".format(current_node,current_value,next_node,next_value))

    def check_loop(self) :
        t = self.head
        count = 0
        if self.size == 0 :
            print("No Loop")
            print("Empty")
        else :
            while t.next is not None:
                if count >= self.size :
                    print("Found Loop")
                    t.next = None
                    break
                t = t.next
                count += 1
            if count < self.size :
                print("No Loop")
                self.__str__()
                
        

    

L = LinkedList()
inp = input("Enter input : ").split(',')
current_node = 0
next_node = 0
for item in inp :
    if item[:1] == "A":
        L.append(item[2:])
        L.__str__()
    if item[:1] == "S" :
        L.set_next(int(item[2]),int(item[4]))
        
L.check_loop()

    
