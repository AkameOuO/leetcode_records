long long minEnd(int n, int x) {
    n--;
    int i = 0;
    long long res = 0;
    while(n||x) {
        if (x & 1) {
            res |= (long long)1 << i;
        } else {
            res |= (long long)(n&1) << i;
            n >>= 1;
        }
        i++;
        x >>= 1;
    }
    return res;
}