city ='gadag'
state = 'Karnataka is state of many cities'
print(f'The state name is {state} and city name is {city}')
print(city == city[: : -1])
res = state.split()
print(res)
res.reverse()
print('after reverse:', res)
out = " ".join(res)
print(out)
num1 = 20
num2 = 30
num1, num2 = num2, num1
print(num1,num2)

statement ="Hello world from python"
out = " ".join(statement.split()[::-1])
print(out)

word = "banana"
print("".join(set(word)))


#string operations
s = 'Hello World'

print('Upper Case:', s.upper())
print('Lower Case:', s.lower())
print('Title Case:', s.title())
print('capitalize Case:', s.capitalize())
print('swapcase Case:', s.swapcase())

#Membership operator, find  & index keywords

word = "Hello, Welcome to Devops"

print("seach the keyword:", word.lower().find('welcome'))
print("printing the index:", word.lower().index('to'))
print('counting the characters:', word.lower().count('o'))
print('using membership operator:', 'Devops' in word)
print('using not in membership operator:', 'test' not in word)

#removing the spacess & its types
word = " Hello, Welcome to Devops "

print("removing the spaces using strip:", word.strip())
print("removing left side spaces lstrip", word.lstrip())
print('removing right side spaces rstrip:', word.rstrip())


#to check if its a number or not
word='Python1234'
print('using isDigit:', word.isdigit())

def checkEvenOrOdd(num1):
    if num1 % 2 == 0:
        print('Number is even')
    else:
        print("number is odd")


res =int(input())
checkEvenOrOdd(res)

    

