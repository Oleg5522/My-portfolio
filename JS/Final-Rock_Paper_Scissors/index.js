!(function() {
 
    let choise = ["Rock", "Paper", "Scissors"];
    let images = {
        "Rock": "https://images.pexels.com/photos/1093207/pexels-photo-1093207.jpeg?cs=srgb&dl=pexels-pille-kirsi-222198-1093207.jpg&fm=jpg&_gl=1*1j5d19u*_ga*MTE2Njc3NTM0NS4xNzM0ODQyMzcw*_ga_8JE65Q40S6*MTczNDg0MjM2OS4xLjEuMTczNDg0MjM4MS4wLjAuMA..",
        "Paper": "https://images.pexels.com/photos/8533218/pexels-photo-8533218.jpeg?cs=srgb&dl=pexels-anna-nekrashevich-8533218.jpg&fm=jpg&_gl=1*lo4v5z*_ga*MTE2Njc3NTM0NS4xNzM0ODQyMzcw*_ga_8JE65Q40S6*MTczNDg0MjM2OS4xLjEuMTczNDg0MjU2MC4wLjAuMA..",
        "Scissors": "https://images.pexels.com/photos/4226896/pexels-photo-4226896.jpeg?cs=srgb&dl=pexels-karolina-grabowska-4226896.jpg&fm=jpg&_gl=1*10itz7m*_ga*MTE2Njc3NTM0NS4xNzM0ODQyMzcw*_ga_8JE65Q40S6*MTczNDg0MjM2OS4xLjEuMTczNDg0MjY1NS4wLjAuMA..",
    };

    let selection = document.getElementById("selection");
    let result_on_screen = document.getElementById("result_on_screen");
    let result_text = document.getElementById("result-text");
    let again = document.getElementById("again");
    let choose = document.querySelectorAll(".choose");
    
    let your_choise = document.getElementById("your_choise");
    
    let PC_choise = document.getElementById("PC_choise");

    
    choose.forEach(button => {
        button.addEventListener("click",handleChoise);
    });
    again.addEventListener("click", resetGame);

    function handleChoise(event) {
        let user_choise = event.target.dataset.choise;

        let computerChoise = getComputerChoise();
        let winner = getWinner(user_choise, computerChoise);

        displayResult(user_choise,computerChoise,winner);
    }

    function getComputerChoise() {
        const randomIndex = Math.floor(Math.random()*choise.length);
        return choise[randomIndex];
    }

    function getWinner(user_choise,computerChoise) {
        if (user_choise === computerChoise) {
            return 'draw';
        } else if (
            (user_choise === "Rock" && computerChoise === "Scissors") ||
            (user_choise === "Paper" && computerChoise === "Rock") ||
            (user_choise === "Scissors" && computerChoise === "Paper")
        ) {
            return "user";

        } else {
            return "computer";
        }
    }

    function displayResult(user_choise, computerChoise,winner) {
        selection.classList.add("hidden");
        result_on_screen.classList.remove("hidden");
    
        your_choise.src = images[user_choise];
        
        PC_choise.src=images[computerChoise];


        if (winner === 'draw') {
            result_text.innerText = `There is draw! You and your PC chose ${user_choise}.`;
        } else if (winner === 'user') {
            result_text.innerText = `You won! ${user_choise} beats ${computerChoise}.`;
        } else {
            result_text.innerText = `You lost! ${computerChoise} beats ${user_choise}`;
        }


    }

    function resetGame() {
        selection.classList.remove('hidden');
        result_on_screen.classList.add('hidden');
    }

}

)();