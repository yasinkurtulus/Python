# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum=0
for n in student_heights:
  sum+=n
number_of_students=0
for n in student_heights:
  number_of_students+=1
average=int(sum/(number_of_students))
print(f"total height {sum}")
print(f"average height {average}")
print(f"total student {number_of_students}")
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
max_score=0
for maxscore in student_scores:
  if maxscore > max_score:
      max_score = maxscore
print(f"maximum score is {max_score}")

#For Loops with range func
for n in range(1,11,2):
  print(n)
  #Addıng Even Numbers
target = int(input())  # Enter a number between 0 and 1000
sum=0
for n in range(1,target+1):
  if n%2==0:
    sum+=n
print(sum)


