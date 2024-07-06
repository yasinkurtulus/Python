# integer = 10
# _float = 4.6
# string = "Yasin"
# boolen = False
# #Variables
# name = input("Enter your name: ")
# res=name*4
# print("hi "+ name+ res)
# birth_year= input("Birth Year")
# print(type(birth_year))
# age = 2024-int(birth_year)
# print(type(birth_year))
# print(age)
# #input func only return str values
# weight = input("Enter your weight(pounds): ")
# weight = int(weight)*0.45
# print("Your Weight is "+str(weight)+" kg")
# #input
# course = "Python for Beginners"
#          #012345
# print(course[-1])
# print(course[0:5])
# messages=f'{name} [{birth_year}] is a engineer'
# print(messages)
# print("Hi {} your age is {}".format(name,age))
# #format method
# print(len(name))#length of str
def score_calcutale(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
list=[11,11,11]
print(score_calcutale(list))



