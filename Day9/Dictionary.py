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