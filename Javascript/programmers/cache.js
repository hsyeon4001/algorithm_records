function solution(cacheSize, cities) {
	var answer = 0;
	var cache = [];

	if (cacheSize === 0) {
		answer = cities.length * 5;
		return answer;
	}

	for (var city of cities) {
		city = city.toLowerCase();
		if (cache.includes(city)) {
			cache.splice(cache.indexOf(city), 1);
			cache.push(city);
			answer += 1;
		} else {
			if (cache.length < cacheSize) {
				cache.push(city);
			} else {
				cache.shift();
				cache.push(city);
			}
			answer += 5;
		}
	}
	return answer;
}
