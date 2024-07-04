import random
names=input("Enter names:")
list=names.split(',')
int=random.randint(0,len(list)-1)
print(f"{list[int]} will buy the meal")
