function solution(str1, str2) {
    var answer = 0;
    var pattern = /^[a-zA-Z]+$/;
    var arr1 = [];
    var arr2 = [];
    var union = [];
    var intersection = [];
    
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    
    for (var i = 0; i < str1.length-1; i++) {
        if (pattern.test(str1[i]) && pattern.test(str1[i+1])) {
            arr1.push(str1[i]+str1[i+1]);
        }
    }
    for (var i = 0; i < str2.length-1; i++) {
        if (pattern.test(str2[i]) && pattern.test(str2[i+1])) {
            arr2.push(str2[i]+str2[i+1]);
        }
    }

    for (var i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) >= 0) {
            intersection.push(arr1.splice(arr1.indexOf(arr2[i]), 1));
        }
        union.push(arr2[i]);
    }

    for (var i = 0; i < arr1.length; i++) {
        union.push(arr1[i]);
    }
    
    if( union.length === 0 ){
        answer = 65536;
    }else{
        answer = Math.floor((intersection.length / union.length) * 65536);
    } 
    
    return answer;
}