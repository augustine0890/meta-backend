function less(a: number, b: number): boolean {
    return a < b;
}

function more(a: number, b: number): boolean {
    return a > b;
}

/**
 * Time: O(n^2)
 * Space: O(1) - only one temp variable
 */
function BubbleSort(arr: Array<number>) {
    let size: number = arr.length;
    let i: number;
    let j: number;
    let temp: number;
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
let array: Array<number> = [9, 1, 8, 2, 7, 3, 6, 4, 5];
BubbleSort(array);
console.log(array);