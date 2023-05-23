function getCount(objects) {
    let bob=objects.length;
    let x=0
    let value=0
    for(x in objects){
      let b=objects[x];
      if(b.x==b.y){
          value+=1  
      }
        
    }
    return value
    
}
