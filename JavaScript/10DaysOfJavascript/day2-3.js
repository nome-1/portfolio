function vowelsAndConsonants(s) {
    let n ="";
    let t ="";
    let vowels=[]
    let consonat=[]
    for (let x in s) {
        n=s[x].search(/[^aeiou]/);
        if(n==-1){
            n=x;
            console.log(s[n])
        }
    }
        for (let x in s){
        t=s[x].search(/[aeiou]/);
        if(t==-1){
            t=x;
            console.log(s[t])
        }
      }
    
    }
let s="abbiffe"
vowelsAndConsonants(s)