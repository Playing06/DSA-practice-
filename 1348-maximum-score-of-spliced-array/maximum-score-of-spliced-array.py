class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        sum1=sum(nums1)
        sum2=sum(nums2)

        curr1=0
        max_curr1=0

        curr2=0
        max_curr2=0
        for i in range(len(nums1)):
            curr1+=nums2[i]-nums1[i]
            if curr1<0:
                curr1=0
            max_curr1=max(max_curr1,curr1)

            curr2+=nums1[i]-nums2[i]
            if curr2<0:
                curr2=0
            max_curr2=max(max_curr2,curr2)
        return max(sum1+max_curr1,sum2+max_curr2)



        