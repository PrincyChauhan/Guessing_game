import random
random_number=random.randint(1,10)
while True:
    guess=input("choose any number from 1 to 10")
    guess=int(guess)

    if guess<random_number:
        print("It is low")
    elif guess>random_number:
        print("It is high")
    else:
        print("You win") 

        play_again=input("You want to play again?(y/n)") 
        if play_again=='y':
            guess=input("choose any number from 1 to 10")
            guess=None
        else:
            print("thanks for playing")
            break  
