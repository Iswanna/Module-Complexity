/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const numbersSet = new Set();
  
  for (let i=0; i<numbers.length; i++) {
    const remainingNumberNeeded = target - numbers[i];
    if (numbersSet.has(remainingNumberNeeded)) {
      return true;
    } else {
      numbersSet.add(numbers[i]);
    }
  }
  return false;
}
