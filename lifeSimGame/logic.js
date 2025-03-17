var MonthlySalary = 0;
var balance = 0;
var saving = 0;
var month = 1;

document.getElementById("monthlySalary").innerHTML(MonthlySalary)

function calculateExpense(expense) {
  if (expense > MonthlySalary) {
    alert("You Trippin-you cant afford this.");
  } else {
    var newBalance = expense - MonthlySalary;
    return newBalance;
  }
}
