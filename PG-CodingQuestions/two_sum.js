const twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let x = 1; x < nums.length; x++) {
      //   console.log(i, x);
      //   if (!(i <= x)) {
      const value = nums[i] + nums[x] === target;
      if (value) {
        console.log([x, i]);
        return [x, i];
      }
      //   }
    }
  }
};

twoSum([2, 7, 11, 15], 9);
twoSum([2, 5, 5, 11], 10);
twoSum([2, 5, 56, 4, 646, 3, 5, 10, 5, 11], 14);
