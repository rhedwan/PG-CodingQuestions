function convert(s, numRows) {
  if (numRows === 1) return s;
  let result = "";
  for (let r = 0; r < numRows; r++) {
    const increment = 2 * (numRows - 1);
    for (let i = r; i < s.length; i += increment) {
      result += s[i];
      console.log(i + increment - 2 * r);
      if (r > 0 && r < numRows - 1 && i + increment - 2 * r < s.length) {
        result += s[i + increment - 2 * r];
      }
    }
  }
  console.log(result);
  return result;
}

convert("PAYPALISHIRING", 4);
