##NUMBER GUESSING GAME(1-100)
import random
num=random.randint(1,100)
while True:
    tries+=1
    guess=int(input("guess your number between 1-100"))
    if guess==num:
        print(f"congratulation you won in {tries} tries")
        break
    elif guess>num:
        print("Go a bit lower")
    else:
        print("Go a bit higher")

"""##rock paper scissor 
import random
com_score=0
user_score=0
while True:
    print()
    print()
    if user_score==5:
        print("congratulation")
        break
    elif com_score==5:
        print("you lost")
        break
    print(f"score: computer={com_score} human={user_score}")
    com= random.randint(1,3)
    #1-rock
    #2.paper
    #3.scissors
    print("#1-rock#2.paper#3.scissors")
    user=int(input("select your option:-"))
    if user>=1 and com<=3:

        if user==com:
            print("its a draw")
        elif user==1 and com==3:
            print("you won")
            user_score+=1
        elif user==2 and com==1:
            print("you won")
            user_score+=1
        elif user==3 and com==2:
            print("you won")
            user_score+=1
        else:
            print("computer won")
            com_score+=1
        
    else:
        print("choose between 1-3")"""

