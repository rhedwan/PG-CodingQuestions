var plusOne = function (digits) {
  let number = String(+digits.join("") + 1);
  let newArray = number.split("");
  return newArray;
};

console.log(plusOne([1, 2, 3]));
