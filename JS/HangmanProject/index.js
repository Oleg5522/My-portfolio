import prompt from "picoprompt";
import wordBank from "./word-bank.js";
let W = ["Oleg","Tany","Ola"];


function getRandomWord(wordList) {
    let randomIndex = Math.floor(Math.random()*wordList.length);
    return wordList[randomIndex];
}
let randomWord = getRandomWord(W);
console.log("PC chose "+randomWord);

let output_ = "";
for (let i = 0; i<randomWord.length;i++) {
    output_ += "_";
}
console.log(output_);

let userInput = prompt("Please, enter letter  ")
console.log(userInput);

let row1 = "  -----";
let row2 = " |     |";
let row3 = " |";
let row4 = " |";
let row5 = " |";
console.log(row1);
console.log(row2);
console.log(row3);
console.log(row4);
console.log(row5);
//row3 = row3 + "     o";
console.log(row3 );
row4 = row4 + "    /";
console.log(row4);
row4 = row4 + "|"
console.log(row4);
row4=row4+"\\";
console.log(row4);
row5=row5+"    /";
console.log(row5);
row5=row5+"\\";
let row6 = "     o";
console.log(row5);
console.log(row3,row6);



