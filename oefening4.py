


target = int(input("input target"))
nums = list(map(int, input("lijst").split(",")))
def countTargetPairs(nums, target):
    
    TrPairs = 0
    for i in range(len(nums)):
        for j in range( i +1, len(nums)):
            if i != j:
                if nums[i] + nums[j] < target:
                    TrPairs += 1
    return TrPairs


print(countTargetPairs(nums, target))













    
