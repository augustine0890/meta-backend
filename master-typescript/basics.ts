console.log("HELLO!");
console.log(Math.round(3.699999999));
console.log("GOODBYE");

const movies = [
    {
        name: "The Shawshank Redemption",
        year: 1994,
    },
    {
        name: "The Godfather",
        year: 1972,
    },
    {
        name: "The Godfather: Part II",
        year: 1974,
    },
    {
        name: "The Dark Knight",
        year: 2008,
    },
];

movies.sort((a, b) => a.year - b.year); // O(nlogn)
console.log(movies.map(movie => movie.name));