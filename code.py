print("Welcome to my computer quiz !")
playing=input("Do you want to play ? ")
if playing.lower() !="yes":
    quit()
print("okay! let's play :) ")
score=0
answer=input("What does CPU stands for ? ")
if (answer.lower()=="central processing unit"):
    print("Correct !!")
    score=score+1
else:
    print("Incorrect !!")
answer=input("What does GPU stands for ? ")
if (answer.lower()=="graphics processing unit"):
    print("Correct !!")
    score=score+1
else:
    print("Incorrect !!")
answer=input("What does RAM stands for ? ")
if (answer.lower()=="random access memory"):
    print("Correct !!")
    score=score+1
else:
    print("Incorrect !!")
answer=input("What does ROM stands for ? ")
if (answer.lower()=="read only memory"):
    print("Correct !!")
    score=score+1
else:
    print("Incorrect !!")
print("you got "+ str(score)+ " questions correct!!")
print("you got "+ str((score/4)*100)+ " %")
print("Thank you for playing this game ")
