function solution(new_id) {
	var answer = "";
	var lowerId = new_id.toLowerCase();
	var pattern = /([a-z0-9]|-|_|\.)/;

	for (var char of lowerId) {
		if (pattern.test(char)) {
			answer += char;
		}
	}

	while (true) {
		while (answer.includes("..")) {
			answer = answer.replace("..", ".");
		}

		if (answer[0] === ".") {
			answer = answer.substring(1);
		} else if (answer[answer.length - 1] === ".") {
			answer = answer.substring(0, answer.length - 1);
		} else {
			break;
		}
	}

	while (true) {
		if (answer.length === 0) {
			answer += "aaa";
			break;
		}

		if (answer.length < 3) {
			answer += answer[answer.length - 1].repeat(3 - answer.length);
			break;
		} else if (answer.length > 15) {
			answer = answer.substring(0, 15);
			if (answer[answer.length - 1] === ".") {
				answer = answer.substring(0, answer.length - 1);
			}
			break;
		} else {
			break;
		}
	}

	return answer;
}
