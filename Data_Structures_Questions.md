Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
    O(1)

2. What is the runtime complexity of `dequeue`?
    O(n)

3. What is the runtime complexity of `len`?
    O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?
    O(log n)

2. What is the runtime complexity of `contains`?
    O(log n)

3. What is the runtime complexity of `get_max`? 
    O(log n)

## Heap

1. What is the runtime complexity of `_bubble_up`?
    O(log n)

2. What is the runtime complexity of `_sift_down`?
    O(log n)

3. What is the runtime complexity of `insert`?
    O(log n)

4. What is the runtime complexity of `delete`?
    O(log n)


5. What is the runtime complexity of `get_max`?
    O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
    O(1)

2. What is the runtime complexity of `ListNode.insert_before`?
    O(1)

3. What is the runtime complexity of `ListNode.delete`?
    O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1) or O(n)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    Worst case run time is O(n) for array.splice.
    Worst case run time for doubly linked list is O(n)