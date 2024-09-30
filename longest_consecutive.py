# 128 Longest consecutive
def longestConsecutive(nums):
    if len(nums)==0:
        return 0
    my_hash={}
    for items in nums:
        if items in my_hash:
            continue

        # both left and right are consecutive
        if items-1 in my_hash and items+1 in my_hash:
            update_num=my_hash[items-1]+my_hash[items+1]+1
            my_hash[items-my_hash[items-1]]=update_num
            my_hash[items+my_hash[items+1]]=update_num
            my_hash[items]=update_num
        # only left
        elif items-1 in my_hash:
            update_num = my_hash[items - 1]+1
            my_hash[items]=update_num
            my_hash[items-my_hash[items-1]]=update_num
        # only right
        elif items+1 in my_hash:
            update_num = my_hash[items + 1]+1
            my_hash[items]=update_num
            my_hash[items+my_hash[items+1]]=update_num
        # no left no right
        else:
            my_hash[items]=1
    return max(my_hash.values())

if __name__ == '__main__':
    nums=[0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutive(nums))