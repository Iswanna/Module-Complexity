This is a great way to document your learning and show the impact of your refactoring. Below is the content for your `changes-made.md` file, formatted exactly like the comparison table you provided.

---

# Sprint 1: Complexity Analysis & Refactoring

## 1. calculateSumAndProduct.js
| Feature | Original Code | Refactored Code |
| :--- | :--- | :--- |
| **Time Complexity** | **Linear $O(n)$** | **Linear $O(n)$** |
| **Why?** | Two separate loops ($n + n$). | Combined into a single loop ($n$). |
| **Space Complexity** | **Constant $O(1)$** | **Constant $O(1)$** |
| **Why?** | Only two scalar variables used. | Only two scalar variables used. |

---

## 2. findCommonItems.js
| Feature | Original Code | Refactored Code |
| :--- | :--- | :--- |
| **Time Complexity** | **Quadratic $O(n \times m)$** | **Linear $O(n + m)$** |
| **Why?** | Nested loop: `.includes()` inside `.filter()`. | Set lookup: `.has()` inside `.filter()`. |
| **Space Complexity** | **Constant $O(1)$** | **Linear $O(m)$** |
| **Why?** | No extra search structure created. | Created a `Set` to store the second array. |

---

## 3. hasPairWithSum.js
| Feature | Original Code | Refactored Code |
| :--- | :--- | :--- |
| **Time Complexity** | **Quadratic $O(n^2)$** | **Linear $O(n)$** |
| **Why?** | Nested `for` loops comparing every pair. | One loop with instant "Complement" lookup. |
| **Space Complexity** | **Constant $O(1)$** | **Linear $O(n)$** |
| **Why?** | No extra storage used. | Created a `Set` to store visited numbers. |

---

## 4. removeDuplicates.js
| Feature | Original Code | Refactored Code |
| :--- | :--- | :--- |
| **Time Complexity** | **Quadratic $O(n^2)$** | **Linear $O(n)$** |
| **Why?** | Nested loop searching the result array. | One loop using a Set for "Seen" items. |
| **Space Complexity** | **Linear $O(n)$** | **Linear $O(n)$** |
| **Why?** | Stored unique items in an array. | Stored unique items in both an array and a Set. |

---

### Key Takeaway: The Space-Time Trade-off
In the `findCommonItems.js`, `hasPairWithSum.js` and `removeDuplicates.js` tasks, I successfully reduced the **Time Complexity** from Quadratic to Linear. I did this by choosing a **Set** instead of an **Array** for searching. This is a classic "Space-Time Trade-off": I used a bit more memory (Space) to make the program run significantly faster (Time).

