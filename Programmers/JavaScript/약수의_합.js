function solution(n) {
    return Array.from({length: n+1}, (v, i) => i).reduce((sum, item)=> n%item === 0? sum+=item : sum);
}

// Array.form 으로 수열 생성.
// Array.from({length: n+1}, (v, i) => i) n 까지의 수열 만들기
// reduce((sum, item)=> n%item === 0? sum+=item : sum) 0으로 나누어 떨어지는 숫자들만 더하기