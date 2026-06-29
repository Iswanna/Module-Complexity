from typing import List, Set, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    # 1. Initialize an empty set called seen.
    seen: Set[Number] = set()

    # 2. Loop through each num in the numbers list.
    for num in numbers:
        # 3. Calculate the remaining_number_needed (the missing piece).
        remaining_number_needed = target_sum - num

        # 4. Check: if remaining_number_needed in seen.
        if remaining_number_needed in seen:
            return True

        # 5. If not, add the current num to the set.
        seen.add(num)

    # 6. If the loop finishes, return False.
    return False
