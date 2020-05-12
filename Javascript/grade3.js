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
