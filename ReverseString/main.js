/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/
// const str1 = "creature";
// const expected1 = "erutaerc";

// const str2 = "dog";
// const expected2 = "god";

// const str3 = "hello";
// const expected3 = "olleh";

// const str4 = "";
// const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */

 const str1 = "creature";
 const expected1 = "erutaerc";
 
 const str2 = "dog";
 const expected2 = "god";
 
 const str3 = "hello";
 const expected3 = "olleh";
 
 const str4 = "";
 const expected4 = "";
 
function reverseString(str) {
  return str.split("").reverse().join("");
}

var a= reverseString(str1);
var b= reverseString(str2);
var c= reverseString(str3);
var d= reverseString(str4);

console.log(a)
console.log(b)
console.log(c)
console.log(d)
