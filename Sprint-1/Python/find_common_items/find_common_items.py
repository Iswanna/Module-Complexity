from typing import List, Sequence, TypeVar

ItemType = TypeVar("ItemType")


def find_common_items(
    first_sequence: Sequence[ItemType], second_sequence: Sequence[ItemType]
) -> List[ItemType]:
    """
    Find common items between two arrays.

    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    # 1. Convert second_sequence into a Python set for O(1) lookups
    second_set = set(second_sequence)
    
    # 2. Use a set to keep track of results (handles the "Unique Items" requirement)
    common_items_set: Set[ItemType] = set()

    # 3. Use one loop to go through first_sequence
    for item in first_sequence:
        # 4. Check if the item is in the second_set
        if item in second_set:
            common_items_set.add(item)

    # 5. Convert final set back into a list
    return list(common_items_set)