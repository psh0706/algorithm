function solution(s) {
    let answer = s;
    let word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for(let i=0; i<word.length; i++){
        let arr = answer.split(word[i]);
        answer = arr.join(i)
    }

    answer = Number(answer)
    return answer;
}

/*
단어로 split 한 후, 해당 단어를 나타내는 숫자로 다시 이어 붙혀주는 방식을 사용.
 */