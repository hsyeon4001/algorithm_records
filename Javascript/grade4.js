// 10952번
const fs = require('fs');
const arr = fs.readFileSync('/dev/stdin').toString().split('\n');

let i = 0;
while ( i < arr.length ) {
    const sum = Number(arr[i].split(" ")[0]) + Number(arr[i].split(" ")[1])
    if ( sum === 0 ) {
        break;
    } else {
        console.log(sum);
    }
    i++;
    }

//10951번
const fs = require('fs');
const arr = fs.readFileSync('/dev/stdin').toString().split('\n');
let i = 0;
while ( i < arr.length-1 ) {
    const sum = Number(arr[i].split(" ")[0]) + Number(arr[i].split(" ")[1])
    console.log(sum);
    i++;
    }

// 1110번
const fs = require('fs');
const num = Number(fs.readFileSync('/dev/stdin'));
let n = num;
let answer;
let i = 0;

while ( Number(answer) !== num ) {
    let a = String(n)[0];
    let b = String(n)[1];
    
    let sum = Number(a) + Number(b);
    
    if ( n < 10 ) {
        n = Number(n);
        answer = String(n) + String(n);
    } else {
        if ( sum >= 10 ) {            
            answer = b + String(sum)[1];
        } else {
            answer = b + String(sum);
        }
    }
    n = answer;
    i++;
}
console.log(i);