from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.__len__() < self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.current==None:
                self.current=self.storage.head
            while self.storage.head!=self.current:
                 self.storage.head=self.storage.head.next
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current=self.storage.head.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        start=self.storage.head
        while start:
            print(list_buffer_contents)
            list_buffer_contents=list_buffer_contents+[start.value]
            print(list_buffer_contents)
            start=start.next
            

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
