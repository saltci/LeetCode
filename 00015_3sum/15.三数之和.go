/*
 * @lc app=leetcode.cn id=15 lang=golang
 *
 * [15] 三数之和
 */

// @lc code=start
// 先对数组进行排序，然后对数组进行遍历
// 1. 如果num[i],也就是如果一开始第一个数大于0,则退出循环
// 2. 如果num[i]和num[i-1]相等，则跳过
// 3. 生成两个指针, left和right
func threeSum(nums []int) [][]int {
	target := [][]int{}
	sort.Ints(nums)

	if nums == nil || len(nums) < 3 {
		return target
	}

	for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			break
		}

		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		left := i + 1
		right := len(nums) - 1

		for left < right {
			sum := nums[i] + nums[left] + nums[right]
			if sum == 0 {
				res := []int{nums[i], nums[left], nums[right]}
				target = append(target, res)
				
				// 因为存在重复元素，使用两个for循环来判断去重，最后将结果边界缩减
				for left < right && nums[left] == nums[left + 1] {
					left++
				}
				for left < right && nums[right] == nums[right-1] {
					right--
				}
				left++
				right--
			} else if sum > 0 {
				right--
			} else if sum < 0 {
				left++
			}
		}
	}

	return target
}
// @lc code=end

