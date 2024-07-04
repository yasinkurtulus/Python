line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map=[line1,line2,line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
letter=position[0].lower()
abc=["a","b","c"]
first_index=abc.index(letter)
map[first_index][int(position[1])-1]="X"
print(f"{line1}\n{line2}\n{line3}")
