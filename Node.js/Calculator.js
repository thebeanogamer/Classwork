var input1 = 1;
var input2 = 2;
var action = "add";
var answer = 0;

if (action.toLowerCase() == "add"){
  answer = input1 + input2;
}
else if (action.toLowerCase() == "subtract") {
  answer = input1 - input2;
}
else if (action.toLowerCase() == "multiply") {
  answer = input1 * input2;
}
else if (action.toLowerCase() == "divide") {
  answer = input1 / input2;
}
else {
  answer = "Unrecognised Action";
}

console.log(answer);
