const encourageStudent = (name: string) => {
    return `Hey, ${name}, you're doing GREAT!`;
}
console.log(encourageStudent("Augustine"));

function square(num: number) {
    return num * num;
}
console.log(square(3));

function greet(person: string = "Augustine") {
    return `Hi there, ${person}!`;
}
console.log(greet());

const addNums = (x: number, y: number): number => {
    return x + y;
}
console.log(addNums(3, 5));

const colors = ["red", "green", "yellow"];
colors.forEach((color, index) => {
    colors[index] = color.toUpperCase();
})
console.log(colors);

const twoFer = (name: string = "Augustine"): string => {
    return `one for ${name}, one for me`;
}

const isLeapYear = (year: number): boolean => {
    return (year % 100 !== 0 && year % 4 === 0) || year % 400 === 0;
}
console.log(isLeapYear(2012));
console.log(isLeapYear(2013));