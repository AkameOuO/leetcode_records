/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    const fns = functions.reverse()
    
    return function(x) {
        for (const fn of fns) {
            x = fn(x)
        }
        return x
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */