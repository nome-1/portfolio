
let bob="1234";
let rm=bob.split("");
rm.reverse();
let zz=rm.join("")
console.log(zz);
const items = [1, 2, 3];
console.log(items); // [1, 2, 3]

items.reverse();
console.log(items); // [3, 2, 1]

const fruits = ["Banana", "Orange", "Apple", "Mango"];
console.log(fruits)
let text = fruits.join();
console.log(text)


function reverseString(s) {
    try{
        let rm=s.split("");
        rm.reverse();
        let zz=rm.join("");
        console.log(zz);
    }
    catch (e) {
    console.log(e.message);
    console.log(s);
}
}


function main() {
    const s = eval(readLine());
    
    reverseString(s);
}