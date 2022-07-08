function mergeSortedArray(array1, array2) {
  const mergeArray = [];
  let array1Item = array1[0];
  let array2Item = array2[0];
  let i = 1;
  let j = 1;
  if (array1.length === 0) {
    return array2;
  }
  if (array2.length === 0) {
    return array1;
  }
  while (array1Item || array2Item) {
    console.log(array1Item, array2Item);
    if (!array2Item || array1Item < array2Item) {
      mergeArray.push(array1Item);
      array1Item = array1[i];
      i++;
    } else {
      mergeArray.push(array2Item);
      array2Item = array2[j];
      j++;
    }
  }
  console.log(mergeArray);
  return mergeArray;
}

// mergeSortedArray([0, 3, 4, 31], [4, 6, 30]);
mergeSortedArray([40, 67], [30]);
