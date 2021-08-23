import random


actions = ['rock', 'paper', 'scissors']
round_limit = 3
game_over = False


class Game():
    def __init__(self, player1):
        self.player1 = player1
    def brain(self):
        actions = ['rock', 'paper', 'scissors']

        player1 = input(' Input your choice: rock, paper, scissor: ')
        player2 = random.choice(actions)
        if player1 == player2:
            print(f"Both players selected {player1}. It's a tie!")
        elif player1 == 'rock':
            if player2 == 'scissors':
                print("Rock Smashes Scissors, you win!")
            else:
                print("Paper covers rock! You lose!")
        elif player1 == 'paper':
            if player2 == 'rock':
                print('Paper covers Rock! You Win!')
            else:
                print('Scissors cuts paper! You lose!!')
        elif player1 == 'scissors':
            if player2 == 'paper':
                print('Scissors cuts paper! You Win!')
            else:
                print("Rock smashes scissors! You Lose")
        def game_tracker():
            round_count = 1
            while game_over == False:
                if round_count < round_limit:
                    player1, player2
                    round_count += 1            
            
                else:
                    game_over == True
                    return(game_over)
me = Game("me")
me.brain()





