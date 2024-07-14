from functools import reduce
my_list=[1,2,3,4,5,6,7,8,9,10]
your_list=[10,20,"a",True]
their_list=[70,80,90,100,250]
def multiply_by_2(item):
    return item*2
print(list(map(multiply_by_2,my_list)))
print(my_list)
 #filter
def check_odd(item):
     return item%2!=0
print(list(filter(check_odd, my_list)))
print(my_list)
#zip
print(list(zip(my_list,your_list,their_list)))
print(my_list)
print(your_list)
#reduce
def accumulator(acc,item):
    print(acc,item)
    return acc+item
print(reduce(accumulator,my_list))
