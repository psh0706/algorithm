function solution(n) {
    return "수박".repeat(n/2)+"수".repeat(n%2);
}

// 문자열.repeat(반복횟수)
// -> 반복횟수가 0 일때는 빈 문자열 반환.
// 문자열 끼리는 더해질 수 있다.