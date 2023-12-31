class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxLengthBetweenEqualCharacters($s) {
        $l = strlen($s);
        $arr = array();
        $res = -1;
        for($i = 0;$i < $l;$i++) {
            if(isset($arr[$s[$i]])) {
                $res = max($res,$i-$arr[$s[$i]]-1);
            }
            else {
                $arr[$s[$i]] = $i;
            }
        }
        return $res;
    }
}