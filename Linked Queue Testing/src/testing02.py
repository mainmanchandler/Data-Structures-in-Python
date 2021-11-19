"""
------------------------------------------------------------------------
Sorted_list_linked testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-03-01"
------------------------------------------------------------------------
"""
#imports
from Sorted_List_linked import Sorted_List

print("---insert Testing---")
slist = Sorted_List()

#should be = [-4,-3,-1,0,1,1,4,6,6,7,8,9,10,14,14]
slist.insert(1)
slist.insert(6)
slist.insert(7)
slist.insert(4)
slist.insert(9)
slist.insert(10)
slist.insert(0)
slist.insert(1)
slist.insert(14)
slist.insert(6)
slist.insert(-3)
slist.insert(8)
slist.insert(14)
slist.insert(-1)
slist.insert(-4)
slist.insert(14)


print([x for x in slist])



print("\n\n---_linear_search method Testing---")
print("searching for 6 in the above list")
previous, current, index = slist._linear_search(6)
print(previous, "\n",current, "\n",index)



print("\n\n---remove Testing---")
print('removing 1:')
value = slist.remove(1)
print(value)
print([x for x in slist])



print("\n\n---remove_front Testing---")
value = slist.remove_front()
print(value)
print([x for x in slist])



print("\n\n---index Testing---")
print('finding the index of 6')
n = slist.index(6)
print(n)


print("\n\n---find Testing---")
print('finding 10')
value = slist.find(10)
print(value)


print("\n\n---peek Testing---")
print(slist.peek())


print("\n\n---count Testing---")
print('finding the amount of times 14 appears')
n = slist.count(14)
print(n)



print("\n\n---min Testing---")
value = slist.min()
print(value)


print("\n\n---max Testing---")
slist2 = Sorted_List()
slist2.insert(1)
slist2.insert(6)
slist2.insert(10)
slist2.insert(7)
slist2.insert(4)
slist2.insert(9)
value = slist2.max()
print([x for x in slist2])
print(value)



print("\n\n---is_identical Testing---")
source = [1,2,3,4,5,6]
list1 = Sorted_List()
llist1 = Sorted_List()

for i in source:
    list1.insert(i)
    llist1.insert(i)

b = list1.is_identical(llist1)
print(b)
print([x for x in list1])
print([x for x in llist1])


print()


source = [1,3,2,5,4,6]
source1 = [1,2,3,4,5,7]
list2 = Sorted_List()
llist2 = Sorted_List()

for i in source:
    list2.insert(i)

for i in source1:
    llist2.insert(i)
    
    
b = list2.is_identical(llist2)
print(b) 
print([x for x in list2])
print([x for x in llist2])





print("\n\n---__contains__ Testing---")
print([x for x in slist])
print('does the large list contain a 7')
yes = 7 in slist
print(yes)

print('does the large list contain a 7900')
no = 7900 in slist
print(no)


print("\n\n---__getitem__ method Testing---")
print('getting item at 1')
i = 1
value = slist[i]
print(value)



print("\n\n---clean Testing---")
print([x for x in slist])

slist.clean()

print([x for x in slist])



print("\n\n---intersection Testing---")
source1 = [1,2,3,4,5,6]
list1 = Sorted_List()

source2 = [1,4,23,42,42,2,3]
list2 = Sorted_List()

print(source1)
print(source2)

for i in source1:
    list1.insert(i)
    
for i in source2:
    list2.insert(i)
   
   
target = Sorted_List() 
target.intersection(list1, list2)

print("\nIntersection:")
for i in target:
    print(i, end=" ")




print("\n\n---union Testing---")
source1 = [1,2,3,4,5,6]
list1 = Sorted_List()

source2 = [1,4,23,42,42,2,3]
list2 = Sorted_List()

print(source1)
print(source2)

for i in source1:
    list1.insert(i)
    
for i in source2:
    list2.insert(i)
   
   
target = Sorted_List() 
target.union(list1, list2)

print("\nUnion:")
for i in target:
    print(i, end=" ")

