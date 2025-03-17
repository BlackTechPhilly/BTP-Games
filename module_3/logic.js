let salary = 3000;
let balance = salary;
let savings = 0;
let month = 1;

function spend(amount) {
    if (balance >= amount) {
        balance -= amount;
        document.getElementById("balance").textContent = balance;
    } else {
        alert("Not enough balance for this expense!");
    }
}

function nextMonth() {
    savings += balance; 
    balance = salary; 
    month++;
    
    document.getElementById("balance").textContent = balance;
    document.getElementById("moneySaved").textContent = savings;
    document.getElementById("month").textContent = month;
}


// function randomEvent() {
//     const events = [
//         { name: "Nothing happens", cost: 0 },
//         { name: "Car repair", cost: 300 },
//         { name: "Medical bill", cost: 500 },
//         { name: "House repair", cost: 400 },
//         { name: "Lost wallet", cost: 100 }
//     ];
    
//     let event = events[Math.floor(Math.random() * events.length)];
    
//     if (event.cost > 0) {
//         alert(`Random Event: ${event.name} - You lost $${event.cost}`);
//         balance -= event.cost;
//         if (balance < 0) balance = 0;
//     } else {
//         alert("Random Event: Nothing happened this time.");
//     }
    
//     document.getElementById("balance").textContent = balance;
// }