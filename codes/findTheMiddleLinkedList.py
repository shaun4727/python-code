class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtTheEnd(self,data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return
        else:
            currentNode = self.head
            while(currentNode.next):
                currentNode = currentNode.next
            
            currentNode.next = newNode
    
    def printAll(self):
        for i in range(3):
            print(i)
        currentNode = self.head
        while(currentNode):
            print(currentNode.data)
            currentNode = currentNode.next

    def findTheMiddle(self):
        slow = self.head
        fast = self.head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        print(slow.data)


llist = LinkedList()

# llist.insertAtTheEnd(1)
# llist.insertAtTheEnd(2)
# llist.insertAtTheEnd(3)
# llist.insertAtTheEnd(4)
# llist.insertAtTheEnd(5)
# llist.insertAtTheEnd(6)

# llist.findTheMiddle()
llist.printAll()





