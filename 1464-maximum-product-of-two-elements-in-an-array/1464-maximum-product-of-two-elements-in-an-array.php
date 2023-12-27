class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProduct($nums) {
        $a = max($nums);
        unset($nums[array_search($a,$nums)]);
        $b = max($nums);
        return ($a-1) * ($b-1);
    }
}