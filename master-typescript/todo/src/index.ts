console.log("HELLO, WORLD!");
console.log("ADD ONE MORE THING");
document
const h = "hello".replaceAll("l", "i");
console.log(h);

const btn = document.getElementById("btn");
const input = document.getElementById("todoinput")! as HTMLInputElement;

btn?.addEventListener("click", function () {
    alert(input.value);
    input.value = "";
});
