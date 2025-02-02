class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j < len(nums2) - 1:
                        large = -1
                        for jj in range ((j+1),len(nums2)):
                            if nums2[j] < nums2[jj]:
                                large = nums2[jj]
                                ans.append(large)
                                break
                            elif jj == len(nums2) - 1:
                                ans.append(large)
                                break
                    else:
                        ans.append(-1)
        return ans
