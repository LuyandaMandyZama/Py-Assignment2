my_list = []
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list = [10, 20, 30, 40]
my_list.insert(1, 15)
print(my_list)


my_list = [10, 15, 20, 30, 40 ] 
list2 = [50, 60, 70]
my_list.extend(list2)
print(my_list)


my_list = [10, 15,  20, 30, 40, 50, 60, 70 ]
my_list.pop()
print(my_list)

my_list.sort()
print(my_list)

my_list = [10, 15, 20, 30, 40, 50, 60, 70]
index = my_list.index(30) 
print(index)
