list = [2, 3, 4, 5]
result = 1
for num in list:
    result *= num
print("Product of all items:", result)


list = [5, 12, 7, 20, 3]
largest = max(list)
print("Largest number:", largest)


my_list = [1, 2, 2, 3, 4, 4, 5]
removed_list = list(dict.fromkeys(my_list))  # Or: list(set(my_list)) (unordered)
print("List without duplicates:", removed_list)

my_list = ['a', 'b', 'a', 'c', 'b', 'a']
frequency = {}
for item in my_list:
    frequency[item] = frequency.get(item, 0) + 1
print("Frequency of elements:", frequency)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = list(set(list1) & set(list2))
print("Common items:", common)

int_list = [1, 2, 3, 4]
combined = int("".join(map(str, int_list)))
print("Combined integer:", combined)

