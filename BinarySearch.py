#https://docs.python.org/3/library/functions.html
#b-search, Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next is not None and current.next.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def binary_search(self, key):
        start = self.head
        end = None
        while start != end:
            mid = start
            mid_prev = None
            hop1 = start
            hop2 = start
            while hop2 is not end and hop2.next is not end:
                mid_prev = mid
                mid = mid.next
                hop2 = hop2.next.next
            if mid.data == key:
                return True
            elif mid.data < key:
                start = mid.next
            else:
                if mid_prev is None:
                    end = mid
                else:
                    end = mid_prev
        return False

# Driver code
llist = LinkedList()
data = [10, 20, 30, 40, 50]
for i in data:
    llist.sorted_insert(i)

key = 50
if llist.binary_search(key):
    print("Yes, the key is in the list.")
else:
    print("No, the key is not in the list.")
