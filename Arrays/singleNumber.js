var singleNumber = function (nums) {
  let unique = {};

  for (let i = 0; i < nums.length; i++) {
    if (unique[nums[i]]) {
      delete unique[nums[i]];
      console.log(unique);
    } else {
      unique[nums[i]] = nums[i];
    }
  }

  return unique;
};
console.log(singleNumber([4, 1, 2, 1, 2]));
console.log(singleNumber([2, 2, 1]));
