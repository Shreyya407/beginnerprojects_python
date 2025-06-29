print("WELCOME TO MY PYTHON QUIZ! ARE YOU READY TO TEST YOUR KNOWLEDGE")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Let's Begin! There are 5 questions to answer.(ANSWER IN LOWER CASES) :)")
score = 0

answer = input("Which keyword is used to define a function in Python?")
if answer.lower() == "def":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What data type is result of type(5.0)?")
if answer.lower() == "float":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which operator is used for exponentiation in Python?")
if answer.lower() == "**":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which built-in function is used to get the length of the list? ")
if answer.lower() == "len()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which module is used for working with random values?  ")
if answer.lower() == "random":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")