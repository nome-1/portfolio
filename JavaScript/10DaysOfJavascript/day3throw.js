function isPositive(a) {
    let bob="YES";
    try{
        if(a>0){
        return bob
    }
    else if(a==0){
        throw "Zero Error";
    }
    else{
        throw "Negative Error";
    }
    }catch(e) {
        return e

  }
    
    
}
