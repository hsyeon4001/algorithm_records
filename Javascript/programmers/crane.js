function solution(board, moves) {
	var answer = 0;
	var basket = [];
	var grabbed_toys = [];

	for (var i = 0; i < board.length; i++) {
		var toys = [];
		for (var j = 0; j < board.length; j++) {
			var toy = board[j].shift();
			if (toy !== 0) {
				toys.push(toy);
			}
		}
		basket.push(toys);
	}

	for (var i = 0; i < moves.length; i++) {
		if (basket[moves[i] - 1].length) {
			var grabbed_toy = basket[moves[i] - 1].shift();
			if (grabbed_toy === grabbed_toys[grabbed_toys.length - 1]) {
				grabbed_toys.pop();
				answer += 2;
			} else {
				grabbed_toys.push(grabbed_toy);
			}
		}
	}

	return answer;
}
