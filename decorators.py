#decorators
def decorators(param):
    def wrapper(*args):
        print('Performing the operations')
        res = param(*args)
        print(f"The operation is performed and the value is {res} \n")

    return wrapper

@decorators
def difference(num1,num2):
    return num1 - num2

@decorators
def add(num1,num2):
    return num1 + num2

add(50,70)

difference(60,40)

