import random                       #Importing Random module
num = random.randint(1,10)
guesses = 6
count = 1
print("Guess a number between 1 and 10")
while guesses >0:                       #Loop begins
    print("Take a guess")
    guess = int(input())
    if guess > num:
        print("Your guess is too high")
    elif guess <num:
        print("Your guess is too low")
    elif guess == num:
        break
    guesses = guesses-1
    count = count + 1           #Loop ends

if guess == num:
    print('Congratulations, You guessed the no. in', count, 'guesses')
if guess !=num:
    print("The number I thought was",num)
    
input()
