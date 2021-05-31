/*
 * @lc app=leetcode.cn id=704 lang=golang
 *
 * [704] 二分查找
 */

// @lc code=start
func search(nums []int, target int) int {
	left := 0
	length := len(nums)
	right := length - 1

	for (left <= right) {
		middle := left + ((right - left) / 2)

		if nums[middle] > target {
			right = middle - 1
		} else if nums[middle] < target {
			left = middle + 1
		} else {
			return middle
		}
	}

	return -1
		
}
// @lc code=end

