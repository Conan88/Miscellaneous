import random


player1 = input("Player 1 select a number between 0 and 10: ")
player2 = input("Player 2 select a number between 0 and 10: ")

random_number = random.randint(0, 10)

print("Random number is:", random_number)

if abs(int(player1) - int(random_number)) < abs(int(player2) - int(random_number)):
    print("Player 1 was closest! Congrats!")
elif abs(int(player1) - int(random_number)) > abs(int(player2) - int(random_number)):
    print("Player 2 was closest! Congrats!")
else:
    print("Draw! Go again!")
