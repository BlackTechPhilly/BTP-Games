const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
canvas.width = 600;
canvas.height = 400;

const keys = ["A", "S", "D", "F"];
const keyPositions = [100, 200, 300, 400];
let notes = [];
let score = 0;

// Generate falling notes
function createNote() {
    const index = Math.floor(Math.random() * keys.length);
    notes.push({ x: keyPositions[index], y: 0, key: keys[index] });
}

// Update game state
function update() {
    notes.forEach(note => note.y += 5);
    notes = notes.filter(note => note.y < canvas.height);
}

// Draw game elements
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw keys
    keys.forEach((key, index) => {
        ctx.fillStyle = "gray";
        ctx.fillRect(keyPositions[index], canvas.height - 50, 50, 50);
        ctx.fillStyle = "white";
        ctx.fillText(key, keyPositions[index] + 20, canvas.height - 20);
    });
    
    // Draw notes
    notes.forEach(note => {
        ctx.fillStyle = "red";
        ctx.fillRect(note.x, note.y, 50, 20);
    });
    
    // Draw score
    ctx.fillStyle = "white";
    ctx.fillText("Score: " + score, 20, 30);
}

// Handle key presses
window.addEventListener("keydown", (e) => {
    notes.forEach((note, index) => {
        if (e.key.toUpperCase() === note.key && note.y > canvas.height - 70 && note.y < canvas.height - 30) {
            score += 10;
            notes.splice(index, 1);
        }
    });
});

// Game loop
function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

// Start the game
setInterval(createNote, 1000);
gameLoop();
