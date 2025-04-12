#copy 
# it copies entire list address assign it to new varible it will have new address for the new variable
# definition: Creates a new object but does not create copies of the nested objects. Instead, it copies the references of the nested objects from the original object to the new object.
list1 = [1,4,7,8,9,2]
list2 = list1 # here both are referring to same address, any changes made to any of them will affect to both
list3 = list2.copy() # here it list3 will have new address for entire list
list3.append(15)  # as list3 will have new address so append of new value will only be present for list3 not for list1 or list2
print('After appending the values:', list1, list2, list3)

#another way of doing shallow  copy
list2 = list1[:]
# one more scenario of shallow copy

list1 = [1,4,7,[15,16,26]]
list3 = list1.copy() # it will be shallow copy means list3 will have entire new address but inside elements are still have same old address
list1[3].append(55)  # as list3 will have new address so append of new value will only be present for list3 not for list1 or list2
print('\n After shallow copy values get changed:', list1, list3)

# with deepcopy this will create new address for entire list and elements present inside 
# definition: Creates a new object and recursively copies all nested objects. The new object and all its nested objects are completely independent of the original object.
import copy

list1 = [1,4,7,[15,16,26]]
list2 = list1 # here both are referring to same address, any changes made to any of them will affect to both
list3 = copy.deepcopy(list1) # here it list3 will have new address for entire list
list1[3].append(55)  # as list3 will have new address so append of new value will only be present for list3 not for list1 or list2
print('\n After doing with the deepcopy the values are:', list1, list2, list3)


# 1. lambda
# lambda: is anonymous function, that can take any number of parameters but , can have just one statement
# lambda is applicable to individual data type not for sequence 
s1 = 'GeekforGreek'
s2 = lambda el: el.upper()
print("\n Convert into upper case:", s2(s1))

# sum of two numbers
add = lambda x,y: x + y
print("\n adding two numbers:", add(5,6))

# using if and else loop inside lambda

res = lambda x,y: x if x > y else y
print("\n Check which number is greater:", res(20,55))

square = [2,4,8,6,18,20]
square_numbers = lambda x: [y **2 for y in square]
print('\n squaring the numbers:', square_numbers(square))


# 2. filter
age_groups = [12,7,8,14,25,56,96,75,20,35]
res = list(filter(lambda age: age > 18, age_groups))  # if we don't convert into list it will give the object back
print('\n voting age should be more than 18:', res)

#even number 
res = list(filter(lambda x: x % 2 == 0, age_groups))
print('\n check even numbers:', res)

#odd number
res = list(filter(lambda x: x %2 != 0, age_groups))
print('\n check odd numbers:', res)

# 3. Map
sqre = [2,3,9,18,17,16]

my_map = list(map(lambda x: x ** 2, sqre))
print('\n square of the number using map function:', my_map)