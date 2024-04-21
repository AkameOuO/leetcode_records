int scoreOfString(char* s) {
    int r = 0;
    int last = s[0];
    int l = strlen(s);
    for(int i = 1;i < l;i++){
        r += s[i] > last ? s[i] - last : last - s[i];
        last = s[i];
    }
    return r;
    
}