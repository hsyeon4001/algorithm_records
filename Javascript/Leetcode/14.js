/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = function (strs) {
	let prefix = "";

	if (strs.length === 0) return prefix;

	const shortStr = strs.reduce((prev, curr) => {
		return prev.length > curr.length ? curr : prev;
	});

	const filteredStrs = strs.filter((str) => str != shortStr);
	const max = shortStr.length;

	for (let i = 0; i < max; i++) {
		const alphabets = filteredStrs.map((str) => str.charAt(i));
		const result = alphabets.filter((a) => a !== shortStr[i]);
		if (result.length === 0) {
			prefix += shortStr[i];
		} else {
			return prefix;
		}
	}

	return prefix;
};
