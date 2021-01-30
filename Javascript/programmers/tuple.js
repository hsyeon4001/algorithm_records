function solution(s) {
	var answer = [];
	var table = {};
	s = s.slice(2, -2).split("},{");

	for (var nums of s) {
		nums = nums.split(",");
		for (var num of nums) {
			if (num in table) {
				table[num] += 1;
			} else {
				table[num] = 1;
			}
		}
	}
	answer = Object.entries(table).sort((a, b) => {
		return b[1] - a[1];
	});
	answer = answer.map((x) => Number(x[0]));

	return answer;
}
