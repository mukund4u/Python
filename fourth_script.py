#list operations crud 
# List is mutable it will allow you to append, remove basically you will do crud operations
# pop is associated with the list and del is keyword which can use for inbuilt function like list, tuples,set & dictionary,
# once del (deleted) it will delete with the memory not same for the pop keyword it will hold the address but not the value of it. will be not access the address

print(list(range(0,10))) # print all the numbers from 0 to 9

# 1. Append the list 

technologies = ['AWS','GCP', 'AZURE', 'AWS']

print('\n technologies:', technologies)

technologies1 = ['VS CODE','JENKINS', 'AWS']

technologies.extend(technologies1)
print("\n Extending the present list",technologies)
tool = technologies.copy()
print('\n Copying data from the list:', tool)

print("\n 0000000000",technologies * 5)

technologies.remove('AWS')
print("\n removing the data from the listt using remove:",technologies)
technologies.pop(2)
print("\n removing the elements using pop for specific index", technologies)


# to check duplicate item present in the list
print("insert at 1:",len(technologies))
print("set of len:", len(set(technologies)))
print("\n Cheking the duplicate list using set:", len(technologies) != len(set(technologies)))


# Differencce between Append & extend is, extend will add the items of another list at the last of the first list 
# where as Append will add the items at the last but it will insert complete list or single element

tool.append('Docker')
print('Appended:the list:tool', tool)
print('Appended:the list:technologies', technologies)
numbers = [1,2,3,4,5,2,3]
numbers.reverse()
print("numbers will be reversed:", numbers)

# inserting data at specific poistion
new_numbers = [7,8,9] 
new_numbers[2:2] = [1,2,4]  # output [7, 8, 1, 2, 4, 9]
print("inserting the data at specific index new_numbers:",new_numbers)


tool.clear()
print("\n using clear to empty the list:", tool)

# nested list
nested_list = [[123,456],45,56,6,89,7]
print("to access the items of nested list:",nested_list[0][1])   # output will be 456

# List Comphrension 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
res = [x for x in fruits if 'a' in x]
print(res)

