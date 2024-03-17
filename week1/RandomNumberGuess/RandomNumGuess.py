import random
def main():
    while True:
        randNum = random.randint(1, 100)
        userGuess = int(input('Enter your guess: '))
        if userGuess < randNum:
            print('Too low, try again.')
            break
        elif userGuess > randNum:
            print('Too high, try again.')
            break
        else:
            print('Congrats you are right.')
main()