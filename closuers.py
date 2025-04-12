# Clousers
def exponents(num1):
    def doSomething(num2):
        return num2 ** num1
    
    return doSomething

square = exponents(2)
print(square(5))
print(square(3))

def counters():
    count = 0
    def doIncrements():
        nonlocal count
        count+= 1
        return count
    return doIncrements

counter_instances = counters()
print(counter_instances())

def greeting(param):
    def doSomething():
        print(f"Good Morning Mr.{param}")

    return doSomething

greet = greeting('sachin')
print(greet())