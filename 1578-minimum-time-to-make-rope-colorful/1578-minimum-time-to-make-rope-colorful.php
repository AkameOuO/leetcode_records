class Solution {

    /**
     * @param String $colors
     * @param Integer[] $neededTime
     * @return Integer
     */
    function minCost($colors, $neededTime) {
        $l = strlen($colors);
        $lc = $colors[0];
        $lt = $neededTime[0];
        $res = 0;
        for($i = 1;$i < $l;$i++) {
            if($lc == $colors[$i]) {
                if($lt <= $neededTime[$i]) {
                    $res += $lt;
                }
                else {
                    $res += $neededTime[$i];
                    continue;
                }
            }
            $lc = $colors[$i];
            $lt = $neededTime[$i];
        }
        return $res;
    }
}