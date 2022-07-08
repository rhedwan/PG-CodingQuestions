// var rotate = function (nums, k) {
//   let pointer = k % nums.length;
//   let arr = [];
//   for (let i = 0; i < nums.length; i++) {
//     arr[(i + pointer) % nums.length] = nums[i];
//   }
//   console.log(arr);
//   return arr;
// };

// rotate([1, 2, 3, 4, 5, 6, 7], 3);
// rotate([-1, -100, 3, 99], 2);
var rotate = function (nums, k) {
  let pointer = k % nums.length;
  let arr = [];
  for (let i = 0; i < nums.length; i++) {
    arr.splice((i + pointer) % nums.length, 0, nums[i]);
  }
  nums = arr;
  return nums;
};
console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3));
