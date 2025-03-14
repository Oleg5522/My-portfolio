let W = ["Olege","Teaney","Oelae"];


function getRandomWord(wordList) {
    let randomIndex = Math.floor(Math.random()*wordList.length);
    return wordList[randomIndex];
}
let randomWord = getRandomWord(W);
console.log("PC chose "+randomWord);
let output_ = "";
for (let i = 0; i<randomWord.length;i++) {
    output_ += "_ ";
}
console.log(output_);
let yourLetter = "e";
let n = randomWord.index;
if (yourLetter == randomWord[n]) {
    output_.replace(output_[index(randomWord[n]), randomWord[n]])
console.log(output_);
}
if (randomWord.includes(yourLetter)) {
    let index = randomWord.indexOf(yourLetter);
    console.log(index);
}

function replaceAllGessedLetters(randomWord, yourLetter) {
    let indexes = [];
    for (let m = 0; m<randomWord.length; m++) {
        if (randomWord[m===yourLetter]){
            indexes.push(m);
        }
        
    }
}
return indexes;
console.log(indexes);