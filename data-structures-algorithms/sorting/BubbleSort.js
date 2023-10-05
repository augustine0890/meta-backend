function less(a, b) {
    return a < b;
}
function more(a, b) {
    return a > b;
}
function BubbleSort(arr) {
    var size = arr.length;
    var i;
    var j;
    var temp;
    for (i = 0; i < size - 1; i++) {
        for (j = 0; j < size - i - 1; j++) {
            if (more(arr[j], arr[j + 1])) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
// Testing code.
var array = [9, 1, 8, 2, 7, 3, 6, 4, 5];
BubbleSort(array);
console.log(array);
