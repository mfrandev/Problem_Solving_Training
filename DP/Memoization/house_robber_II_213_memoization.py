class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def steal_max(i, houses, memo):
            if i >= len(houses):
                return 0
            if i == len(houses) - 1:
                return houses[i]
            if i in memo:
                return memo[i]
            hit_this_house = houses[i] + steal_max(i + 2, houses, memo)
            skip_this_house = steal_max(i + 1, houses, memo)
            memo[i] = max(hit_this_house, skip_this_house)
            return memo[i]

        # norm = nums[:-1]
        # adv = nums[1:]
        # print(norm)
        # print(adv)
        start_normal = steal_max(0, nums[:-1], {})
        start_adv = steal_max(1, nums, {})

        # print(f'pos 0: {start_normal}, pos 1: {start_adv}')
        return max(start_normal, start_adv)
