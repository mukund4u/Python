# pass by value

def modify_value(x):
    x = 10
    print('Value changed inside the function:', x)

num = 5
modify_value(num)
print("Value of the variable outside the function:",num)

#pass by reference
def modify_value(value):
    value.append(4)
    print('The value is changed inside the function:', value)


num = [1,2,5,6]
modify_value(num)
print('Value outside the function:', num)

# Key Takeaways
# 1. Immutable types (int, str, tuple): Behave like pass-by-value (changes inside the function do not affect the original).

# 2. Mutable types (list, dict, set): Behave like pass-by-reference (changes inside the function affect the original).

# 3. Reassignment inside a function creates a new reference and does not affect the original variable.