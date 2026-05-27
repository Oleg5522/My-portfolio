# Hangman Game

A console-based Hangman game built with JavaScript and Node.js.

## What it does

- Picks a random word from a bank of 800+ words
- Displays blanks representing the letters of the word
- Draws the gallows step by step with each wrong guess
- Tracks letters already guessed and warns if the same letter is entered twice
- Counts remaining attempts and shows them after each move
- Announces win or loss at the end and shows the correct word
- Keeps score across multiple games (wins and losses)
- Offers to play again after each round

## Technologies

- JavaScript (ES6+)
- Node.js
- [picoprompt](https://www.npmjs.com/package/picoprompt) — for reading user input in the terminal

## How to run

Make sure Node.js is installed, then in the terminal:

```bash
npm install
node Gallows4.js
```

## Project structure

| File | Description |
|------|-------------|
| `Gallows4.js` | Main game file |
| `word-bank.js` | List of 800+ words to guess |
| `index.js` | Early prototype (not the final version) |
| `experiment.js` | Initial experiments and scratch work |

## Notes

This is a course project completed as part of a JavaScript fundamentals course.