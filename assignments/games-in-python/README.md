
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game using Python strings, loops, conditionals, random selection, and user input. Players should guess letters to reveal a hidden word before they run out of incorrect guesses.

## 📝 Tasks

### 🛠️ Select a Secret Word and Set Up the Game

#### Description
Use the provided list of words to select a random secret word. Initialize the variables needed to track guessed letters, incorrect guesses, and the maximum number of incorrect guesses allowed.

#### Requirements
Completed program should:

- Use `random.choice()` to select one word from the provided `words` list.
- Store the selected word in a variable named `secret_word`.
- Create variables to track guessed letters and the number of incorrect guesses.
- Set a clear maximum number of incorrect guesses before the player loses.

### 🛠️ Display Progress and Process Guesses

#### Description
Create a game loop that shows the player which letters have been revealed, asks for a letter guess, and updates the game state after each guess.

#### Requirements
Completed program should:

- Display the secret word with unguessed letters shown as underscores, such as `_ _ _ _ _ _`.
- Prompt the player to enter one letter using `input()`.
- Reveal correctly guessed letters in every matching position in the word.
- Record incorrect guesses and display how many guesses remain.
- Prevent repeated guesses from changing the number of incorrect guesses.

### 🛠️ End the Game and Report the Result

#### Description
Finish the game when the player has guessed every letter in the secret word or has used all allowed incorrect guesses. Display a message that clearly reports the result.

#### Requirements
Completed program should:

- End the loop when every letter in `secret_word` has been guessed.
- End the loop when the player reaches the maximum number of incorrect guesses.
- Display a win message when the player reveals the full word.
- Display a lose message that includes the secret word when no guesses remain.
