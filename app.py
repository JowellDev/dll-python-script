class Node:
    def __init__(self, data):
        self.item = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self, *args):
        self.start_node = None
        for arg in args:
            self.append(arg)

    # Return double Linked List length
    def __len__(self):
        k = 0
        n = self.start_node

        if n is None:
            return 0
        else:
            k += 1
            while n.next is not None:
                k +=1
                n = n.next
            return k


    #Get an item with index
    def __getitem__(self, index: int):
        self._check_index_existance(index)
        
        self._check_if_list_is_empty()

        k = 0
        n = self.start_node

        while n is not None:
            if index == k:
                return n.item
            n = n.next
            k += 1
    
    #Set dll[index] value
    def __setitem__(self, index: int, data):
        self._check_index_existance(index)

        self._check_if_list_is_empty()

        k = 0
        n = self.start_node

        while n is not None:
            if index == k:
                n.item = data
            n = n.next
            k += 1
    

    def _check_if_list_is_empty(self):
        if self.start_node is None:
            print("Liste vide ! ")
            return
    

    def _check_index_existance(self, index: int):
        if index > self.__len__() or index < 0:
            raise IndexError('Index introuvable ❌')
    

    def _insert_first_element(self, data):
        new_node = Node(data)
        self.start_node = new_node
        return

    def _insert_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node
        return

    #Display DLL content
    def display(self):
        self._check_if_list_is_empty()
        
        while self.start_node is not None:
            print(self.start_node.item , " ")
            self.start_node = self.start_node.next

    # Insert to DLL beginnig
    def unshift(self, data):
        if self.start_node is None:
            self._insert_first_element(data)
        else:
            self._insert_to_start(data)

    # Insert to DLL end
    def append(self, data):
        if self.start_node is None:
            self._insert_first_element(data)
        else:
            n = self.start_node
            while n.next is not None:
                n = n.next
            new_node = Node(data)
            n.next = new_node
            new_node.prev = n

    # Insert to index[i] of DLL
    def insert(self, data, index: int):
        self._check_if_list_is_empty()

        k = 0
        n = self.start_node

        while n is not None:
            if k == 0 and index == k:
                self._insert_to_start(data)
            if index == k:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                n.prev.next = new_node
                return
            n = n.next
            k += 1

    # delete the first element of DLL
    def shift(self):
        self._check_if_list_is_empty()

        if self.start_node.next is None:
            self.start_node = None
            return

        self.start_node = self.start_node.next
        self.start_node.prev = None;


    # delete the last element of DLL
    def pop(self):
        if self.start_node is None:
            return
        
        if self.start_node.next is None:
            self.start_node = None
            return

        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None


    # delete the first element of DLL who correspond to data
    def remove(self, data):
        self._check_if_list_is_empty

        if self.start_node.next is None:
            if self.start_node.item == data:
                self.start_node = None
            else:
                print("Element introuvable ❌")
            return 

        if self.start_node.item == data:
            self.start_node = self.start_node.next
            self.start_node.prev = None
            return

        n = self.start_node
        while n.next is not None:
            if n.item == data:
                break;
            n = n.next

        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.item == data:
                n.prev.next = None
            else:
                print("Element introuvable ❌")


    # Get an item index
    def indexOf(self, data) -> int:
        k = 0
        n = self.start_node

        while n is not None:
            if n.item == data:
                return k
            k +=1
            n = n.next

    # Counter data occurance in dll
    def count(self, data) -> int:
        k = 0
        n = self.start_node

        while n is not None:
            if n.item == data:
                k += 1
            n = n.next
        return k


if __name__ == '__main__':
    maListe = DoubleLinkedList(3, 6, 87)
    maListe.display()