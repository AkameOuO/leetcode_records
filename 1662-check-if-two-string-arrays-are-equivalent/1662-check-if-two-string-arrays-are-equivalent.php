class Solution {

    /**
     * @param String[] $word1
     * @param String[] $word2
     * @return Boolean
     */
    function arrayStringsAreEqual($word1, $word2) {
        $s1 = "";
        $s2 = "";
        foreach($word1 as $w1) {
            $s1 .= $w1;
        }
        
        foreach($word2 as $w2) {
            $s2 .= $w2;
        }
        
        return $s1 == $s2;
    }
}