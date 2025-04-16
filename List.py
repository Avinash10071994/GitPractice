
#==========================LIST==========================================

#List allows duplicate elements
#List objects are mutable means we can change the list elements

lst = ['a2',1]
print(lst)

#creating list by using range() functino

lst1 = list(range(10))
print(lst1)
lst2 = list(range(2,8))
print(lst2)

#slicing = (:)

lst3 = ['a','b',2,4]
print(lst3[0:2])

#list allows concatination and multiplication

lst4 = [1,2,3]
lst5 = ['a','b','c']
print(lst4+lst5)

lst6 = [10,20,30,40]
print(lst6*2)

#List functions or Methods

#1. len()

lst7 = [1,5,8,'a','b',5]
print(len(lst7))

#2. count(element)

print(lst7.count(5))

#3. index(object)

print(lst7.index('a'))
#3

#4. index on nested list

lst8 = ['a',100,'b',2,3,4,['ram',5]]
print(lst8[6].index(5))
#1
print(lst8[6].index('ram'))
#0

#5. append()

lst9 = [10,20,'avi',50,30]
lst9.append(80)
print(lst9)
#[10, 20, 'avi', 50, 30, 80]
lst9.append([0,1,2])  #will add in list as sublist
print(lst9)
#[10, 20, 'avi', 50, 30, 80, [0, 1, 2]]

#6 extend()

# This function adds multiple elements at the end of the existing list as multiple elements

lst10 = [1,2,8,7,'a','b','c']
lst10.extend([10,20,30])
print(lst10)
#[1, 2, 8, 7, 'a', 'b', 'c', 10, 20, 30]

#7. insert(index_position,element)

lst11 = [1,2,3,4]
lst11.insert(2,5)
print(lst11)
#[1, 2, 5, 3, 4]
lst11.insert(1,[10,20])
print(lst11)
#[1, [10, 20], 2, 5, 3, 4]

#8. remove(object)
lst11.remove(1)
print(lst11)
#[[10, 20], 2, 5, 3, 4]

lst12 = [1,2,1,3]
lst12.remove(1) #only first occurence element deleted
print(lst12)
#[2, 1, 3]

#9. pop(index)

lst13 = [10,20,40,'a','b']
lst13.pop(2)
print(lst13)
#[10, 20, 'a', 'b']
lst13.pop() #If index value not given then by default last element removed automatically from given list  and also returns this removed value. 
print(lst13)
#[10, 20, 'a']

#10. reverse()
lst14 = ['avi','vipul',1,5,4]
lst14.reverse() #gives output in reverse order
print(lst14)
#[4, 5, 1, 'vipul', 'avi']

#11. reversed(object)

lst12 = [2,4,8,'a','c']
print(reversed(lst12)) #gives output in reversediterator object
#<list_reverseiterator object at 0x000002815D8108B0>
print(list(reversed(lst12))) #using list() method we can get elements
#['c', 'a', 8, 4, 2]

#12. copy()


lst13 = [1,2,3]
x = lst13.copy()
print(lst13)
print(x)
#[1, 2, 3]
#[1, 2, 3]

#After copying the given list elements into another list gets new object reference.
print(id(lst13))
print(id(x))
#2259784938944
#2259784938752



#13.clear()

#This function clears entire elements from the list

lst14 = [1,2,3]
lst14.clear()
print(lst14)
#[]

#14. max()

lst15 = [2,4,6,8]
print(max(lst15))
#8

#15. min()
print(min(lst15))
#2

#15. sort()

lst16 = [1,8,7,2,4]
lst16.sort()
print(lst16)
#[1, 2, 4, 7, 8]
lst16.sort(reverse=True)
print(lst16)
#[8, 7, 4, 2, 1]

#16. del(index_number)

lst17 = [1,5,4,7]
del lst17[2]
print(lst17)
#[1, 5, 7]

#for deleting entire list objects
del lst17
#print(lst17)


#17 Converting a string into list

str = "Hello i am learning list functions"
print(str)

a = str.split()
print(a)
#['Hello', 'i', 'am', 'learning', 'list', 'functions']

#18. Converting list into string

lst19 = ['a','v','i']
a = "".join(lst19)
print(a)
#avi

#19 List packing

a = 10
b = 20
c = "avinash"
d = 40

lst = [a,b,c,d]
print(lst)
#[10, 20, 'avinash', 40]

#20. list unpacking

lst = [10,20,"rajesh",50]
a,b,c,d = lst
print(a)
print(b)
print(c)
print(d)
#10
#20
#rajesh
#50