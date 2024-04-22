''' Random Library 4 Choosing Random Words For List '''
import random

'''You're To Put-In Your Username'''
user_name = input("Dear User Key-In Your Name: ")

'''Printing Welcome Message 2 The User'''
print("Welcome 2 Our Word Guessing App!", user_name)

'''Word List'''
words = [
        "Grape",
        "Apple",
        "Peach",
        "Blueberry",
        "Cherry",
        "Orange"
]

'''Choose Random Choice'''
word = random.choice(words)

print("Guess Character: ")
'''Set Guesses To An Empty String'''
guesses = ''

'''Set Numbers Of Turns'''
turns = 15

'''Integrating While Loop'''
while turns > 0:
    failed = 0

    '''Integrating For Loop 4 Looping Through Word Guesses'''
    for i in word:
        '''Comparing Character With Character In Guesses'''
        if i in guesses:
            print(i, end=" ")
        else:
               print(".......")

               '''4 Every Failed Attempt 1 Will Be Incremented'''
               failed += 1
    if failed == 0:
        '''User's Gonna Win The Game Only If Failed Is Equal 2 Zero'''
        print("You're Exceptional Boss, You Win!")

        '''This's Gonna Print Out The Correct Word'''
        print("The Word Is: ", word)
        break
    print()
    guess = input("Guess Character: ")

    '''Every Input Is Gonna Stored In Guesses'''
    guesses += guess

    '''Checking 4 Input Character In Word'''
    if guess not in word:
        turns -= 1
        
        '''If Character Doesn't Match The Word, It's Gonna Render You Wrong Message'''
        print("Wrong Boss, The Word Doesn't Matches Your Request")

        '''This's Gonna Print Out Turns Left 4 User To Make Use Of'''
        print("You're Entitled To,", +turns, 'More Guesses')

        '''If It Turned Out Zero'''
        if turns == 0:
            print("Boss, You Loose")    
