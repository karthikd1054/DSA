class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self,head):
        self.head = head

    def appendNode(self, newNode):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newNode            
        else:
            self.head = newNode

    def insertNode(self, position, newNode):
        current  = self.head
        previous = self.head
        i = 0
        if position == 1 and self.head != None:
            newNode = self.head
            self.head.next = newNode
        elif position == 1:
            self.head = newNode
        else:
            while i<position-1:
                previous = current
                current = current.next
                i = i+1
            previous.next = newNode
            newNode.next = current

    def searchValue(self, value):
        if self.head == None:
            print("Linked List is Empty")
            return 0
        else:
            if self.head.value == value:
                print(self.head.value)
            else:
                current = self.head
                i = 0
                while current.value != value:
                    current = current.next
                print(current.value)

    def searchNode(self, position):
        if self.head == None:
            print("Linked List is Empty")
            return 0
        else:
            current = self.head
            if position == 1:
                print("Value at Node "+str(position)+": "+self.head.value)
            else:
                i = 0
                while i<position:
                    if current.next:
                        current = current.next
                        i = i+1
                    else:
                        print("Node out of bound\n")
                        return 0
                print("Value at Node "+str(position)+": "+current.value)

    def printLL(self):
        if self.head:
            current = self.head
            print(current.value)
            while current.next:
                current = current.next
                print(current.value)
        else:
            print("Linked List is Empty")

    def deleteValue(self, value):
        current = self.head
        previous = self.head
        if self.head.value == value:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        else:
            while current.next !=None:
                if current.value == value:
                    previous.next = current.next
                    current.next = None
                    return 1
                else:
                    previous = current
                    current = current.next
                    if current.next == None and current.value == value:
                        previous.next = None
                        return 1
            print("Value not found\n")

    def deleteNode(self, position):
        current = self.head
        previous = self.head
        i = 0
        if position == 1:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        else:
            while i<position-1:
                previous = current
                current = current.next
                i = i+1
            previous.next = current.next
            current.next = None

    def clearLL(self):
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp.next = None

ll = LinkedList(None)

print("Test Linked Lists Implementation\n")

while True:
    inp = int(input("1.Append Node\n2.Insert Node\n3.Search by Value\n4.Search by Node\n5.Delete by Value\n6.Delete by Node\n7.Delete the Linked List\n8.Print Linked List\n**ENTER 0 TO EXIT**\n"))
    if inp == 1:
        ll.appendNode(Node(input("Enter the value to be appended\n")))
    elif inp == 2:
        ll.insertNode(int(input("Enter the position to insert the new Node\n")),Node(input("Enter the value to be inserted\n")))
    elif inp == 3:
        ll.searchValue(int(input("Enter the Value to be searched\n")))
    elif inp == 4:
        ll.searchNode(int(input("Enter the Node to be searched\n")))
    elif inp == 5:
        ll.deleteValue(input("Enter the Value to be deleted\n"))
    elif inp == 6:
        ll.deleteNode(int(input("Enter the Node to be delete\n")))
    elif inp == 7:
        ll.clearLL()
    elif inp == 8:
        ll.printLL()
    elif inp == 0:
        break
    else:
        print("\nPlease Enter a Valid Option\n")