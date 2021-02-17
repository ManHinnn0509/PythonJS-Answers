function log(s) {
    console.log(s);
}

// O(n^2) but whatever
function bbs(a) {
    const len = a.length;

    for (y = 0; y < len - 1; y++) {
        for (x = 0; x < len - y - 1; x++) {
            if (a[x] > a[x + 1]) {
                temp = a[x];
                a[x] = a[x + 1];
                a[x + 1] = temp;
            }
        }
    }
    return a;
}

let numbers = [5, 3, 11, 2, 6, 27, 13];
log("Before sorting: " + numbers);
log("After sorting: " + bbs(numbers));
