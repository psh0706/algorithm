function solution(x, n) {
    let answer = [x];

    for(let i=1; i<n; i++){
        answer.push(answer[i-1]+x)
    }
    return answer;
}