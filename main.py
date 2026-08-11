import random

n = random.randint(1, 100)
a = -1
Guesses = 1
while(a != n):
    a = int(input("Guess The Number: "))
    if(a > n):
        print("Lower Number Please")
        Guesses += 1
    elif(a < n):
        print("Higher Number Please")
        Guesses += 1
    else:
        print("Number You Entered Is: Invalid")

print(f"You Have Guessed The Number, {n} Correctly in {Guesses} Attempt")
