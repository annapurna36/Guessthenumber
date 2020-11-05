import random

def login():

    print ("Welcome to guess the number")
    username = input("please enter the username :")
    password = input("please enter your password :")
    if username == "poonam" and password == "1234":
        print("correct!! you have successfully login to the application")
        return True
    else:
        print("You have entered the wrong login details, Authentication failed")
        return False
def start_game():
    if login():
        number = random.randint(1,10)
        chances = 0

        while chances < 10:
            print("The random number has been generated")
            guess = int(input("Guess the number: "))
            chances = chances +1

            if guess == number:
                print("Congratulations you have won the game")
                break

            elif guess < number:
                print("You are nearer to the number")

            elif guess > number:
                print("You are far from the number")

        if chances > 10:
            print("Sorry you have run out of chances, Game over!!!")

start_game()
