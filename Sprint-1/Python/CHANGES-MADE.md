# Sprint 1: Complexity Analysis & Refactoring (Python)

## 1. calculate_sum_and_product.py
| Feature | Original Code | Refactored Code |
| :--- | :--- | :--- |
| **Time Complexity** | **Linear $O(n)$** | **Linear $O(n)$** |
| **Why?** | Two separate `for` loops ($n + n$). | Combined into a single `for` loop ($n$). |
| **Space Complexity** | **Constant $O(1)$** | **Constant $O(1)$** |
| **Why?** | Used two scalar variables. | Used two scalar variables. |

**Note:** Renamed the variable `sum` to `total_sum` to avoid shadowing Python's built-in `sum()` function.

---

## 2. find_common_items.py
| Feature | Original Code | Refactored Code |
| :--- | :--- | :--- |
| **Time Complexity** | **Quadratic $O(n \times m)$** | **Linear $O(n + m)$** |
| **Why?** | Nested loops searching a **list** with the `in` keyword ($O(m)$). | Used a **set** for $O(1)$ membership lookups with the `in` keyword. |
| **Space Complexity** | **Constant $O(1)$** | **Linear $O(m)$** |
| **Why?** | No extra storage created. | Created a `set` to store the second sequence for fast lookups. |

---

## 3. has_pair_with_sum.py
| Feature | Original Code | Refactored Code |
| :--- | :--- | :--- |
| **Time Complexity** | **Quadratic $O(n^2)$** | **Linear $O(n)$** |
| **Why?** | Nested loops comparing every index. | Single pass with a `set` to find the `remaining_number_needed`. |
| **Space Complexity** | **Constant $O(1)$** | **Linear $O(n)$** |
| **Why?** | No extra storage used. | Created a `seen` set to store visited numbers. |

---

## 4. remove_duplicates.py
| Feature | Original Code | Refactored Code |
| :--- | :--- | :--- |
| **Time Complexity** | **Quadratic $O(n^2)$** | **Linear $O(n)$** |
| **Why?** | Nested loops checking if an item was `not in` the result **list**. | Used an `element_seen` **set** for $O(1)$ "already seen" checks. |
| **Space Complexity** | **Linear $O(n)$** | **Linear $O(n)$** |
| **Why?** | Stored unique items in a list. | Stored items in both a result list (for order) and a set (for speed). |

---

### Key Python Takeaways

1.  **The `in` Keyword Efficiency:** In Python, the `in` operator is very readable, but its speed depends on the container. Checking `in` for a **list** is $O(n)$, while checking `in` for a **set** is $O(1)$. Leveraging this difference allowed me to optimize three of the four tasks.
2.  **Space-Time Trade-off:** To improve the runtime of `find_common_items`, `has_pair_with_sum`, and `remove_duplicates` from $O(n^2)$ to $O(n)$, I utilized extra memory (Space) by creating Python **sets**.
3.  **Built-in Shadowing:** I learned to be careful with variable naming (e.g., using `total_sum` instead of `sum`) to avoid overwriting Python’s built-in functions.
4.  **Preserving Order:** In `remove_duplicates`, I learned that while sets are fast, they don't preserve order. Using a list for results and a set for tracking allowed for both $O(n)$ speed and correct ordering.

