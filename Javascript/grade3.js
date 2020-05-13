// 2739번
const fs = require('fs');
const a = Number(fs.readFileSync('/dev/stdin'));

for ( i = 1; i <= 9; i++ ) {
    console.log(`${a} * ${i} = ${a * i}`);
}

//10950번
const fs = require('fs');
const a = fs.readFileSync('/dev/stdin').toString().split('\n');

const len = Number(a.shift());
for ( i = 0; i < len; i++) {
    const arr = a[i].split(' ');
    console.log((Number(arr[0]) + Number(arr[1])));
};

//8393번
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin'));
const arr = [];
const reducer = (a, b) => a+b;

for ( i = 1; i <= n; i++ ) {
    arr.push(i);
}
console.log(arr.reduce(reducer));

// 2741번
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin'));
for (i = 1; i <= n; i++) {
    console.log(i);
}

// 2742번
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin'));
for (i = n; i >= 1; i--) {
    console.log(i);
}

// 11021번
const fs = require('fs');
const a = fs.readFileSync('/dev/stdin').toString().split('\n');
const len = a.shift();
for ( i = 0; i < len; i++) {
    const n = a[i].split(' ');
    console.log(`Case #${i+1}: ${Number(n[0])+Number(n[1])}`);
}

//11022번
const fs = require('fs');
const a = fs.readFileSync('/dev/stdin').toString().split('\n');
const len = a.shift();
for ( i = 0; i < len; i++) {
    const n = a[i].split(' ');
    console.log(`Case #${i+1}: ${n[0]} + ${n[1]} = ${Number(n[0])+Number(n[1])}`);
}

// 2438번
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin'));
const arr = [];
for (i = 1; i <= n; i++) {
    arr.push("*");
    console.log(arr.join(""));
}

// 2439번
const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin'));
let star = "";
let space = "";
let space_arr = [];
for ( i = 0; i <= n-1; i++) {
    space_arr.push(space)
    space += " "
}
for ( i = n-1; i >= 0; i--) {
    star += "*";
    console.log(space_arr[i] + star);
}

// 10871번
const fs = require('fs');
const a = fs.readFileSync('/dev/stdin').toString().split('\n');
const len = Number(a[0].toString().split(' ')[0]);
const n = Number(a[0].toString().split(' ')[1]);
const arr = a[1].split(' ');
const answer = [];
for ( i = 0; i < arr.length; i++ ) {
    arr[i] = Number(arr[i]);
}
for ( i = 0; i < len; i++ ) {
    if ( arr[i] < n ) {
        answer.push(arr[i]);
    }
}
console.log(answer.join(" "));

