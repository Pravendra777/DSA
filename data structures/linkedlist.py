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
        tem = self.head
        while tem.next is not None:
            tem = tem.next
        tem.next = new_node

    def print_list(self):
        tem = self.head
        while tem is not None:
            print(tem.data, end=" ")
            tem = tem.next

    def delete(self, data):
        tem = self.head
        if tem is None:
            return
        if tem == self.head:
            self.head = self.head.next
        else:
            tem = self.head
            while tem is not None:
                if tem.data == data:
                    break
                tem = tem.next
            tem.next = tem.next.next

    def search(self, data):
        tem = self.head
        while tem is not None:
            if tem.data == data:
                print("found", tem.data)
                return True
            tem = tem.next
        print("not found")
        return False


new_linked = linked()
new_linked.insert(1)
new_linked.insert(2)
new_linked.insert(3)
new_linked.insert(4)
new_linked.insert(5)
new_linked.insert(6)
new_linked.insert_at_end(7)
new_linked.print_list()
