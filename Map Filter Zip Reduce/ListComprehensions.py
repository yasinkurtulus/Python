my_list=[char for char in "hello"]
my_list2=[even**2 for even in range(0,100) if even%2==0]
#set comperhesions
my_set={char for char in "hello"}
my_set2={num**2 for num in range(0,10)}
#dict
dict={"a":1,"b":2,"c":3,"d":4}
my_dict={k:v**2 for k,v in dict.items()}
print(my_dict)