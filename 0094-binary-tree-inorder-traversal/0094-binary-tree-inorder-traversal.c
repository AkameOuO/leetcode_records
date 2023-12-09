/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void append(int *ans,int val)
{
    ans[ans[0]+1] = val;
    ans[0]++;
}

void travel(struct TreeNode* root,int *ans)
{
    if(root->left) travel(root->left,ans);
    append(ans,root->val);
    if(root->right) travel(root->right,ans);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize){
    if(!root)
    {
        *returnSize = 0;
        return NULL;
    }
    int *ans = calloc(101,sizeof(int));
    travel(root,ans);
    *returnSize = ans[0];
    return ans+1;
}