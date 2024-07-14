# list=[0,4,5,6]
# enemies=1
"""If you operate with the same variable name inside and outside of
 a function, Python will treat them as two separate variables,
  one available in the global scope (outside the function)
 and one available in the local scope (inside the function):"""
# def change_variable():
#     enemies=3
#     print(enemies)
# change_variable()
# print(enemies)
# def change_list():
#     list[0]=1
#     print(list)
# change_list()
# print(list)

# player_health=10
# def game():
#     player_health=5
#     def drink_potion():
#         #player_health=2
#         potion_strength=7
#         print(player_health)
#     drink_potion()
#     print(player_health)
# game()
# print(player_health)
# #Dögüler local scope oluşturmaz
# if 3>2:
#     new_player_health=22
# player_health=new_player_health
# print(new_player_health)
# """If you need to create a global variable, but are stuck in the local scope,
#  you can use the global keyword.
# The global keyword makes the variable global."""
# def myfunc():
#     global x
#     x=300
# #firstly you should invoke the func, otherwise you will get an error
# myfunc()
# print(x
list=[0,1]
a=5
def change_list():
    a=3
    list.append(2)

change_list()
print(list)
print(a)



