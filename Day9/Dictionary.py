programming_dictionary={
    "Bug":"an error in a program that prevents the program running as expected.",
    "Function:":"a piece of code that you can easiyl call over and over again",
}
dic={"a":5}
dic[5]="c"
print(dic)
print(programming_dictionary)
print(programming_dictionary.get("Bug"))
programming_dictionary["Loop"]="the action of doing something over and over again"
print(programming_dictionary)
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
a={"a":5,"b":3,"c":99,"f":55}
b={"a":3}
print(3 in a.values())
print(a.popitem())

