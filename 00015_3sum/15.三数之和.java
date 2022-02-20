/*
 * @lc app=leetcode.cn id=15 lang=java
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i=0; i<nums.length;i++) {
            if (nums[i] > 0) {
                break;
            }

            if (i>0 && nums[i] == nums[i-1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int sumRes = nums[i] + nums[left] + nums[right];
                if (sumRes == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left+1]) left++;
                    while (left < right && nums[right] == nums[right-1]) right--;

                    right--;
                    left++;
                } else if (sumRes > 0) {
                    right--;
                } else if (sumRes < 0) {
                    left++;
                }
            }
        }

        return result;
    }
}
// @lc code=end

