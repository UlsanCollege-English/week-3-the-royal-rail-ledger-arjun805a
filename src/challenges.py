"""Week 3 homework: The Royal Rail Ledger.

Implement the required functions below.
Use stdlib only.
"""

from __future__ import annotations


class SLLNode:
    """Node for a singly linked list."""

    def __init__(self, value: int, next: "SLLNode | None" = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    """Simple singly linked list with a head reference."""

    def __init__(self) -> None:
        self.head: SLLNode | None = None


class DLLNode:
    """Node for a doubly linked list."""

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
    """Simple doubly linked list with head and tail references."""

    def __init__(self) -> None:
        self.head: DLLNode | None = None
        self.tail: DLLNode | None = None


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


def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    result = []
    current = sll.head

    while current:
        result.append(current.value)
        current = current.next

    return result


def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    seen = set()
    current = sll.head

    while current:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next

    return None


def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    current = dll.head

    while current:
        next_node = current.next

        if current.value == target:
            # update previous node
            if current.prev:
                current.prev.next = current.next
            else:
                dll.head = current.next

            # update next node
            if current.next:
                current.next.prev = current.prev
            else:
                dll.tail = current.prev

        current = next_node


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    left = dll.head
    right = dll.tail

    while left and right and left != right and left.prev != right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev

    return True