let s ="affrdsa"
function getLetter(s) {
    let letter;
    let bob=s.match(/(^[a,e,i,o,u])/);
    console.log(bob)
    console.log(bob.constructor)
    // Write your code here
    switch(true){
        case 'aeiou'.includes(s[0]):
            letter = 'A';
            break;
        case 'bcdfg'.includes(s[0]):
            letter = 'B';
            break;
        case 'hjkml'.includes(s[0]):
            letter = 'C';
            break;
        default:
            letter = 'D';
            break;
    }
return letter;

    
}

console.log(getLetter(s))
