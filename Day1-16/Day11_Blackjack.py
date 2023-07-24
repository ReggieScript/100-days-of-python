import numpy as np
import os

def draw_card(sz):
    '''sz is the value of the size of the sample'''
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rnd_crd= np.random.choice(cards, size=sz, replace=False)
    return  rnd_crd

def check(user):
    x=sum(user)
    if x>21 :
        return False
    return True

def blackJack():
    play=input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")
    while play== 'y':
        os.system('cls')
        #print(art.logo)
        user_crds=draw_card(2)
        computer_crds=draw_card(2)
        while check(user_crds):
            print(f"Your cards: {user_crds}, current score: {sum(user_crds)}")
            print(f"Computer's first card: {computer_crds[0]}")
            if input("Type 'y' to get another card, type 'n' to pass:\n")=='y':
                user_crds=np.concatenate((user_crds,draw_card(1)),axis=None)
            else:
                break
        while sum(computer_crds)<17:
            computer_crds=np.concatenate((computer_crds,draw_card(1)),axis=None)

#Final results

        print(f"Your final hand:{user_crds}, final score: {sum(user_crds)}")
        print(f"Computer's final hand:{computer_crds}, final score: {sum(computer_crds)}")

#Decision section

        if sum(user_crds)==21 and len(user_crds)==2:
            print('You win with BLACKJACK')
        elif (sum(user_crds)> sum(computer_crds) and sum(user_crds)<=21) or sum(computer_crds)>21:
            print("You Win!")
        elif sum(computer_crds)==21:
            print("The computer has blackjack, you lose!")
        elif sum(user_crds)==sum(computer_crds):
            print("Draw!")
        else:
            print("You lose!")
        play=input("'Do you want to play again?Type 'y' or 'n':\n")

blackJack()
