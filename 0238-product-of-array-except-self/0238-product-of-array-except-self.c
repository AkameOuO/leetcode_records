

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize){
    (*returnSize) = numsSize;
    int zeroCount = 0,zeroIndex = 0,product = 1;
    int* ans = calloc(numsSize,sizeof(int));
    for(int i = 0;i < numsSize;i++)
    {
        if(nums[i])
            product *= nums[i];
        else if(zeroCount)
        {
            zeroCount++;
            break;
        }
        else
        {
            zeroCount++;
            zeroIndex = i;
        }
    }
    if(zeroCount >= 2)
    {
        return ans;
    }
    else if(zeroCount == 1)
    {
        ans[zeroIndex] = product;
        return ans;
    }
    else
    {
        for(int i = 0;i < numsSize;i++)
        {
            ans[i] = product / nums[i];
        }
    }
    return ans;
}