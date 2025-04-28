from typing import List, Dict, Any


board: List = [
			   "O", "X", "O", 
			   "X", "X", "O", 
			   "X", "X", None
   			  ]


class Players():
	x = "X"
	o = "O"

class GameState():
	x_won = "X_WON"
	o_won = "O_WON"
	draw = "DRAW"


def get_result(player: Players, game_state:GameState, board: List) -> GameState:

	if (board[0] == board[1] == board[2]==player.x or board[3] == board[4] == board[5]==player.x or board[6] == board[7] == board[8]==player.x 
		or board[0] == board[3] == board[6]==player.x  or board[1] == board[4] == board[7]==player.x  or board[2] == board[5] == board[8]==player.x 
		or board[0]==board[4] == board[8]==player.x  or board[2] == board[4] == board[5]==player.x) : 
		return game_state.x_won

	elif (board[0] == board[1] == board[2]==player.o or board[3] == board[4] == board[5]==player.o or board[6] == board[7] == board[8]==player.o 
		or board[0] == board[3] == board[6]==player.o  or board[1] == board[4] == board[7]==player.o  or board[2] == board[5] == board[8]==player.o 
		or board[0]==board[4] == board[8]==player.o  or board[2] == board[4] == board[5]==player.o) : 
		return game_state.o_won

	else:
		return game_state.draw


players = Players()
game_state = GameState()

print(get_result(players, game_state, board))
