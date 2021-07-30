import math
import random

# print(math.pi)
# print(math.ceil(1.1))
# print(math.floor(1.9))

# print(math.trunc(-1.9))
# print(math.floor(-1.9))

# print(math.sqrt(25))
# print(math.pow(2,3))


# print(random.randint(1,10))       # randint = 1~10   <= 10

# print(random.randrange(10))       # randrange = 1~9   <10
# print(random.randrange(1,10))
# print(random.randrange(1,10,2))

# print(random.random())

# if random.random() < 0.5:
#     print('Hi')

# seasons = ['spring', 'summer', 'fall', 'winter']
# print(random.choice(seasons))

# print(random.sample(range(1,46),6))

# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)

# dice = random.randint(1,6)
# while True:
#     user = int('What if the value of dice?')
#     if dice == user:
#         print('{}! Thats right')
#         break
#     else:
#         print('Thats wrong. Please try again')


# Rock, scissors, paper game
 
import random

com = [1, 2, 3]
player = 0

player = [1, 2, 3]
com = random.randint(1,3)
while True:
    user = int(input('Play rock, scissors, paper. 1. scissors 2. rock 3. paper\n\n >>>'))
    if player == 1 and com == 2:
        print('\n You win')
        break
    elif player == 2 and com == 3:
        print('\n You win')
        break
    elif player == 3 and com == 1:
        print('\n You win')
        break
    elif player == 2 and com == 1:
        print('\n You lose')
        break
    elif player == 3 and com == 2:
        print('\n You lose')
        break
    elif player == 1 and com == 3:
        print('\n You lose')
        break
    else:
        print('\n Try again')


