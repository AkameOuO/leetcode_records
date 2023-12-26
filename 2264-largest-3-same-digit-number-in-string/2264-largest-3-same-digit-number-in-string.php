class Solution {

    /**
     * @param String $num
     * @return String
     */
    function largestGoodInteger($num) {
        $l = strlen($num);
        $res = "";
        for($i = 0;$i < $l-2;$i++) {
            if($num[$i] == $num[$i+1] && $num[$i] == $num[$i+2]) {
                $tmp = substr($num,$i,3);
                if($tmp > $res) {
                    $res = $tmp;
                }
            }
        }
        return $res;
    }
}