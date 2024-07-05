import math
def paint_calc(height,width,cover):
    numberofcans =math.ceil(height*width/cover)
    print(f"You'll need {numberofcans} cans of paint.")
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(test_h,test_w,coverage)
#PrimeChecker
n = int(input()) # Check this number


def prime_checker(number):
    prime = True
    for i in range(2,number):
        if number % i == 0:
            prime = False

    print(f"{number} is prime:{prime}.")


prime_checker(n)
