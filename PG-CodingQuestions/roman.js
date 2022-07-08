const roman = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };

var romanToInt = function (S) {
  let ans = 0;
  for (let i = S.length - 1; ~i; i--) {
    // console.log(i);
    let num = roman[S.charAt(i)];
    console.log(num);
    if (4 * num < ans) ans -= num;
    else ans += num;
  }
  return ans;
};

console.log(romanToInt("MXIII"));
console.log(romanToInt("XIX"));

// https://dev.to/seanpgallivan/solution-roman-to-integer-567f#idea
