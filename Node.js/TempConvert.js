// Defines a constant to store the tempreture in kelvin
const kelvin = 0;

// Subtracts 273 from the tempreture in Kelvin to calculate the tempreture in Celcius
const celcius = kelvin - 273;

// Converts celcius to fahrenheit
var fahrenheit = celcius * (9/5) + 32;

// Rounds Fahrenheit down
fahrenheit = Math.floor(fahrenheit);

console.log("The temperature is " + fahrenheit + " degrees Fahrenheit.")
