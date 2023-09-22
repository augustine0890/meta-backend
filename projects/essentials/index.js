import express from "express";
import data from "./data/mock.json" assert {type: "json"};

const app = express();

const PORT = 3000;

// Using the public folder at the root of the application
app.use(express.static("public"));

// Using the images folder at the route /images
app.use('/images', express.static("images"));

app.get('/', (req, res) => {
    res.json(data);
});

app.post('/create', (req, res) => {
    res.send("This is a POST request at /create")
});

app.put('/edit', (req, res) => {
    res.send("This is a PUT request at /edit")
});

app.delete('/delete', (req, res) => {
    res.send("This is a DELETE request at /delete")
})

app.listen(PORT, () => {
    console.log(`The server is running at ${PORT}`);
});