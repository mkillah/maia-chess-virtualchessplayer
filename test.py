import chess
import chess.engine

# engine = chess.engine.SimpleEngine.popen_uci(r"C:/Users/marko/PycharmProjects/maia-chess-virtualchessplayer/lc0/lc0.exe")
#
# board = chess.Board("r1bqkbnr/p1pp1ppp/1pn5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 2 4")
# info = engine.analyse(board, chess.engine.Limit(depth=1))
# result = engine.play(board, chess.engine.Limit(time=0.1))
# print("Score:", info["score"])
# # Score: PovScore(Mate(+1), WHITE)
# print("Best move:", result.move)
#
# print(board)
# engine.quit()

import subprocess

# Compile the .cpp file
subprocess.run(['g++', 'trainingdata-tool/src/trainingdata-tool.cpp', '-o', 'trainingdata-tool'])

# Run the compiled executable
subprocess.run(['./trainingdata-tool'])
