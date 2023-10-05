/**
 * Write a program that prints the integers from 1 to 100
 * But
 * - for multiples of three, print Fizz
 * - for multiples of five, print Buzz
 * - for multiples of both three and five, print FizzBuzz
 */

function fizzBuzz() {
    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 === 0) {
            console.log("FizzBuzz");
        } else if (i % 5 === 0) {
            console.log("Buzz");
        } else if (i % 3 === 0) {
            console.log("Fizz");
        } else {
            console.log(i);
        }
    }
}

fizzBuzz();