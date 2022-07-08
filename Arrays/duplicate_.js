var containsDuplicate = function (nums) {
  let unique = {};
  for (let i = 0; i < nums.length; i++) {
    if (unique[nums[i]]) {
      return true;
    } else {
      unique[nums[i]] = "exist";
    }
  }
  return false;
};

console.log(containsDuplicate([2, 36, 5, 2, 2, 3, 4, 4, 4, 32, 23, 3]));
console.log(containsDuplicate([1, 5, 2]));
console.log(containsDuplicate([1, 5, 2, 2]));
