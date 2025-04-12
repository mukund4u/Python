
# Tuples : are the one which allows us to creat & read the items, but it will not allow us to modify means its immutable 
# This means Tuples once created it shouln't be altered as for that reason it will be created
# If the data is to big its better to go with Tuple as we can read and create & faster execution

technologies = ('JAVA','C#','Javascript')
print("print the techologies:", technologies)
print("\n it will give type of the variable i.e Tuples ", type(technologies))

print("to access the tuples will go with the indexing:", technologies[0])  # it will print JAVA

# reassigning the value
# technologies[0] = 'Linux'  # it will throw the error as its immutable

technologies = list((technologies))
print("\n after converitng into list:",technologies)
technologies = tuple((technologies))
print("\n converting back to tuples:",technologies)

# How to modify the tuple: tuple can modified by putting list value inside tuple and pop the list value 

num1 = [22,55,66,85,96,1,2,3]
tuple = ('A','B','C', num1)

num1.pop()

print('\n print the list value:', num1)
print('\n modifying the tuple value:', tuple)
