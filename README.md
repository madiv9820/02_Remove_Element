# [Remove Element 🡽](https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150)

***Topics:-*** 🧮 **Array**, 🔁 **Two Pointers**

#### 📌 **What’s the task?**

You're given:

- 📊 An **integer array** called `nums`
- 🎯 An **integer value** called `val`

You need to:

- 🧽 **Remove all occurrences of** `val` **from** `nums`, **in-place**
- 🔢 Return the number `k`, which is the **count of elements not equal to** `val`
- ✅ Ensure the **first `k` elements in** `nums` contain the elements that are **not equal to** `val`
- 🔀 The **order doesn’t matter**
- 🚫 Anything beyond the first `k` elements can be **ignored** (garbage, underscores, etc.)

#### 📚 **Examples**

- **Input:** `nums = [3,2,2,3]`, `val = 3`  
  👉 Remove all `3`s  
  ✅ Possible output: `nums = [2,2,_,_]`  
  ✅ Return `k = 2`  
  ℹ️ Underscores represent irrelevant values.

- **Input:** `nums = [0,1,2,2,3,0,4,2]`, `val = 2`  
  👉 Remove all `2`s  
  ✅ Possible output: `nums = [0,1,4,0,3,_,_,_]`  
  ✅ Return `k = 5`  
  🔀 Order can vary: `[4,1,0,3,0,...]` is also correct

#### ⚙️ **What does "in-place" mean?**

"In-place" means:

- 🚫 Do **not** use another array (no extra space!)
- 🔄 Make all changes **inside the given `nums` array**
- 🔁 You're allowed to **swap, overwrite, or replace elements** as needed

#### ✅ **What does the system (judge) check?**

After your function runs, the judge does this:

```java
int k = removeElement(nums, val);  // 🔧 Your function is called

assert k == expectedNums.length;   // ✅ Check 1: Correct count of elements

sort(nums, 0, k);                  // 🔄 Sort the first k elements

for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];  // ✅ Check 2: Elements match
}
```

#### 📝 Notes:
- ✅ Only the first k elements matter
- 🔢 Their values must match the expected result (after sorting)
- 🚫 The rest of the array (after k) is ignored


#### 🔒 Constraints:
- `0 ≤ nums.length ≤ 100`
- `0 ≤ nums[i] ≤ 50`
- `0 ≤ val ≤ 100`

**🔑 In One Line:** 
- 🧼 Remove all `val` values from `nums` in-place, return how many values are left (`k`), and make sure the first `k` elements of `nums` are the ones that are not equal to `val`.<br> 🎲 The order doesn't matter, and the rest of the array can be ignored.