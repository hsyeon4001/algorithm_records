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
