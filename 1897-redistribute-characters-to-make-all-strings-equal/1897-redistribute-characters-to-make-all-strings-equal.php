class Solution {

    /**
     * @param String[] $words
     * @return Boolean
     */
    function makeEqual($words) {
        $l = count($words);
        $counter = array();
        foreach($words as $w) {
            for($i = 0;$i < strlen($w);$i++) {
                $c = $w[$i];
                $counter[$c] += 1;
            }
        }
        print_r($counter);
        foreach($counter as $v) {
            if($v % $l !== 0) {
                return false;
            }
        }
        return true;
    }
}