print("ROCK-PAPER-SCISSOR GAME")
player1=input("Player1: ")
player2=input("Player2: ")
if (player1=="ROCK" or player1=="Rock" or player1=="rock") and (player2=="paper" or player2=="PAPER" or player2=="Paper"):
    print("player2 WINS")
elif (player1=="ROCK" or player1=="Rock" or player1=="rock") and (player2=="scissor" or player2=="SCISSOR" or player2=="Scissor"):
    print("player1 WINS")
elif (player1=="paper" or player1=="PAPER" or player1=="Paper") and (player2=="ROCK" or player2=="Rock" or player2=="rock"):
    print("player1 WINS")
elif (player1=="paper" or player1=="PAPER" or player1=="Paper") and (player2=="scissor" or player2=="SCISSOR" or player2=="Scissor"):
    print("player2 WINS")
elif (player1=="scissor" or player1=="SCISSOR" or player1=="Scissor") and (player2=="ROCK" or player2=="Rock" or player2=="rock"):
    print("player2 WINS")
elif (player1=="scissor" or player1=="SCISSOR" or player1=="Scissor") and (player2=="paper" or player2=="PAPER" or player2=="Paper"):
    print("player1 WINS")
else:
    print("CLASH")
    


