const isPalindrome = function (x) {
  let num = String(x);
  let left = 0;
  let right = num.length - 1;
  while (left < right) {
    if (num[left] !== num[right]) {
      return false;
    }
    left += 1;
    right -= 1;
  }
  return true;
};

isPalindrome(121);
isPalindrome(123);
