let movieTitle: string = "Amadeus";
movieTitle = "Arrival";
console.log(movieTitle.toUpperCase());

let numCatLives: number = 9;
numCatLives++;
console.log(numCatLives);

let gameOver: boolean = false;
gameOver = true;
console.log(gameOver);

const movies = ["Arrival", "The Thing", "Aliens", "Amadeus"];
let foundMovie: any;
console.log(foundMovie);
for (let movie of movies) {
    if (movie == "Amadeus") {
        foundMovie = "Amadeus";
    }
}
console.log(foundMovie);


