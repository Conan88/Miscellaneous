import math
import random

challenge = False
challenge_index = 0

player1 = []
player1_dice_left = 5
player1_dice_bet = -1
player1_number_of_dice = -1

player2 = []
player2_dice_left = 5
player2_dice_bet = -1
player2_number_of_dice = -1

player3 = []
player3_dice_left = 5
player3_dice_bet = -1
player3_number_of_dice = -1

player4 = []
player4_dice_left = 5
player4_dice_bet = -1
player4_number_of_dice = -1

all_players = [player1, player2, player3, player4]
all_players_dice = [player1_dice_left, player2_dice_left, player3_dice_left, player4_dice_left]
all_players_bet = [player1_dice_bet, player2_dice_bet, player3_dice_bet, player4_dice_bet]
all_players_number_of_dice = [player1_number_of_dice, player2_number_of_dice, player3_number_of_dice, player4_number_of_dice]

def dice():
    dice = random.randrange(1,7)
    return dice

def round(dice_left, all_players):
    index = 0
    for player in all_players:
        for i in range(all_players_dice[index]):
            player.append(dice())
        index += 1

round(all_players_dice, all_players)

print("player 1", player1)
print("player 2", player2)
print("player 3", player3)
print("player 4", player4)

def bet():
    global challenge_index
    while True:
        user_challenge = str(input("Do you want to challenge bet? (y,Y/n,N)"))
        if user_challenge in ["y", "Y"]:
            global challenge
            challenge = True
            return False
        else:
            user_bet = input("Enter dice bet:")
            global all_players_bet
            all_players_bet[challenge_index] = user_bet
            print("dice bet: ", user_bet)
            user_number = input("Enter number of dice bet:")
            global all_players_number_of_dice
            all_players_number_of_dice[challenge_index] = user_number
            print("number of dice bet: ", user_number)
        if challenge_index == 3:
            challenge_index = 0
        challenge_index += 1

def check_winner():
    global all_players_bet
    last_bet = all_players_bet[challenge_index - 1]
    global all_players_number_of_dice
    last_dice = all_players_number_of_dice[challenge_index - 1]
    global count_dice
    count_dice = 0
    index = 0

    for player in all_players:
        for i in range(all_players_dice[index]):
            if int(player[i]) == int(last_bet):
                count_dice += 1
        index += 1
        
    if count_dice > int(last_dice):
        all_players_dice[challenge_index] -= 1
        print("challenger wins", challenge_index)
    elif count_dice < int(last_dice):
        all_players_dice[challenge_index - 1] -= 1
        print("the challenged wins", challenge_index - 1)
    else:
        all_players_dice[challenge_index] -= 1
        all_players_dice[challenge_index - 1] -= 1
        print("draw", challenge_index - 1)

bet()
check_winner()
round(all_players_dice, all_players)

print("player 1", player1)
print("player 2", player2)
print("player 3", player3)
print("player 4", player4)
print("player",challenge_index)
