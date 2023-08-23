class Cookies {
    constructor(color) {
        this.color = color;
    }
    getColor() {
        return this.color;
    }
    setColor(color) {
        this.color = color;
    }
}

let cookieOne = new Cookies("green");
console.log(cookieOne.getColor());
cookieOne.setColor("yellow");
console.log(cookieOne.getColor());
let cookieTwo = new Cookies("blue");

/**
 * The garbage collector (GC) serves as an automatic memory manager.
 * Automatic memory management can eliminate common problems such as forgetting to free an object and causing a memory leak
 * or attempting to access freed memory for an object that is already been freed.
 */