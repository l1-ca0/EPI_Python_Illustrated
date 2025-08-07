##  The Three Core Patterns

Most binary search problems can be solved using one of three general patterns.

#### Pattern 1: Exact Match Search

This is the classic, textbook binary search. Its goal is to find if a **specific value `k`** exists in an array.

  * **Goal:** Find an index `i` such that `A[i] == k`.

  * **Logic:** At each step, you check `A[mid]`. If it's your target, you're done. If it's too small, you know the target must be to the right. If it's too big, it must be to the left. You can always **discard `mid`** after the check.

  * **Template:**

    ```python
    def exact_match_search(A, k):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == k:
                return mid  # Found it!
            elif A[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return -1 # Not found
    ```

#### Pattern 2: Lower Bound Search (Finding the First)

This is the most common pattern for solving variants. Its goal is to find the **first element that meets a condition**. This is equivalent to finding the first element that is greater than or equal to a target `k` (`>= k`).

  * **Goal:** Find the first index `i` where a condition `is_true(A[i])` is `True`.

  * **Logic:** If `A[mid]` meets the condition, it's a potential answer. But there might be an even earlier one, so you store it and continue searching to the **left**. If it doesn't meet the condition, you must search to the **right**.

  * **Template:**

    ```python
    def lower_bound_search(A, k):
        left, right = 0, len(A)
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] >= k:
                # A[mid] is a potential answer, try for an even better one to the left.
                right = mid
            else:
                # A[mid] is too small, the answer must be to the right.
                left = mid + 1
        # `left` is the insertion point, i.e., the first index >= k.
        return left
    ```

#### Pattern 3: Upper Bound Search (Finding Past the Last)

This pattern is the mirror of the lower bound. Its goal is to find the first element that is **strictly greater** than a target `k` (`> k`). This is useful for finding the insertion point *after* all occurrences of `k`.

  * **Goal:** Find the first index `i` where `A[i] > k`.

  * **Logic:** Similar to the lower bound, but the condition is stricter.

  * **Template:**

    ```python
    def upper_bound_search(A, k):
        left, right = 0, len(A)
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] > k:
                # A[mid] is a potential answer, look for a better one left.
                right = mid
            else:
                # A[mid] is not large enough, answer must be right.
                left = mid + 1
        return left
    ```

-----

## Loop Conditions: `left <= right` vs. `left < right`

This choice is directly tied to the pattern you're using and how you define your search space.

| Feature         | `while left <= right` (Pattern 1)                                                                   | `while left < right` (Patterns 2 & 3)                                                                |
| --------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Search Space** | A **closed interval `[left, right]`**. The loop can run when `left == right` (a 1-element space).      | A **half-open interval `[left, right)`**. The loop stops when `left == right` (an empty space).         |
| **When to Use** | When searching for an **exact match** where you can return from inside the loop.                      | When **converging on a boundary** (first/last element that meets a condition). The answer is found *after* the loop. |
| **Why it Works** | Because you always discard `mid` (`left = mid + 1` or `right = mid - 1`), the loop is guaranteed to terminate. | One branch must be `right = mid` (not `mid - 1`) to avoid skipping over the potential answer, ensuring the loop converges correctly. |

-----

## Solving Variants by Applying Patterns

Most variants are just clever applications of these patterns, especially Pattern 2.

  * **Find First and Last Occurrence of `k`:**

      * **First:** Use Pattern 2 (`lower_bound_search`) to find the first element `>= k`. This gives you the start of the interval.
      * **Last:** Use Pattern 3 (`upper_bound_search`) to find the first element `> k`. The index *before* this (`result - 1`) is the last occurrence of `k`.

  * **Find Square Root of a Number `x`:**

      * This is a binary search on the **answer space**, not an array.
      * **Search Space:** `[0, x]`
      * **Condition:** Is `mid * mid > x`? This creates a monotonic condition: `[F, F, F, T, T, T]`.
      * **Goal:** Find the boundary. This maps perfectly to Pattern 2 or 3.

  * **Search in a Rotated Sorted Array:**

      * This is a modified Pattern 1.
      * At each step, you first determine which half (`[left, mid]` or `[mid, right]`) is normally sorted.
      * Then, you apply the "exact match" logic: check if your target is in the sorted half. If yes, search there. If no, search the other half.