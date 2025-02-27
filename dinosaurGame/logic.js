let dino = document.getElementById("dino");
let obstacle = document.getElementById("obstacle");
let scoreDisplay = document.getElementById("score");
let score = 0;
let jumping = false;

document.addEventListener("keydown", function(event) {
    if (event.code === "Space" && !jumping) {
        jump();
    }
});

function jump() {
    jumping = true;
    let position = 0;
    let upInterval = setInterval(() => {
        if (position >= 100) {
            clearInterval(upInterval);
            let downInterval = setInterval(() => {
                if (position <= 0) {
                    clearInterval(downInterval);
                    jumping = false;
                }
                dino.style.bottom = position + "px";
                position -= 5;
            }, 20);
        }
        dino.style.bottom = position + "px";
        position += 5;
    }, 20);
}

function moveObstacle() {
    let obstaclePosition = 600;
    let obstacleInterval = setInterval(() => {
        if (obstaclePosition < 0) {
            obstaclePosition = 600;
            score += 10;
            scoreDisplay.innerText = score;
        }
        
        let dinoBottom = parseInt(window.getComputedStyle(dino).getPropertyValue("bottom"));
        if (obstaclePosition < 90 && obstaclePosition > 50 && dinoBottom <= 40) {
            alert("Game Over! Your score: " + score);
            clearInterval(obstacleInterval);
            location.reload();
        }
        
        obstacle.style.right = (600 - obstaclePosition) + "px";
        obstaclePosition -= 5;
    }, 20);
}

moveObstacle();