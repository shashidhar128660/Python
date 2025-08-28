numbers = (1, 2, -5)
print(numbers)

a_tuple = (0, [1, 2, 3], (4, 5, 6), 7.0)
print(a_tuple)

languages = ('Python', 'Swift', 'C++')
print(languages[0])

cars = ("BMW", "Tesla", "Ford", "Toyota")
print("Total cars are ",len(cars))

a = tuple(range(5))
print(a)

b = tuple(range(5, 10))
print(b)

c = tuple(range(0, 10, 2))
print(c)

d = tuple(range(10, 0, -2))
print(d)

d = (3,[5,6,7],(4,5,6),[5,6,7,(6,7,8)],9,10)
print(d[1][1])
print(d[2][2])
print(d[3][1])
print(d[3][3][0])

t1 = (2, 3, 4, 5)
print(sum(t1))

t3 = (3, 4, 4, 2, 2, 3, 6, 7 ,4 ,4)
print(t3.count(4))

t3 = (3, 4, 4, 2, 2, 3, 6, 7, 4, 4)
print(t3.index(2))
print(t3.index(4, 3, 9))

t3 = (3, 4, 4, 2, 2, 3, 6, 7, 4, 4)
print(min(t3))

numbers = (7, 2, 8, 5, 9)
print(max(numbers))

a = (5, 6, 7, 5, 5, 9, 7)
b = ("a", "b", "v", "b")
my_tu_1 = tuple(dict.fromkeys(a))
print(my_tu_1)
my_tu_2 = tuple(dict.fromkeys(b))
print(my_tu_2)

first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')
last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes')
ages = (49, 55, 39, 33)
zipped = tuple(zip(first_names, last_names, ages))
print(zipped)

b = ((1,2),(3,4),(5,6))
my = tuple(item for l in b for item in l)
print(my)

