// 1330번
const fs = require('fs');
const a = fs.readFileSync('/dev/stdin').toString().split(' ');
for (i = 0; i < a.length; i++) {
    a[i] = Number(a[i]);
}
if ( a[0] < a[1] ) {
    console.log('<');
} else if ( a[0] > a[1] ) {
    console.log('>');
} else {
    console.log('==');
}

//9498번
const fs = require('fs');
const a = Number(fs.readFileSync('/dev/stdin'));
if ( 90 <= a && a <= 100 ) {
    console.log('A');
} else if ( 80 <= a && a <= 89 ) {
    console.log('B');
} else if ( 70 <= a && a <= 79 ) {
    console.log('C');
} else if ( 60 <= a && a <= 69 ) {
    console.log('D');
} else {
    console.log('F');
}

// 2753번
const fs = require('fs');
const a = Number(fs.readFileSync('/dev/stdin'));
if ( a % 4 === 0 ) {
    if ( a % 100 !== 0 || a % 400 === 0) {
        console.log(1);
    } else {
        console.log(0);
    }
} else {
    console.log(0);
}

14681번
var fs = require('fs');
var line = require("fs").readFileSync("./j1/j1/j1.15.in", "utf8");
var input = line.trim().split("\r\n");
var x = input[0];
var y = input[1];

if ( x > 0 && y > 0 ) {
    console.log(1);
} else if ( x < 0 && y > 0 ) {
    console.log(2);
} else if ( x < 0 && y < 0 ) {
    console.log(3);
} else {
    console.log(4);
}

//2884번
const fs = require('fs');
const h = Number(fs.readFileSync('/dev/stdin').toString().split(" ")[0]);
const m = Number(fs.readFileSync('/dev/stdin').toString().split(" ")[1]);

if ( m >= 45 ) {
    console.log(h, m-45);
} else if ( m >= 0 && m < 45 ) {
    if ( h !== 0 ) {
        console.log(h-1, m+15);
    } else {
        console.log(23, m+15);
    }
}

