def arrayChk(nums):
    print(nums)
    for x in range(len(nums)-2):
        if nums[x]==1 and nums[x+1]==2 and nums[x+2]==3:
            return True
    return False

print(arrayChk([1,1,2,3,1]))

print(arrayChk([1,1,2,4,1]))
