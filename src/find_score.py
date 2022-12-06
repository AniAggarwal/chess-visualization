import chess.engine
import chess.pgn

pgn = open("../data/Carlsen, Magnus.pgn")
first_game = chess.pgn.read_game(pgn)
print("Game: ", first_game.headers["Event"])

board = first_game.board()

engine = chess.engine.SimpleEngine.popen_uci(
    "../stockfish_15.1_linux_x64_avx2/stockfish-ubuntu-20.04-x86-64-avx2"
)

for move in first_game.mainline_moves():
    print("Doing move: ", move)
    board.push(move)
    info = engine.analyse(board, chess.engine.Limit(time=5))
    print(info["score"])
    input("Continue?")

