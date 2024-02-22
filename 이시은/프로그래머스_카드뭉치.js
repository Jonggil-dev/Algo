// 프로그래머스 Lv1 카드뭉치

function solution(cards1, cards2, goal) {
	let index1 = 0;
	let index2 = 0;

	let answer = true;
	goal.map((item) => {
		if (item == cards1[index1]) {
			index1 += 1;
		} else if (item == cards2[index2]) {
			index2 += 1;
		} else {
			answer = false;
		}
	});

	return answer ? "Yes" : "No";
}

const cards1 = ["i", "water", "drink"]; // ["i", "drink", "water"];
const cards2 = ["want", "to"]; //["want", "to"];
const goal = ["i", "want", "to", "drink", "water"];
console.log(solution(cards1, cards2, goal));
