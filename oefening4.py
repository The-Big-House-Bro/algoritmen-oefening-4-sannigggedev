def countTargetPairs(nums):
    target = int(input("input target "))
    TrPairs = 0
    for i in range(len(nums)):
        for j in range( i + 1, len(nums)):
            if i != j:
                if nums[i] + nums[j] < target:
                    TrPairs += 1
    return TrPairs

nums = []
print(countTargetPairs(nums))
       













    
