class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $target
     * @return Integer
     */
    private $dp = [];
    function numRollsToTarget($n, $k, $target) {
        if($target > $n * $k || $target < $n) {
            return 0;
        }
        if($n == 1 && $target <= $k){
            return 1;
        }
        $s = $this->toStr($n,$target);
        if(is_array($this->$dp) && array_key_exists($s,$this->$dp)) {
            return $this->$dp[$s];
        }
        $res = 0;
        for($i = 1;$i <= $k;$i++) {
            $res = ($res + $this->numRollsToTarget($n-1,$k,$target-$i)) % (1000000007);
        }
        $this->$dp[$s] = $res;
        return $this->$dp[$s];
    }
    
    function toStr($a,$b) {
        return strval($a).",".strval($b);
    }
}