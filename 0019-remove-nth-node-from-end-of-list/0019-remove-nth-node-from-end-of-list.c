/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* cur = head;
    int count = 0;
    for(;cur;cur = cur->next)count++;
    if(count == n)
        return head->next;
    cur = head;
    for(int i = 1;i < count-n;i++)cur = cur->next;
    //if(cur->next == NULL)return NULL;
    cur->next = cur->next->next;
    return head;
}