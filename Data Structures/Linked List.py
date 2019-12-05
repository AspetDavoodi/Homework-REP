
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def main():
    LL = LinkedList()

    LL.head = Node(1)
    second = Node(2)
    third = Node(3)

    LL.head.next = second
    second.next = third

    LL.printList()

main()