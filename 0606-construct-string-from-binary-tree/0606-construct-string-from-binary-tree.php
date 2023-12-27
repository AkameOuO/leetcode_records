/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return String
     */
    function tree2str($root) {
        if($root === null) {
            return "";
        }
        $res = strval($root->val);
        if($root->right !== null) {
            $res .= "(".$this->tree2str($root->left).")";
            $res .= "(".$this->tree2str($root->right).")";
        }
        else if($root->left !== null) {
            $res .= "(".$this->tree2str($root->left).")";
        }
        return $res;
    }
}