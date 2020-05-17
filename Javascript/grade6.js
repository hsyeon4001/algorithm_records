// 10818번
const fs = require('fs');
const len = Number(fs.readFileSync('/dev/stdin').toString().split('\n')[0]);
const arr = fs.readFileSync('/dev/stdin').toString().split('\n')[1];
const nums = arr.split(" ");
for ( i = 0; i < len; i++ ) {
    nums[i] = Number(nums[i]);
}
nums.sort((a, b) => a - b);
console.log(nums[0], nums[nums.length-1]);

// 2562번
const arr_origin = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const arr = input.toString().split('\n');
arr.sort((a, b) => b-a);
const index = Number(arr_origin.indexOf(arr[0]))+1
console.log(Number(arr[0]) + '\n' + index);

// 2577번
const nums = require(fs).readFileSync('/dev/stdin').toString().split('\n');
for ( i = 0; i < nums.length; i++ ) {
    nums[i] = Number(nums[i]);
}
let result = nums[0]
for ( i = 1; i < nums.length; i++ ) {
    result *= nums[i]
}
for ( i = 0; i <= 9; i++ ) {
    const a = new RegExp(i, 'g');
    if (result.toString().match(a) !== null) {
        console.log(result.toString().match(a).length);
    } else {
        console.log('0');
    }
}
