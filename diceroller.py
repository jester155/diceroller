import random

def diceRoller(numSides):
    #generates random number based on parameter
    rollResult = random.randint(1, numSides)
    print('The result of the roll is: ', rollResult)

rollAgain = 'yes'

while rollAgain == 'yes' or rollAgain == 'y':

    print('How many sides does this dice have(2-30)?')

    dice = int(input())

    while dice > 1 and dice < 31: #As it was before you had to choose a number less than 1 and greater than 31
        print('Please type a number between 2 and 30')
        dice = int(input())

    diceRoller(dice)

    print('Do you want to roll again? (yes or no)')
    rollAgain = input()
