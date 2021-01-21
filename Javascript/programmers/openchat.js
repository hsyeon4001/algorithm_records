function solution(record) {
	var answer = [];
	var userTable = {};
	var data = "";

	for (var i in record) {
		data = record[i].split(" ");
		if (data[0] === "Leave") {
			continue;
		}
		userTable[data[1]] = data[2];
	}

	for (var i in record) {
		data = record[i].split(" ");

		if (data[0] === "Enter") {
			answer.push(`${userTable[data[1]]}님이 들어왔습니다.`);
		} else if (data[0] === "Leave") {
			answer.push(`${userTable[data[1]]}님이 나갔습니다.`);
		}
	}
	return answer;
}
