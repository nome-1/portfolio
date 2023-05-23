function getSecondLargest(nums) {
    const tom= Math.max.apply(null,nums)
    let i=0;
    while (i < nums.length) {
        if(Math.max.apply(null,nums)==tom){
            let index = nums.indexOf(tom);
            nums.splice(index, 1);
            i++;
        }
        else{
            let mark=Math.max.apply(null, nums)
            return mark;
        }
    // Complete the function
}
}
let nums=[2, 3 ,6 ,6 ,5]
console.log(getSecondLargest(nums))