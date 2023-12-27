class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function totalMoney($n) {
        // print_r( array_map(function($i){return intdiv($i,7)+$i%7+1;},range($n-1)));
        return array_sum(array_map(function($i){return intdiv($i,7)+$i%7+1;},range(0,$n-1)));
    }
}