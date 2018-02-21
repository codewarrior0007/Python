# www.practicepython.org
# Lesson # 7 - Rock Paper Scissors
# -------------------------------------------------------------------------------
# Make a two-player Rock-Paper-Scissors game. _
# (Hint: Ask for player plays (using input), _
# compare them, print out a message of congratulations _
# to the winner, and ask if the players want to start a new game) _
# Remember the rules: _
# Rock beats scissors _
# Scissors beats paper _
# Paper beats rock
# -------------------------------------------------------------------------------
print("Let's play some Rock Paper Scissors   ")
answer = ['rock','paper','scissors']
answer2= ['y','n']

def thegame():
    player1input = str(raw_input("P1 Please enter Rock, Paper, Scissors   "))

    while True:
        if player1input.lower() in answer:
            break
        else:
            player1input = str(raw_input("P1 Please enter Rock, Paper, Scissors   "))
            
    player2input= str(raw_input("P2 Please enter Rock, Paper, Scissors   "))

    while True:
        if player2input.lower() in answer:
            break
        else:
            player2input = str(raw_input("P1 Please enter Rock, Paper, Scissors   "))

    player1input = player1input.lower()
    player2input = player2input.lower()

    def result(a,b):
        if a == b:
            return 'It\'s a Tie!'
        elif (a == 'rock' and b == 'scissors') or (a == 'scissors' and b == 'paper') or (a == 'paper' and b == 'rock'):
            return 'player 1 wins!'
        elif (b == 'rock' and a == 'scissors') or (b == 'scissors' and a == 'paper') or (b == 'paper' and a == 'rock'):
            return 'player 2 wins!'
    print result(player1input,player2input)
            

thegame()

again = str(raw_input('Want to play another game? Type Y or N   '))
while True:
    if again.lower() in answer2:
        if again.lower() =='y':
            thegame()
        elif again.lower == 'n':
            print 'Thanks for playing!'
            break
    else:
        again = str(raw_input('Enter Y or N  '))
