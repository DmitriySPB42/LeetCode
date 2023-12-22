def sequence_counter(nums):
    count = 0
    counts = []
    for i in range(len(nums)):
        if int(nums[i])==1: count+=1; counts.append(count)
        elif int(nums[i])==0: count = 0
    return max(counts)

nums = input()[1:-1].split(",")
print(sequence_counter(nums))