"""
Double Linked List
 - append
 - insert
 - remove
 - index_of
 - Permmettre d'initialiser la structure avec des parametres variables
 - support
    - len
    - bracket index

   None <- A <-> B <-> C <-> D -> None

"""
from typing import Any, Optional


class Node:
    def __init__(self, value: Any, next: Optional[Any] = None, prev: Optional[Any] = None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


class DoubleLinkedList:

    head: Node = None  # Last item
    tail: Node = None  # First item

    def __init__(self, *args):
        for arg in args:
            self.append(arg)

    def append(self, value: Any):
        if not self.tail and not self.head:
            self.tail = self.head = Node(value=value)
        else:
            self._set_head(value)

    def prepend(self, value):
        if not self.tail and not self.head:
            self.tail = self.head = Node(value=value)
        else:
            self._set_tail(value)

    def _set_head(self, value) -> None:
        node = Node(value=value, prev=self.head)
        self.head.next = node
        self.head = node

    def _set_tail(self, value):
        node = Node(value=value, next=self.tail)
        self.tail.prev = node
        self.tail = node

    def insert(self, index: int, value: Any):
        index = self._get_positive_index(index)

        if index != 0:
            current = self._get_node_at_index(index)
            current.prev.next = Node(
                value=value, prev=current.prev, next=current)
        else:
            self.prepend(value)

    def _delete_unique_node(self):
        self.tail = None
        self.head = None

    def _delete_tail(self):
        self.tail = self.tail.next
        self.tail.prev = None
        
    def _delete_head(self):
        self.head.prev.next = None
        self.head = self.head.prev

    
    def remove(self, index: int):
        index = self._get_positive_index(index)
        current = self._get_node_at_index(index)

        if not current.prev and not current.next:
            self._delete_unique_node()
            return
        
        if not current.prev:
            self._delete_tail()
            return
        
        if not current.next:
            self._delete_head()
            return
        
        if current:
            current.prev.next = current.next
            current.next.prev = current.prev


    def index_of(self, value: Any) -> int:
        iter_index = 0
        current = self.tail

        while current:
            if current.value == value:
                return iter_index
            iter_index +=1
            current = current.next

    def __getitem__(self, index: int) -> Any:
        return self._get_node_at_index(index).value

    def _get_node_at_index(self, index) -> Node:
        self._check_index(index)

        current = self.tail
        iter_index = 0

        while current:
            if iter_index == index:
                return current

            iter_index += 1
            current = current.next

    def _check_index(self, index):
        if not self.tail or len(self) <= index:
            raise IndexError(f'{index} is not a valid index')

    def _get_positive_index(self, index):
        if index < 0:
            return len(self) + index

        return index

    def __len__(self):
        current: Node = self.tail
        count = 0

        while current:
            count += 1
            current = current.next

        return count

    def __str__(self):
        if not self.tail:
            return ''

        return self._to_str()

    def _to_str(self):
        result: str = ''
        current: Node = self.tail

        while current:
            symbol = '<->' if current.next else '->'
            result += f'{current.value} {symbol} '
            current = current.next

        return result

if __name__ == '__main__':
    dll = DoubleLinkedList(1)
    dll.insert(-1, 'Nouveau')
    dll.remove(0)
    print(dll[0])
