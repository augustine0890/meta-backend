function medianValue(a: number[]): number {
    a.sort()
    const mid = Math.floor(a.length / 2);
    if (mid % 2 === 0) {
        return (a[mid] + a[mid - 1]) / 2;
    } else {
        return a[mid];
    }
}

console.log(medianValue([2, 4, 7]));
console.log(medianValue([2, 4, 7, 6]));
console.log(medianValue([2, 4, 7, 6, 6]));
console.log(medianValue([2, 4, 7, 6, 6, 8]));