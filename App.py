"""TIC TAC TOE GAME"""
import time


def check_logic(player, p_input, p_number):

    try:
        p_input = int(p_input)
    except ValueError:
        print('\nInvalid entry')
        p_input = input('Player {}, please enter a number (1 - 9) to input '
                            'an {} in the corresponding location:\n'.format(p_number, player))
        p_input = check_logic(player, p_input, p_number)

    while p_input not in range(1, 10):
        p_input = input('Player {} out of range index, please enter a number (1 - 9) to input '
                            'an {} in the corresponding location:\n'.format(p_number, player))
        p_input = check_logic(player, p_input, p_number)

    if dictionary[p_input] is not '':
        while dictionary[p_input] is not '':
            print('That cell has already been taken, please choose a valid cell!\n')
            p_input = input('Player {}, please enter a number (1 - 9) to input '
                                'an {} in the corresponding location:\n'.format(player_number, player))
            p_input = check_logic(player, p_input, p_number)
    else:
        pass

    return p_input


print("\n\n\n\t\tWelcome!\n------------------------\n")

player1 = ''

"""this value is just an empty string-holder"""
a = ''

dictionary = {1: a, 2: a, 3: a, 4: a, 5: a, 6: a, 7: a, 8: a, 9: a}
won = False
iterator = 2

while player1 not in ('X', 'O'):
    print("Please enter a valid choice (X, O)")
    player1 = input('Player 1, Do you want to be X or O?: ').upper()
    player1 = player1.replace(" ", "")

if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'

print('\nPlayer 1 --> {} <-- will go first\n\n'.format(player1))
print('Please wait for the screen to display')

time.sleep(3.75)
print('{}'.format('\n') * 20)

while won is False:
    print('Board layout is as follows: 7 | 8 | 9\n\t\t\t\t\t\t   -----------'
          '\n\t\t\t\t\t\t\t4 | 5 | 6\n\t\t\t\t\t\t   -----------\n\t\t\t\t\t\t\t1 | 2 | 3')
    print('\t\t|\t\t|\t')
    print('\t{}\t|\t{}\t|\t{}'.format(dictionary[7], dictionary[8], dictionary[9]))
    print('\t\t|\t\t|')
    print('-------------------------')
    print('\t\t|\t\t|')
    print('\t{}\t|\t{}\t|\t{}'.format(dictionary[4], dictionary[5], dictionary[6]))
    print('\t\t|\t\t|')
    print('-------------------------')
    print('\t\t|\t\t|')
    print('\t{}\t|\t{}\t|\t{}'.format(dictionary[1], dictionary[2], dictionary[3]))
    print('\t\t|\t\t|\t')

    if '' not in (dictionary[7], dictionary[8], dictionary[9]) and dictionary[7] == dictionary[8] == dictionary[9]:
        won = True
    elif '' not in (dictionary[4], dictionary[5], dictionary[6]) and dictionary[4] == dictionary[5] == dictionary[6]:
        won = True
    elif '' not in (dictionary[1], dictionary[2], dictionary[3]) and dictionary[1] == dictionary[2] == dictionary[3]:
        won = True
    elif '' not in (dictionary[7], dictionary[4], dictionary[1]) and dictionary[7] == dictionary[4] == dictionary[1]:
        won = True
    elif '' not in (dictionary[2], dictionary[5], dictionary[8]) and dictionary[2] == dictionary[5] == dictionary[8]:
        won = True
    elif '' not in (dictionary[9], dictionary[6], dictionary[3]) and dictionary[9] == dictionary[6] == dictionary[3]:
        won = True
    elif '' not in (dictionary[7], dictionary[5], dictionary[3]) and dictionary[7] == dictionary[5] == dictionary[3]:
        won = True
    elif '' not in (dictionary[9], dictionary[5], dictionary[1]) and dictionary[9] == dictionary[5] == dictionary[1]:
        won = True
    elif iterator == 11:
        break
    else:
        pass

    if won is True:
        break
    else:
        pass

    player_input = 0
    '''or type(player_input) != int'''

    if iterator % 2 == 0:

        player_number = 1
        player_input = input('Player 1, please enter a number (1 - 9) to input '
                                 'an {} in the corresponding location:\n'.format(player1))
        player_input = check_logic(player1, player_input, player_number)
        dictionary[player_input] = player1

    else:

        player_number = 2
        player_input = input('Player 2, please enter a number (1 - 9) to input '
                                 'an {} in the corresponding location:\n'.format(player2))
        player_input = check_logic(player2, player_input, player_number)
        dictionary[player_input] = player2

    iterator += 1
    print('{}'.format('\n') * 15)

if iterator == 11:
    if won is False:
        print('Cat\'s game!')
    else:
        print('Player 1 wins!')
elif iterator % 2 == 0:
    print('Player 2 has won!')
else:
    print('Player 1 has won!')
