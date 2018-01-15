//We should know about each sharpie:
//  color (which should be a string)
//  width (which will be a number)
//  inkAmount (another number)
//When instantiating a Sharpie, we need to specify the color and the width
//Every sharpie is created with a default 100 as inkAmount
//We can use() the sharpie objects
//  which decreases inkAmount by the width
//Write a loop that consumes all the sharpie's ink.
//  Make sure your loop works with any inkAmount, so your code figures out when it's out of ink.

class Sharpie{
    constructor(color, width) {
        this.color = color;
        this.width = width;
        this.inkAmount = 100;
    }
    use () {
        this.inkAmount -= this.width;
        console.log(this.inkAmount);
    }
}

let sharpie = new Sharpie('blue', 10);

while (sharpie.inkAmount != 0) {
    sharpie.use();
};