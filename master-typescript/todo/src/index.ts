const h = "hello".replaceAll("l", "i");
console.log(h);

const btn = document.getElementById("btn");
const input = document.getElementById("todoinput")! as HTMLInputElement;
const form = document.querySelector("form")!;

function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    console.log("SUBMITTED");
}
form.addEventListener("submit", handleSubmit);
// btn?.addEventListener("click", function () {
    // alert(input.value);
    // input.value = "";
// });
