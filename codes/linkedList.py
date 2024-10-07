class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            currentNode = self.head
            while(currentNode.next != None):
                currentNode = currentNode.next
            currentNode.next = newNode

        
    def removeDuplicates(self, head=None):
        # code here
        # return head after editing list
        prev = self.head
        stack = []
        stack.append(prev.data)
        curr = self.head.next
        while curr is not None and prev is not None:
            while prev.data == curr.data and curr.next is not None:
                curr = curr.next
                prev.next = None
            if stack.count(curr.data)>0:
                pass
            else:
                stack.append(curr.data)
                prev.next = curr
            
            curr = curr.next
            prev = prev.next

        print(stack)      
        return self.head

    def printAll(self):
        currentNode = self.head
        while(currentNode):
            print(currentNode.data)
            currentNode = currentNode.next


llist = LinkedList()

llist.insertAtEnd(1);
llist.insertAtEnd(2);
llist.insertAtEnd(3);
llist.insertAtEnd(3);
llist.insertAtEnd(2);
llist.insertAtEnd(3);
llist.removeDuplicates();

llist.printAll();