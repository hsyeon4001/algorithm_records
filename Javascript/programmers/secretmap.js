function solution(n, arr1, arr2) {
	var answer = [];

	for (var i = 0; i < n; i++) {
		var num1 = arr1[i].toString(2);
		var num2 = arr2[i].toString(2);
		var num3 = "";

		num1 = Array(n - num1.length + 1).join("0") + String(num1);
		num2 = Array(n - num2.length + 1).join("0") + String(num2);

		for (var j = 0; j < n; j++) {
			if (num1[j] === "0" && num2[j] === "0") {
				num3 += " ";
			} else {
				num3 += "#";
			}
		}
		answer.push(num3);
	}

	return answer;
}
