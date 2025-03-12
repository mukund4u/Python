# 1. String Concatenation:
str1 = "Hello"  
str2 = "World"
print(f'String Concatenation: {str1} {str2}')

# 2. String Repetition:
word = "Python"
word = word  * 3
print(f"String Repetition:{word}")

# 3. Extracting Characters:
text = "Programming"
middleCharater = len(text) // 2
print(f"Extracting Characters: printing the first character: {text[0]}")
print(f"Extracting Characters: printing the middle character: {text[middleCharater]}")
print(f"Extracting Characters: printing the last character: {text[-1]}")

# 4. String Slicing:
sentence = "The quick brown fox jumps over the lazy dog"

first_five = sentence[:5]
last_five = sentence[-5:]
print(f"String Slicing: printing the first five characters: {first_five}")
print(f"String Slicing: printing the last five characters: {last_five}")

# 5. Reversing a String:
word = "Django"
print(f"Reverse string: {word[ : :-1]}")

# 6. String Methods:
phrase = "  Python is Awesome!  "
print(f"String Methods: Upper case:{phrase.upper()} ")
print(f"Remove leading and trailing spaces: {phrase.strip()}")
res = phrase.replace('Awesome', 'Powerful')
print(f"Replace: {res}")

# 7. Checking for Substrings:
message = "Welcome to Python programming"
res = message.find("Python")
print(f"Checking for Substrings: Value : {res}")


# 8. Formatting Strings:

name = "Alice"
age = 25
print(f"Formatting Strings: {name} is {age} years old")

# 9. Splitting and Joining Strings:

quote = "Knowledge is power"
split_word = quote.split(" ")
join_word = quote.replace(" ", "-")
print(f"Splitting and Joining Strings: Split the string into words:{split_word}")
print(f"Join the words back together: {join_word}")

# 10. Counting Characters:

text = "banana"
char_count = text.count('a')
print(f"Counting Characters: character count:{char_count}")