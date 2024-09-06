# Akshat Choudhary
# Roll NO- 08
# 23t3008



# Q. given an array, make a linked list out of the values in it
class Node:
    def __init__(self,val=0,next=None) -> None:          # making a node class
        self.val=val
        self.next=next
arr = [12,43,23,43,76,54,34]                             # taking a static arrau
print('Printing the array : - ')
for i in arr:
    print(i, end= "\t")
head=Node()                                              # head is taken as a empty which we will delete later
last=head
for i in arr:
    last.next=Node(i)                                    # adding values in a node using iteration
    last=last.next
head = head.next                                          #removing empty head
i=head
print('\n Printing the linked list : - ')
while i:
    print(i.val, end= "\t")
    i=i.next