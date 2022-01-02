import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format=' % (asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails (# 0 is tails, 1 is heads) :')
    guess = int(input())
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    if toss == guess:
        print('You got it!')
        continue
    else:
        print('Nope! Guess again!')
    guesss = int(input())
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        break
