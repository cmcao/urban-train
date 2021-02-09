import sys

''' 
This function will give a sum of arrary
''' 
def array_sum(array_num):
    sum = 0
    for val_i in array_num:
        sum += val_i
    return sum

list = [3,4,5,6,7]
print("The list contain:",list)

print("Total sum of list is:",array_sum(list))

print(sys.version)

print("hello world")
