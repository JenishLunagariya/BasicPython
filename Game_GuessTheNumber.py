import random
guesstaken=0

name=input('hello, what is your name:')
print(f'well,{name}, I am thinking of one number between 1 and 20')

number=random.randint(1,20)

for guesstaken in range(6):
    guess=input('take a guess:')
    guess=int(guess)

    if guess < number:
        print('your guess is too low.')

    if guess> number:
        print('your number is too high.')

    if guess==number:
        break

if guess==number:
    guesstaken=str(guesstaken+1)
    print('good job,',name,'! you guess my numer in',guesstaken,'guesses')

if guess!=number:
    number=str(number)
    print('nope. The number I was thinking is ',number)

