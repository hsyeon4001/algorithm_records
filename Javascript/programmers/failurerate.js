function solution(N, stages) {
	var answer = [];
	var deno = 0;
	var nume = 0;

	for (var i = 1; i <= N; i++) {
		deno = stages.filter((stage) => stage >= i).length;
		nume = stages.filter((stage) => stage === i).length;

		answer.push(nume / deno);
	}

	answer = Object.entries(answer);
	answer.sort((a, b) => {
		return b[1] - a[1];
	});
	answer = answer.map((x) => parseInt(x[0]) + 1);

	return answer;
}
