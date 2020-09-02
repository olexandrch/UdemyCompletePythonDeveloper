#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 129. Extending List


class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print("Len of the empty list:  ", len(super_list1))
super_list1.append(5)
print("Len of the list after adding 5:  ", len(super_list1))
print("super_list1:  ", super_list1)

print("super_list1[0]:  ", super_list1[0])
print("issubclass(SuperList, list):  ", issubclass(SuperList, list))
