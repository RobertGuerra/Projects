
import random
import time


class Hand:
    number = 0
    suits = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             {'Ace': '11'}, {'Jack': '10'}, {'Queen': '10'}, {'King': '10'}]
    ace_list = []

    def __init__(self):
        pass

    def assign(self):
        num = random.choice(self.cards)
        suit = random.choice(self.suits)
        card = (num, suit)

        return card

    def update_running_total(self, card):
        num = card[0]
        if type(num) == dict:
            num = num.values()[0]
        else:
            pass
        self.number += int(num)

    def check_total(self, card_list):
        if self.number > 21:
            for card in card_list:
                if type(card[0]) == dict and card[0].keys()[0] == 'Ace':
                    if card in self.ace_list:
                        pass
                    else:
                        self.number = self.number - 10
                        self.ace_list.append(card)
                else:
                    pass
            if self.number > 21:
                return 'bust'
            else:
                return ''
        elif self.number == 21:
            return 'won'
        else:
            return ''

    @staticmethod
    def unique_card(card, card_list, second_card_list):
        while card in card_list or card in second_card_list:
            card = Hand().assign()
        return card

    def display(self, card):
        num, suit = card
        if type(num) == dict:
            num = num.keys()[0]
        else:
            pass
        return '{} of {}'.format(num, suit)


cont = raw_input('\n\nPress enter key to continue...')

'''GAME START'''
'''Player and Dealer Initialization'''
player = Hand()
dealer = Hand()

'''Lists containing tuples (card#, suit)'''
player_card_list = []
dealer_card_list = []

'''Lists containing each card the dealer and the player have drawn'''

'''Player'''
player_card_list.append(player.assign())
new_card = player.assign()
new_card = player.unique_card(new_card, player_card_list, dealer_card_list)
player_card_list.append(new_card)
player.update_running_total(player_card_list[0])
player.update_running_total(player_card_list[1])

print('\n\nHere are your cards: {}  | and |  {}'.format(player.display(player_card_list[0]),
                                                            player.display(player_card_list[1])))

'''Dealer'''
dealer_card_list.append(player.assign())
new_card = dealer.assign()
new_card = dealer.unique_card(new_card, dealer_card_list, player_card_list)
dealer_card_list.append(new_card)
dealer.update_running_total(dealer_card_list[0])
dealer.update_running_total(dealer_card_list[1])

print('\n\nHere are the dealers cards: {}  | and |  ?'.format(dealer.display(dealer_card_list[0])))
print('\n')

'''Hit/Stay (Player)?'''
choosing = True
user_input = ''

player_bust = False

while choosing:
    if user_input in ('H', 'h'):
        new_card = player.assign()
        new_card = player.unique_card(new_card, player_card_list, dealer_card_list)
        player_card_list.append(new_card)
        print('\n\nHere is your card: {}'.format(player.display(new_card)))
        print('Current cards: {}'.format(map(player.display, player_card_list)))
        player.update_running_total(player_card_list[len(player_card_list) - 1])
    elif user_input in ('S', 's'):
        print('You have made it to {}. The dealer will now play his hand.'.format(player.number))
        break
    else:
        pass

    if player.check_total(player_card_list) == 'bust':
        print("\nOh no you have exceeded 21!\nPlayer Total: {}".format(player.number))
        player_bust = True
        break
    elif player.check_total(player_card_list) == 'won':
        print("\nYou got to 21! Congratulations!")
        player_bust = True
        break
    else:
        pass

    user_input = raw_input('Would you like to hit or stay? (H/S): ')

'''Hit/Stay (Dealer)'''
while choosing and player_bust is False:
    new_card = dealer.assign()
    new_card = dealer.unique_card(new_card, dealer_card_list, player_card_list)
    dealer_card_list.append(new_card)
    print('\n\nHere is the dealer\'s card: {}'.format(dealer.display(new_card)))
    print('Dealer\'s current cards: {}'.format(map(dealer.display, dealer_card_list)))
    dealer.update_running_total(dealer_card_list[len(dealer_card_list) - 1])

    if dealer.check_total(dealer_card_list) == 'bust':
        print("\nThe dealer has surpassed 21!\nYou win!\nPlayer Total: {}"
              "\nDealer Total: {}".format(player.number, dealer.number))
        break
    elif dealer.check_total(dealer_card_list) == 'won':
        print("\nThe dealer got to 21!")
        break
    else:
        pass

    time.sleep(3)

