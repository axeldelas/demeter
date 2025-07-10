# 🎮 Demeter Game – Reach the End, Outsmart the AI

Demeter is a minimalist yet strategic board game developed in Python. Inspired by the core mechanics of chess, the game replaces the complexity of piece types with a simple but clever goal: Advance your pawns to the opposite side of the board before the AI does.\

Unlike chess, there are no kings, queens, or checkmates. The only rule is: move forward and reach the other side first

# 🕹️ Gameplay Overview

• You control a row of pawns starting on your baseline.

• The AI opponent controls its own pawns on the opposite side.

• Each pawn can:

&nbsp;&nbsp;&nbsp;&nbsp;• Move forward one square.

&nbsp;&nbsp;&nbsp;&nbsp;• Jump over any adjacent pawn (your own or the AI’s), as long as the landing square is free.

• You win by getting any one of your pawns to reach the opponent’s baseline (the last row).

# 🤖 Naive but Clever AI

The AI in Demeter is naive, but not random. It evaluates all of its possible legal moves each turn and selects the one that brings it closest to the goal.

• It uses a simple heuristic: prioritize moves that advance its pawns furthest.

• It does not predict your moves or counter advanced strategies, but it does not play blindly either.

•  As a result, it can create surprising pressure if you don’t block or outpace it.

# ⚙️ Features

•  Developed fully in Python

•  Turn-based logic with clear board display in the terminal

•  Clean codebase using Object-Oriented Programming

•  Smart move validation and victory detection

•  AI move analyzer evaluates all actions each turn to choose the optimal advance

# 🚀 How to Play

To start the game, simply run the main script:\

`python demeter.py`\

No installation or setup is required — just Python 3.x.

# 🙌 Credits

Thank you for checking out my project!\
Feel free to use it, explore it, and have fun! 😊
