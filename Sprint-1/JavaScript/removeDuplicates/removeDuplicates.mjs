/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const result = [];
  const elementSeen = new Set();

  for (let i=0; i<inputSequence.length; i++) {
    if (!elementSeen.has(inputSequence[i])) {
      elementSeen.add(inputSequence[i]);
      result.push(inputSequence[i]);
    }
  }
  return result;
}
