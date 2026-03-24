"""Week 3 homework: The Royal Rail Ledger."""

from __future__ import annotations


class SLLNode:
    def __init__(self, value: int, next: "SLLNode | None" = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: SLLNode | None = None


class DLLNode:
    def __init__(
        self,
        value: int,
        prev: "DLLNode | None" = None,
        next: "DLLNode | None" = None,
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: DLLNode | None = None
        self.tail: DLLNode | None = None


# ================================
# Build SLL from list
# ================================
def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    sll = SinglyLinkedList()
    
    if not values:
        return sll

    sll.head = SLLNode(values[0])
    current = sll.head

    for value in values[1:]:
        current.next = SLLNode(value)
        current = current.next

    return sll


# ================================
# Convert SLL to Python list
# ================================
def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    result = []
    current = sll.head

    while current:
        result.append(current.value)
        current = current.next

    return result


# ================================
# Find first repeated value
# ================================
def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    seen = set()
    current = sll.head

    while current:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next

    return None


# ================================
# Remove all nodes from DLL
# ================================
def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    current = dll.head

    while current:
        next_node = current.next

        if current.value == target:
            # If it's head
            if current.prev is None:
                dll.head = current.next
                if dll.head:
                    dll.head.prev = None
            else:
                current.prev.next = current.next

            # If it's tail
            if current.next is None:
                dll.tail = current.prev
                if dll.tail:
                    dll.tail.next = None
            else:
                current.next.prev = current.prev

        current = next_node


# ================================
# Check palindrome DLL
# ================================
def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    left = dll.head
    right = dll.tail

    while left and right and left != right and left.prev != right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev

    return True