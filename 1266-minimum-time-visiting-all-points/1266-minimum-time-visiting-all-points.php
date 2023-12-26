class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minTimeToVisitAllPoints($points) {
        $last = $points[0];
        $res = 0;
        for($i = 1;$i < count($points);$i++) {
            $res += max(abs($points[$i][0] - $last[0]),abs($points[$i][1] - $last[1]));
            $last = $points[$i];
        }
        return $res;
    }
}