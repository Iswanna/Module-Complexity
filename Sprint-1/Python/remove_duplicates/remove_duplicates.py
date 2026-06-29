from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def remove_duplicates(values: Sequence[ItemType]) -> List[ItemType]:
    """
    Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.

    Time complexity: O(n)
    Space complexity: O(n)
    Optimal time complexity: O(n)
    """
    # 1. Initialize your list and set
    result: List[ItemType] = []
    element_seen: Set[ItemType] = set()

    # 2. Start your loop
    for value in values:
        # 3. Check if we have NOT seen this value yet
        if value not in element_seen:
            # 4. Remember it in the set and add it to the result
            element_seen.add(value)
            result.append(value)
            
    return result
