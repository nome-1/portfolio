class Polygon {
    constructor(array) {
      this.array =array;
    }
    perimeter(){
        return this.array.reduce(function(a,b){ return +a + +b; })
  
    }
  
  
  }
  
  const rectangle = new Polygon([10, 20, 10, 20]);
  const square = new Polygon([10, 10, 10, 10]);
  const pentagon = new Polygon([10, 20, 30, 40, 43]);
  
  console.log(rectangle.perimeter());
  console.log(square.perimeter());
  console.log(pentagon.perimeter());