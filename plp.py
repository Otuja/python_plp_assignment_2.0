# plp weekly code challenge
# 1
values = input("what are the values u want to compute: ").split(',')
new_values = [int(i) for i in values]
print(sum(new_values))

# 2
fav_books = ("Mixed Grill", "Half-baked Bread", "Animorphers", "Treasure Island", "Oliver Twist")
for books in fav_books:
    print(books)

# 3
dict = {}
name = input("what is your name? ")
age = int(input("what is your age? "))
fav_col = input("what is your favourite color? ")
dict['name'] = name
dict['age'] = age
dict['favorite_color'] = fav_col
print(dict)

# bonus
# list1 = input("what is your first list of integer: ").split(',')
# list2 = input("what is your second list of integer: ").split(',')
# new_list = [i for i in list1 if i in list2]
# print(new_list)

# 4
list1 = input("what is your first list of integer: ").split(',')
list2 = input("what is your second list of integer: ").split(',')
# converting list to set
a = set(list1)
b = set(list2)
# '&' in new_set joins variables that are both in a and b
new_set = a & b
print(new_set)

# 5
store = input("type words u wish to store: ").split(',')
newStore = [i for i in store if len(i) % 2 != 0]
print(newStore)


# plp assignment
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
my_list.remove(70)
my_list.sort()
print(my_list.index(30))
