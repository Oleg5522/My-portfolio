import prompt from "picoprompt";
import wordBank from "./word-bank.js";

let NumberOfGamesWon = 0;
let NumberOfGamesLost = 0;

function getRandomWord(listOfWords) {
    const randomIndex = Math.floor(Math.random()*listOfWords.length);
    return listOfWords[randomIndex];
}

function updateGuessedWord(word, GuessedArray, yourLetter) {
    for (let i=0; i<word.length; i++) {
        //console.log(word[i]);
        if (word[i]===yourLetter) {
            GuessedArray[i] = yourLetter;
            console.log("You are right!");
        }
    } return GuessedArray;
}
//let yourLetter = "";

function hangman(unsuccessfulAttempts) {
    const hangingLevels = [ 
        "--------\n|      |      \n|\n|\n|\n|", "--------\n|      |\n|      O\n|\n|\n|", "--------\n|      |\n|      O\n|     /\n|\n|", "--------\n|      |\n|      O\n|     /|\n|\n|",
        "--------\n|      |\n|      O\n|     /|\\\n|\n|","--------\n|      |\n|      O\n|     /|\\\n|     /\n|","--------\n|      |\n|      O\n|     /|\\\n|     / \\\n|",
    ]
    console.log(hangingLevels[unsuccessfulAttempts]);
}
hangman();

function play() {
    const word = getRandomWord(wordBank);
    let guessedLetters = [];
    let unsuccessfulAttempts = 0;
    const maximumNumberOfAttempts = 6;
    let yourLetter = "";
    let GuessedArray = Array(word.length).fill('_');

    console.log(GuessedArray.join(' '));

    while (unsuccessfulAttempts<maximumNumberOfAttempts) {
        console.clear();
        const greteeng = `Hello!
        We welcome you to the game "Hangman". You will be asked to guess the random word that the computer has guessed.
        You have six attempts, the length of each word does not exceed 6 letters. As you guess the letters, 
        the symbols in the word will be decoded. After the game is over, you will be asked to play again.
        You can stop the game at any time by pressing the key combination "Ctrl + C". Good luck!`
        console.log(greteeng);
        //console.log(unsuccessfulAttempts,maximumNumberOfAttempts,unsuccessfulAttempts);
        hangman(unsuccessfulAttempts);
        let answer = updateGuessedWord(word,GuessedArray,yourLetter);
        console.log(answer.join(" "));
        console.log(`You have ${maximumNumberOfAttempts-unsuccessfulAttempts} attempts left.`);

        yourLetter = prompt("Enter your letter ").toLowerCase();

        if (guessedLetters.includes(yourLetter)) {
            console.log("You have already written this letter, try another one.");
            continue;
        }
        console.log("You have already written this letter, try another one.");
        guessedLetters.push(yourLetter);

        if (word.includes(yourLetter)) {
            console.log("You are right!");
            if (word.split("").every(i=>guessedLetters.includes(i))) {
                console.clear();
                //console.log("You are right!");
                hangman(unsuccessfulAttempts);
                console.log(answer.join(" "));
                console.log("You guessed whole word! The whole word is ", word,".");
                NumberOfGamesWon++;
                break;
            } 
            
        }   else {
                unsuccessfulAttempts++;
                console.log("You are not right.");
        }
    }  

        if (unsuccessfulAttempts===maximumNumberOfAttempts) {
            console.clear();
            //console.log(unsuccessfulAttempts);
            hangman(unsuccessfulAttempts);
            console.log("You are lost. Random word was ", word);
            NumberOfGamesLost++;
        }
        console.log(`Number Of Games Won: ${NumberOfGamesWon} and Number Of Games Lost: ${NumberOfGamesLost}`);

        let willing = prompt(`If you would like try again, just type "Yes"`).toLowerCase();
        //console.log(willing);

        if (willing==="yes") {

            play();
        }
    }

play();