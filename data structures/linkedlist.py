from http.client import NO_CONTENT


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def delete(self, data):
        temp = self.head
        if temp is None:
            return
        if temp == self.head:
            self.head = self.head.next
        else:
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    break
                temp = temp.next
            temp.next = temp.next.next

    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                print("found", temp.data)
                return True
            temp = temp.next
        print("not found")
        return False
    def length(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count


new_linked = linked()
new_linked.insert(1)
new_linked.insert(2)
new_linked.insert(3)
new_linked.insert(4)
new_linked.insert(5)
new_linked.insert(6)
new_linked.insert_at_end(7)
new_linked.print_list()
print("\n",new_linked.length())
