str1 = "ICT Department"
rev_str1 = ""
for char in str1:
    rev_str1 = char + rev_str1
print (rev_str1)

str1 = "pamap"
rev_str1 = ""
for char in str1:
    rev_str1 = char + rev_str1
if (str1 == rev_str1):
    print (str1, "is palindrome")
else:
    print (str1, "is not palindrome")
    
str1 = "125503"
a = str1.isdigit()

if (a == True):
    print ("The string", str1, "contains only digits")
else:
    print ("The string", str1, "does not contain only digits")
    
str1 = "Python is a fun programming language"
words = str1.split()
res = ""

for word in words:
    if len(word) > len(res):
        res = word        
print (res)

str1 = "Python is fun"
words = str1.split()
print ("Length of last word is: ", len(words[-1]))
