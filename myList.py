
my_list = []


my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


my_list.insert(1, 15)


my_list.extend([50, 60, 70])


my_list.pop()


my_list.sort()


index_30 = my_list.index(30)
print("Index of value 30:", index_30)

print("Final list:", my_list)

=============== RESTART: C:/Users/98071456/Desktop/plp/myList.py ===============
Index of value 30: 3
Final list: [10, 15, 20, 30, 40, 50, 60]
