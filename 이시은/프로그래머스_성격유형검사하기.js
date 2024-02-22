// 프로그래머스 lv1 성격 유형 검사하기

function solution(survey, choices) {
	const myObj = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 };

	survey.map((item, index) => {
		const [A, B] = item.split("");
		if (choices[index] <= 3) {
			myObj[A] += 4 - choices[index];
		} else if (choices[index] >= 5) {
			myObj[B] += choices[index] - 4;
		}
	});

	let answer = "";
	myObj.R >= myObj.T ? (answer += "R") : (answer += "T");
	myObj.C >= myObj.F ? (answer += "C") : (answer += "F");
	myObj.J >= myObj.M ? (answer += "J") : (answer += "M");
	myObj.A >= myObj.N ? (answer += "A") : (answer += "N");
	return answer;
}

// const survey = ["AN", "CF", "MJ", "RT", "NA"]
// const choices = [5, 3, 2, 7, 5]
// console.log(solution(survey, choices))

const survey = ["TR", "RT", "TR"];
const choices = [7, 1, 3];
console.log(solution(survey, choices));
