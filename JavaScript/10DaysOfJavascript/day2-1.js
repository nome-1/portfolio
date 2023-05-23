let score=25;

function getGrade(score) {
    let grade;
    // Write your code here
    switch (true) {
    case 25<score&&score<=30:
        grade = "A";
        break;
    case 20<score&&score<=25:
        grade = "B";
        break;
    case 15<score&&score<=20:
        grade = "C";
        break;
    case 10<score&&score<=15:
        grade = "D";
        break;
    case 5<score&&score<=10:
        grade = "E";
        break;
    case 0<=score&&score<=5:
        grade = "F";
        break;
}
    
    return grade;
}
console.log(getGrade(score))