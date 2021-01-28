function solution(orders, course) {
	var answer = [];

	function combination(arr, selectNum) {
		var result = [];
		if (selectNum === 1) return arr.map((v) => [v]);
		arr.forEach((v, idx, arr) => {
			var fixed = v;
			var restArr = arr.slice(idx + 1);
			var combinationArr = combination(restArr, selectNum - 1);
			var combineFix = combinationArr.map((v) => [fixed, ...v].sort().join(""));

			result.push(...combineFix);
		});
		return result;
	}

	for (var num of course) {
		var orderTables = {};
		for (var order of orders) {
			var menu = combination(order.split(""), num);
			menu.forEach((v) => {
				if (v in orderTables) {
					orderTables[v] += 1;
				} else {
					orderTables[v] = 1;
				}
			});
		}

		var max = Math.max.apply(null, Object.values(orderTables));
		if (max < 2) {
			continue;
		} else {
			for (var k in orderTables) {
				if (orderTables[k] === max) {
					answer.push(k);
				}
			}
		}
	}
	answer.sort();
	return answer;
}
