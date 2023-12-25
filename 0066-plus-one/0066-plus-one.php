class Solution {

    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function plusOne($digits) {
        for($i = count($digits) - 1; $i >= 0; $i--) {
            $digits[$i]++;
            if($digits[$i] < 10) {
                break;
            }
            $digits[$i] = 0;
        }
        if($digits[0] == 0) {
            array_push($digits, 0);
            $digits[0] = 1;
        }
        return $digits;
    }
}