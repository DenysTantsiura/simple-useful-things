import copy

my_list = [1, 2, [4, 5]]
copy_list = my_list[:]
copy_list.append(7)
copy_list[2].append(4)
print(my_list)  # [1, 2, [4, 5, 4]]
print(copy_list)# [1, 2, [4, 5, 4], 7]

my_list[2][0] = 3
print(my_list)  # [1, 2, [3, 5, 4]]
print(copy_list)# [1, 2, [3, 5, 4], 7]

copy_list2 = my_list[:][:]
my_list[2][0] = 6
print(my_list)   # [1, 2, [6, 5, 4]]
print(copy_list2)# [1, 2, [6, 5, 4]]

#copy_list3 = my_list.copy()
copy_list3 = copy.copy(my_list)
my_list[2][0] = 30
my_list[0] = 30
print(my_list) # # [30, 2, [30, 5, 4]]
print(copy_list3)  #[1, 2, [30, 5, 4]]


copy_list4 = copy.deepcopy(my_list)
my_list[2][0] = 60
my_list[0] = 60
print(my_list) #   [60, 2, [60, 5, 4]]
print(copy_list4) #[30, 2, [30, 5, 4]]

