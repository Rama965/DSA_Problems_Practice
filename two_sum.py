#Two Sum Problem
#Find two indices whose values add up to target.
#Input: arr = [2,7,11,15], target = 9
#Output: [0,1]
#2 + 7 = 9
def two_sum(arr,target):
    hashmap = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        
        if complement in hashmap:
            return [hashmap[complement],i]
        hashmap[arr[i]] = i
        
print(two_sum([2,7,11,15],9))