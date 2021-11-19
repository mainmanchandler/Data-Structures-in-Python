"""
------------------------------------------------------------------------
Queue_linked testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-03-08"
------------------------------------------------------------------------
"""
#imports
from Queue_linked import Queue

print("--insert testing--")
source = [3,5,3,2,1,5,7,3]
que = Queue()

for i in source:
    que.insert(i)
    
for i in que:
    print(i, end=" ")



print('\n\n')
print("--combine testing--")
source1=[11,33,55]
source2=[22,44,66]
print("input sources:")
print(source1)
print(source2)
print()


que1 = Queue()
que2 = Queue()
target = Queue()
for i in source1:
    que1.insert(i)
for i in source2:
    que2.insert(i)


target.combine(que1,que2)

for i in target:
    print(i, end=' ')



print('\n\n')
print("--split_alt testing--")
source = [1,2,3,4,5,6,7]
que = Queue()

print(source)
for i in source:
    que.insert(i)
    
tar1, tar2 = que.split_alt()
for i in tar1:
    print(i, end=" ")
print()
for i in tar2:
    print(i, end=" ")


print("--is_identical testing--")
source1=[11,33,55]
source2=[22,44,66]
#source1=[1,2,3]
#source2=[1,2,3]
print("input sources:")
print(source1)
print(source2)
print()

que1 = Queue()
que2 = Queue()
for i in source1:
    que1.insert(i)
for i in source2:
    que2.insert(i)


ok = que1.is_identical(que2)

print(ok)




