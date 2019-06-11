from doubly_linked_list import DoublyLinkedList

# 1. Add characters from front & back
# 2. remove characters from front & back
# 3. Render the content of our buffer.
# 4. Concatenate two buffers together. (copy/paste)


## DLL vs Array -- Single Characters

#Features            prepend, append, delete_front, delete_back, join, print
#DLL:                 O(n)      O(1)      O(1)          O(1)      O(1)  O(n)
#Array:               O(n)      O(1)      O(n)          O(1)      O(n)  O(n)

class TextBuffer:
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        if init:
            for char in init:
                self.contents.add_to_tail(char)
    
    def __str__(self):
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, str_to_add):
        for char in str_to_add:
            self.contents.add_to_tail(char)

    def prepend(self, str_to_add):
        for char in str_to_add[::-1]:
            self.contents.add_to_head(char)
    
    def delete_front(self, chars_to_remove):
            # If you don't use the 'i' variable, you can make it an _ so that it takes up less memory.
        for _ in range(chars_to_remove):
            self.contents.remove_from_head()

    def delete_back(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.contents.remove_from_tail()
    
    # connect the tail of this buffer with the head of the other buffer
    # set the other buffer's head's previous to be self.tail
    # update other buffer's head to be this buffer's head
    # update this buffer's tail to be other buffer's tail.
    def join(self, other_buffer):
        self.contents.tail.next = other_buffer.contents.head
        other_buffer.contents.head.prev = self.contents.tail
        other_buffer.contents.head = self.contents.tail
        self.contents.tail = other_buffer.contents.tail


text = TextBuffer("Super")
print(text)

text.append("califragilisticexpealidocious")
print(text)

text.delete_back(8)
print(text)

text.prepend("Hey! ")
print(text)

text.delete_front(5)
print(text)

# from doubly_linked_list import DoublyLinkedList

# class TextBuffer:
#     def __init__(self, init=None):
#         self.contents = DoublyLinkedList()
#         if init:
#             for char in init:
#                 self.contents.add_to_tail(char)

#     def __str__(self):
#         s = ""
#         current = self.contents.head
#         while current:
#             s += current.value
#             current = current.next
#         return s
        
#     def append(self, str_to_add):
#         for char in str_to_add:
#             self.contents.add_to_tail(char)

#     def prepend(self, str_to_add):
#         for char in str_to_add[::-1]:
#             self.contents.add_to_head(char)

#     def delete_front(self, chars_to_remove):
#         for _ in range(chars_to_remove):
#             self.contents.remove_from_head()

#     def delete_back(self, chars_to_remove):
#         for _ in range(chars_to_remove):
#             self.contents.remove_from_tail()

#     def join(self, other_buffer):
#         # connect the tail of this buffer with the head of the other buffer 
#         self.contents.tail.next = other_buffer.contents.head
#         # Set the other buffer's head's previous to be self.tail
#         other_buffer.contents.head.prev = self.contents.tail 
#         # update other buffer's head to be this buffer's head 
#         other_buffer.contents.head = self.contents.head
#         # update this buffer's tail to be the other's tail
#         self.contents.tail = other_buffer.contents.tail


# text = TextBuffer("Super")
# print(text)

# text.append("califragilisticexpealidocious")
# print(text)

# text.delete_back(8)
# print(text)

# text.prepend("Hey! ")
# print(text)

# text.delete_front(5)
# print(text)