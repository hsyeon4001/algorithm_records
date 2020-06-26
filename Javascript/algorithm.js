// function quick (arr) {
//     if (arr.length < 2) {
//         return arr;
//     }

//     const pivot = [arr[0]];
//     const less = [];
//     const greater = [];

//     for (let i = 1; i < arr.length; i++) {
//         if (arr[i] < pivot) {
//             less.push(arr[i]);
//         } else if (arr[i] > pivot) {
//             greater.push(arr[i]);
//         } else {
//             pivot.push(arr[i]);
//         }
//     }
//     return quick(less).concat(pivot, quick(greater));
//     }

//     const arr = [5, 3, 7, 1, 9];
//     console.log(quick(arr));

const tests = new Map();
tests.set(() => 2+2, 4)
tests.set(() => 2*2, 4)
tests.set(() => 2/2, 1)
console.log(tests);

for ( const entry of tests ) {
    console.log(entry[0](), entry[1]);
    
    console.log((entry[0]() === entry[1]) ? 'pass' : 'fail');
    
}
