# Ultimate Tic-Tac-Toe with Monte Carlo Tree Search

This project implements a playable version of **Ultimate Tic-Tac-Toe** using Python. The game features a Monte Carlo Tree Search (MCTS) AI opponent, as well as options to play as a human or against a random move bot.

# Features

- Playable in the terminal with color output.
- Choice between:
  - Human player
  - MCTS AI (configurable move-time)
  - RandomBot (makes random valid moves)
- Fully implemented game logic for Ultimate Tic-Tac-Toe.
- MCTS implementation supports simulation-based decision-making.

The MCTS algorithm simulates many possible games from the current state and chooses the move with the highest average outcome. It balances exploration and exploitation for improved strategy.

# Project Structure

- `play.py` – Main script to run the game
- `utt.py` – Game logic for Ultimate Tic-Tac-Toe
- `MonteCarlo.py` – MCTS implementation
- `human.py` – Human input handler
- `randombot.py` – Random move bot
