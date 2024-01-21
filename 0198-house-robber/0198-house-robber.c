

int rob(int* nums, int numsSize){
    int* ans = calloc(numsSize + 4,sizeof(int));
    for(int i = 3;i < numsSize+3;i++)
        ans[i] = nums[i-3] + (ans[i-2]>ans[i-3]?ans[i-2]:ans[i-3]);
    ans[numsSize+3] = (ans[numsSize+1]>ans[numsSize+2]?ans[numsSize+1]:ans[numsSize+2]);
    return ans[numsSize+3];
}