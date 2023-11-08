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

type StringOrNum = string | number;
let userID: StringOrNum = "abc";
userID = 123;
console.log(userID);

// let user Object;
type User = {
    name: string;
    age: number;
    isAdmin: boolean;
    id: string | number;
};
let user: User;
user = {
    name: "Augustine",
    age: 34,
    isAdmin: true,
    id: 123,
};
console.log(user);

interface Credentials {
    password: string;
    email: string;
}
let creds: Credentials;
creds = {
    password: "abc123",
    email: "abc123@example.com"
}
// class Authentication implements Credentials {
// email: string;
// password: string;
// userName: string;
// }

type Role = 'admin' | 'user' | 'editor';
let role: Role;
role = 'admin';
role = 'user';
role = 'editor';
// role = 'guest';

let roles: Array<Role>;
roles = ['admin', 'editor'];
type DataStorage<T> = {
    storage: T[];
    add: (data: T) => void;
};
const textStorage: DataStorage<string> = {
    storage: [],
    add(data) {
        this.storage.push(data);
    }
};
const userStorage: DataStorage<User> = {
    storage: [],
    add(user) {
        this.storage.push(user);
    }
}

function merge<T, U>(a: T, b: U) {
    return {
        ...a,
        ...b,
    };
}
const newUser = merge(
    { name: "Augustine" }, { age: 34 }
);
console.log(newUser);