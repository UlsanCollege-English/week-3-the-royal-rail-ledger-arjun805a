# Week 3: The Royal Rail Ledger

## Summary

This assignment focuses on linked-list operations in a railway story setting. I implemented functions for building and reading a singly linked list, finding the first repeated value, removing banned cargo from a doubly linked list, and checking whether a train is a palindrome. The assignment uses both singly linked lists and doubly linked lists. The hardest part was handling pointer updates correctly in the doubly linked list.

---

## Approach

### build_sll_from_list(values)

* I started with an empty list and a head pointer set to None
* I built the list by creating new nodes and linking them one by one
* I made sure the values stayed in the correct order by adding nodes at the end

### sll_to_list(sll)

* I started at the head of the list
* I traversed the list by moving to the next node until None
* I collected values in a Python list by appending each node’s value

### find_first_repeat_sll(sll)

* I tracked values I had already seen by using a set
* When I found a repeated value, I returned it immediately
* If I reached the end with no repeat, I returned None

### remove_all_from_dll(dll, target)

* I traversed the list using a current pointer
* When I found the target value, I updated next and prev pointers
* I checked special cases such as removing head, tail, and all nodes

### is_train_palindrome(dll)

* I compared values from the front and back of the list
* I stopped when the pointers met or crossed
* I returned True if all values matched, otherwise False

---

## Complexity

### build_sll_from_list(values)

* *Time complexity:* O(n)
* *Space complexity:* O(n)
* *Why:* we create and link n nodes

### sll_to_list(sll)

* *Time complexity:* O(n)
* *Space complexity:* O(n)
* *Why:* we traverse all nodes and store values

### find_first_repeat_sll(sll)

* *Time complexity:* O(n)
* *Space complexity:* O(n)
* *Why:* we scan once and store seen values in a set

### remove_all_from_dll(dll, target)

* *Time complexity:* O(n)
* *Space complexity:* O(1)
* *Why:* we traverse once and only update pointers

### is_train_palindrome(dll) (stretch)

* *Time complexity:* O(n)
* *Space complexity:* O(1)
* *Why:* we compare from both ends without extra storage

---

## Edge-Case Checklist

* [x] empty SLL
* [x] empty DLL
* [x] single-node SLL
* [x] single-node DLL
* [x] no repeated values in SLL
* [x] repeated value appears later in SLL
* [x] repeated value includes the head value
* [x] removing from DLL when target is at head
* [x] removing from DLL when target is at tail
* [x] removing consecutive target values in DLL
* [x] removing all nodes from DLL
* [x] palindrome with odd length
* [x] palindrome with even length
* [x] non-palindrome DLL

---

## Assistance & Sources

### AI use

* I used AI: Yes
* It helped me understand logic, edge cases, and correct structure of functions

### Other sources

* Class notes: Used for understanding linked list basics
* Slides: Reviewed for concepts
* Book: Not used
* Websites: None
* Other: None

---

## Debugging Notes

* I first got stuck on updating pointers in the doubly linked list
* The failing test that helped me most was when removing head and tail nodes
* I fixed the issue by carefully updating both next and prev references
* One mistake I will avoid next time is forgetting edge cases like empty lists

---

## Final Reflection

This assignment helped me understand how linked lists work in real problems. Doubly linked lists were harder because of pointer management. The most surprising part was how many edge cases exist. I will review traversal and pointer updates before the next assignment.
Compose
