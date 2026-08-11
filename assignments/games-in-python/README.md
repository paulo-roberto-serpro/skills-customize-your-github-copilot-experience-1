
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game in Python that practices string manipulation, control flow, and user input handling. Students will implement the game loop, word selection, and win/lose conditions.

## 📝 Tasks

### 🛠️	Basic Hangman

#### Description
Implement a playable Hangman game that runs in the terminal. The program should select a random word, display masked letters, accept letter guesses, and track remaining attempts until the player wins or loses.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (at least 10 words)
- Display current progress with underscores for unknown letters (e.g., `_ a _ _ m a n`)
- Accept single-letter input (case-insensitive) and reveal matching letters
- Maintain and display a list of incorrect guesses
- Limit attempts (configurable, default 6) and end the game when attempts reach zero
- Print a clear win or loss message and reveal the word


### 🛠️	Extras (Optional)

#### Description
Add optional features to improve user experience and increase challenge.

#### Requirements
Completed program may:

- Add difficulty levels that adjust the number of attempts
- Show simple ASCII-art hangman corresponding to remaining attempts
- Allow replaying the game without restarting the program
- Load words from an external file (e.g., `words.txt`)

