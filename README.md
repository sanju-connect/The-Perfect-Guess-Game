# 🎯 Guess The Number Game

A simple **Guess The Number** game made with Python.
The computer randomly selects a number between **1 and 100**, and the player has to guess it.

After every guess, the game gives a hint:

* 🔽 **Lower Number Please** — if your guess is too high
* 🔼 **Higher Number Please** — if your guess is too low
* 🎉 The game ends when you guess the correct number

## 🛠️ Requirements

* Python 3.x
* No external libraries are required.

The game uses Python's built-in `random` module.

## 🚀 How to Run

1. Make sure Python is installed on your computer.
2. Save the code in a file, for example:

```text
guess_the_number.py
```

3. Open a terminal in the folder containing the file.
4. Run:

```bash
python guess_the_number.py
```

## 🎮 How To Play

1. The computer chooses a random number from **1 to 100**.
2. Enter your guess when prompted.
3. The game tells you whether you need to guess higher or lower.
4. Keep guessing until you find the correct number.
5. Your total number of attempts is displayed at the end.

### Example

```text
Guess The Number: 50
Higher Number Please

Guess The Number: 75
Lower Number Please

Guess The Number: 63
Higher Number Please

Guess The Number: 68
You Have Guessed The Number, 68 Correctly in 4 Attempt
```

## 📌 Features

* Random number generation
* Interactive user input
* Higher/lower hints
* Attempt counter
* Simple command-line gameplay

## 📂 Project Structure

```text
Guess-The-Number/
│
├── guess_the_number.py
└── README.md
```

## 💡 Future Improvements

Some ideas you could add later:

* Add different difficulty levels
* Limit the number of guesses
* Handle invalid inputs
* Add a play-again option
* Add a scoring system
* Add a GUI version using Tkinter

## 👨‍💻 About

This is a beginner-friendly Python project created to practice:

* `random`
* `while` loops
* `if / elif / else`
* User input
* Variables
* Basic game logic

---

⭐ **If you enjoyed the game, try to guess the number in as few attempts as possible!**
