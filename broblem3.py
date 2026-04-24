class solution:
    def movezeros(self,nums):
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index],nums[i] = nums[i],nums[index]
                index+=1

nums = [6,8,0,9,7,0,0,8,7,13,88,0,99,0,7,0,54,7]
sol = solution() 
sol.movezeros(nums)
print(nums)


        
        