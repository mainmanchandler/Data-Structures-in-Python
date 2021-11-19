"""
------------------------------------------------------------------------
list_linked testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-03-01"
------------------------------------------------------------------------
"""
#imports
from List_linked import List

print("---Is_identical Testing---")
source = [1,2,3,4,5,6]
list = List()
llist = List()

for i in source:
    list.append(i)
    llist.append(i)

b = list.is_identical(llist)
print(b)



print("\n\n---remove_many Testing---")
source = [1,2,2,3,2,2,4,2,5,6]
list1 = List()
for i in source:
    list1.append(i)

for i in list1:
    print(i,end=" ")
list1.remove_many(2)
print()
for i in list1:
    print(i,end=" ")



print("\n\n---__getitem__ Testing---")
print([i for i in list])
print("index in the list 1: ", list[1])



print("\n\n---clean Testing---")
source1 = [1,1,2,2,3,4,5,5]
llist = List()
for i in source1:
    llist.append(i)

for i in llist:
    print(i,end=" ")
llist.clean()

print()
for i in list:
    print(i,end=" ")



print("\n\n---intersection Testing---")
source1 = [1,2,3,4,5,6]
list1 = List()

source2 = [1,4,23,42,42,2,3]
list2 = List()

print(source1)
print(source2)

for i in source1:
    list1.append(i)
    
for i in source2:
    list2.append(i)
   
   
target = List() 
target.intersection(list1, list2)

print("\nIntersection:")
for i in target:
    print(i, end=" ")
    
    

print("\n\n---union Testing---")

source1 = [1,2,3,4,5,6]
list1 = List()

source2 = [1,4,23,42,42,2,3]
list2 = List()

print(source1)
print(source2)

for i in source1:
    list1.append(i)
    
for i in source2:
    list2.append(i)
   
   
target = List() 
target.union_r(list1, list2)



print("\nUnion:")
for i in target:
    print(i, end=" ")



print("\n\n---prepend/append Testing---")
for i in source:
    llist.prepend(i)
llist.append(99)
print([x for x in llist])



print("\n\n---remove_front Testing---")
llist.remove_front()
print([x for x in llist])


print("\n\n---combine Testing---")
source3 = [1,2,3,4,5]
source4 = [6,7,8,9,10]
llist1 = List()
llist2 = List()
target = List()

for i in source3:
    llist1.append(i)
for i in source4:
    llist2.append(i)

target.combine(llist1, llist2)

print(source3)
print(source4)
for i in target:
    print(i, end=" ")

for i in llist1:
    print(i, end=" ")
    print('zzz')

for i in llist2:
    print(i, end=" ")
    print('zzz')


print("\n\n---split Testing---")
source = [1,2,3,4,5,6]
list_to_split = List()
for i in source:
    list_to_split.append(i)

print('source:')
for i in list_to_split:
    print(i, end=" ")

target1, target2 = list_to_split.split()

print('\nTarget1:')
for i in target1:
    print(i, end=" ")

print('\nTarget2:')    
for i in target2:
    print(i, end=" ")


print("\n")
source = [1,2,3,4,5]
list_to_split = List()
for i in source:
    list_to_split.append(i)

print('source:')
for i in list_to_split:
    print(i, end=" ")

target1, target2 = list_to_split.split()

print('\nTarget1:')
for i in target1:
    print(i, end=" ")

print('\nTarget2:')    
for i in target2:
    print(i, end=" ")





print("\n\n---split_alt Testing---")

source = [1,2,3,4,5,6]
list = List()

for i in source:
    list.append(i)

target1, target2 = list.split_alt()

print("source array: ",source)

print("target1:")
for i in target1:
    print(i, end=" ")  

print("\ntarget2:")
for i in target2:
    print(i, end=" ") 







