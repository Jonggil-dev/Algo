function solution(today, terms, privacies) {
	const [today_year, today_month, today_day] = today.split(".");
	const termsObj = {};
	for (let term of terms) {
		const [a, b] = term.split(" ");
		termsObj[a] = Number(b);
	}

	var answer = [];

	privacies.map((item, index) => {
		const [date, term] = item.split(" ");
		let [year, month, day] = date.split(".");

		let diff =
			(Number(today_year) - Number(year)) * 12 +
			Number(today_month) -
			Number(month);

		if (diff > termsObj[term]) {
			answer.push(index + 1);
		} else if (diff == termsObj[term] && Number(today_day) >= Number(day)) {
			answer.push(index + 1);
		}
	});

	return answer;
}
