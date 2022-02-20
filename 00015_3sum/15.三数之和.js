/*
 * @lc app=leetcode.cn id=15 lang=javascript
 *
 * [15] 三数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    result = [];

    if (nums.length < 3) {
        return result;
    }
    
    // 升序排序
    nums.sort((a,b)=>a-b);
    for (i = 0; i < nums.length; i++) {
        if (nums[i] > 0) {
            break;
        }

        if (i > 0 && nums[i] == nums[i-1] ) {
            continue;
        }
        
        left = i + 1;
        right = nums.length - 1;

        while (left < right) {
            sumResult = nums[i] + nums[left] + nums[right];
            if (sumResult == 0) {
                result.push([nums[i] , nums[left] , nums[right]]);
                while (left < right && nums[left] == nums[left+1]) {
                    left++;
                }
                while (left < right && nums[right] == nums[right-1]) {
                    right--;
                }
                left++;
                right--;
            } else if (sumResult > 0) {
                right--;
            } else if (sumResult < 0) {
                left++;
            }
        }
    }

    return result;
};
// @lc code=end

