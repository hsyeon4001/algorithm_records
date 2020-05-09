// 10172번
console.log(`|\\_/|
|q p|   /}
( 0 )"""\\
|"^"\`    |
||_/=\\\\__|
`)

//10869번
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');
console.log(input.reduce((prev, curr) => Number(prev) + Number(curr)))
console.log(input.reduce((prev, curr) => Number(prev) - Number(curr)))
console.log(input.reduce((prev, curr) => Number(prev) * Number(curr)))
console.log(input.reduce((prev, curr) => Math.floor(Number(prev) / Number(curr))))
console.log(input.reduce((prev, curr) => Number(prev) % Number(curr)))

//10430번
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

for (i = 0; i < input.length; i++){
    input[i] = Number(input[i]);
}
console.log( ( input[0] + input[1] ) % input[2] );
console.log( ((input[0] % input[2]) + (input[1] % input[2])) % input[2] );
console.log( (input[0] * input[1]) % input[2] );
console.log( ((input[0] % input[2]) * (input[1] % input[2])) % input[2] );

// 2588번 
// 1) 배열 index 활용 (M 7076KB, T 108ms, C 361B)
const fs = require('fs');
const arr = fs.readFileSync('/dev/stdin').toString().split('\n');
const b_arr = arr[1].split("");
for (i = 0; i < b_arr.length; i++){
    arr[i] = Number(arr[i]);
    b_arr[i] = Number(b_arr[i]);
}
arr.pop();
console.log(arr[0] * b_arr[2]);
console.log(arr[0] * b_arr[1]);
console.log(arr[0] * b_arr[0]);
console.log(arr[0] * arr[1]);

// 2) 배열 값 사칙연산 (M 7080KB, T 104ms, C 306B)
const fs = require('fs');
const a = fs.readFileSync('/dev/stdin').toString().split('\n');

for (i = 0; i < a.length; i++){
    a[i] = Number(a[i])
}
console.log(a[0] * ( a[1] % 10 ));
console.log(a[0] * ( parseInt( a[1] / 10 ) % 10 ));
console.log(a[0] * parseInt( a[1] / 100 ));
console.log(a[0] * a[1]);
