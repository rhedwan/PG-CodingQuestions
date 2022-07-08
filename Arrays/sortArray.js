function sortArray(nums) {
  const unique = [...new Set(nums)].sort((a, b) => a - b);
  // const newArray = [];
  // for (let i = 0; i < nums.length; i++) {
  //   if (i < unique.length) {
  //     newArray.push(unique[i]);
  //   } else {
  //     newArray.push("_");
  //   }
  // }
  console.log(unique);
  return unique;
}
var removeDuplicates = function (nums) {
  // Length of the updated array
  let count = 0;
  // Loop for all the elements in the array
  for (let i = 0; i < nums.length; i++) {
    // If the current element is equal to the next element, we skip
    if (i < nums.length - 1 && nums[i] == nums[i + 1]) {
      continue;
    }
    // We will update the array in place
    nums[count] = nums[i];
    count++;
  }
  return count;
};

sortArray([1, 1, 2]);
sortArray([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]);
sortArray([0, 0, 9, 1, 1, 1, 2, 2, 3, 3, 4]);
sortArray([0, 0, 1, 188, 1, 2, 2, 3, 3, 4]);
