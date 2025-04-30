import random
ROCK = 0
PAPER = 1
SCISSORS = 2

#This is the basic rock paper scissor game.
# Read random seed to support testing (do not alter) and starting credits
seed = 100
# Set the seed for random
random.seed(int(seed))
print("Player 1, Enter your name: ")
player_name1 = input()
print("Player 2, Enter your name: ")
player_name2 = input()
rounds = int(input("Number of round you want to play: "))
while rounds < 1 :
   print(f'Rounds must be > 0')
   rounds = int(input())
print(f'{player_name1} vs {player_name2} for {rounds} rounds')
#for number 4
player_win1 = 0
player_win2 = 0
#step 2 : generating random values
for x in range(rounds):
   player_choice1 = random.randint(0,2)
   player_choice2 = random.randint(0,2)
   while player_choice1 == player_choice2 :
       print("Tie")
       player_choice1 = random.randint(0,2)
       player_choice2 = random.randint(0,2)
  
   #step 3: determine the winner
   if (player_choice1 == ROCK and player_choice2 == SCISSORS) or \
      (player_choice1 == SCISSORS and player_choice2 == PAPER) or \
      (player_choice1 == PAPER and player_choice2 == ROCK):
      player_win1 += 1 #player1 win calculation 
      if player_choice1 == ROCK :
       print(f'{player_name1} wins with rock')
      elif player_choice1 == PAPER :
       print(f'{player_name1} wins with paper')
      elif player_choice1 == SCISSORS :
       print(f'{player_name1} wins with scissors')
   else :
       player_win2 += 1
       if player_choice2 == ROCK :
           print(f'{player_name2} wins with rock')
       elif player_choice2 == PAPER :
           print(f'{player_name2} wins with paper')
       elif player_choice2 == SCISSORS :
           print(f'{player_name2} wins with scissors')
#step-4 :finding out the winner
print(f'{player_name1} wins {player_win1} and {player_name2} wins {player_win2}')
