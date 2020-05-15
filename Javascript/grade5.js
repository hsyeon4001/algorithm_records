// 10039번
const fs = require('fs');
const arr = fs.readFileSync('/dev/stdin').toString().split('\n');
for ( i = 0; i < 5; i++ ) {
    arr[i] = Number(arr[i])

    if ( arr[i] < 40 ) {        
        arr[i] = 40;
    }
}
const sum = arr.reduce((a, b) => a + b);
console.log(sum / 5);

//5543번
const fs = require('fs');
const price = fs.readFileSync('/dev/stdin').toString().split('\n');
for ( i = 0; i < price.length; i++ ) {
    price[i] = Number(price[i]);
}
const burger = price.slice(0, 3);
const drink = price.slice(3, 5);
const min = arr => arr.reduce( (prev, curr) => {
    return prev > curr ? curr : prev;
})
console.log( min(burger) + min(drink) - 50 );

// 10817번-1
const fs = require('fs');
const n = fs.readFileSync('/dev/stdin').toString().split(' ');
for ( i = 0; i < n.length; i++ ) {
    n[i] = Number(n[i]);
}
const min = arr => arr.reduce( (prev, curr) => {
    return prev > curr ? curr : prev;
})
const answer = [];
while (n.length !== 0) {
    answer.push(min(n));
    const min_idx = n.indexOf(min(n));
    n.splice(min_idx, 1);
}
console.log(answer[1]);

// 10817번-2
const fs = require('fs');
const n = fs.readFileSync('/dev/stdin').toString().split(' ');
for ( i = 0; i < n.length; i++ ) {
    n[i] = Number(n[i]);
}
n.sort((a, b) => {
    return a - b;
});
console.log(n[1]);

