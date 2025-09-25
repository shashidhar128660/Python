# create a string using double quotes
string1 = "ICT Department"
print(string1)

# create a string using single quotes
string1 = ' ICT Department '
print(string1)

#Access String Characters in Python
string2 = '3EK1'
# access 1st index element
print(string2 [1])

string3 = 'ICT Department'
# access 4th last element
print(string3 [-4])

string4 = 'ICT Department'
# access character from 1st index to 3rd index
print(string4[1:4])

print(string4[:2])
print(string4[2:])

message = 'ICT Department'
message[0] = 'H'
print(message)

message = 'ICT'
# assign new string to message variable
message = 'ICT Department'
print(message)

# multiline string
message = """
ICT
Department
3EK1
"""
print(message)

str1 = "ICT"
str2 = "Department"
str3 = "3EK1"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

greet = "ICT"
name = "Department"
# using + operator
result = greet + name
print(result)

greet = 'ICT'
# count length of greet string
print(len(greet))

print('a' in 'program')
print('at' not in 'battle')

message = 'python is fun'
# convert message to uppercase
print(message.upper())

message = 'PYTHON IS FUN'
# convert message to lowercase
print(message.lower())

text = 'CE Department'
replaced_text = text.replace('CE', 'ICT')
print(replaced_text)

message = 'Python is a fun programming language'
# check the index of 'fun'
print(message.find('fun'))

title = 'Python Programming '
result = title.rstrip()
print(result)

text = 'Python is fun'
# split the text from space
print(text.split())

message = 'Python is fun'
# check if the message starts with Python
print(message.startswith('Python'))

pin = "523"
# checks if every character of pin is numeric
print(pin.isnumeric())

text = 'Python is fun'
# find the index of is
result = text.index('is')
print(result)

name = 'Cathy'
country = 'UK'
print(f'{name} is from {country}')

str = "This is a \n normal string example"
print(str)
raw_str = r"This is a \n raw string example"
print(raw_str)

#postlab exercise
str1 = "ICT Department"
rev_str1 = ""
for char in str1:
    rev_str1 = char + rev_str1
print(rev_str1)

str1 = "pamap"
rev_str1 = ""
for char in str1:
    rev_str1 = char + rev_str1

if (str1 == rev_str1):
    print(str1, "is palindrome")
else:
    print(str1, "is not palindrome")
    
str1 = "12345" # Example string, you can change this
if str1.isdigit():
    print(str1, "contains only digits")
else:
    print(str1, "does not contain only digits")
    
str1 = "125503"
a = str1.isdigit()
if (a == True):
    print ("The string", str1, "contains only digits")
else:
    print ("The string", str1, "does not contain only digits")
    
str1 = "Python is a fun programming Language"
words = str1.split()
res = ""
for word in words:
    if len(word) > len(res):
        res = word
        print (res)
        
str1 = "Python is fun"
words = str1.split()