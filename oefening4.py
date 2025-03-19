import random

def randnumgen():
    startinput = int(input("start " ))
    endinput = int(input("end " ))
    leninput = int(input("length " ))
    num_list = []

    while len(num_list) < leninput:
        num_list.append(random.randint(startinput, endinput))
    return num_list


nums =  randnumgen()


def countTargetPairs(nums):
    target = int(input("input target "))
    TrPairs = 0
    for i in range(len(nums)):
        for j in range( i + 1, len(nums)):
            if i != j:
                if nums[i] + nums[j] < target:
                    TrPairs += 1
    return TrPairs


print(countTargetPairs(nums))
       













    
