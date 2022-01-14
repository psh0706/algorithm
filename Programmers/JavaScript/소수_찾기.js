function solution(n) {
    let visit = new Array(n).fill(false);
    let answer = 0;

    for(let i=2; i<n+1; i++){
        if (visit[i]) {
            continue;
        }
        answer += 1;
        for (let j = i; j * i < n + 1; j++) {
            visit[j * i] = true;
        }
    }

    return answer;
}

// 에라스토테네스의 체 문제.
// 파이썬으로 구현해봤었던 문제라 금방 구현했다.
// 중요한 것은 10번라인의 for 문을 j*i 사이즈로 제한하는것.(단순 j가 아니라)
// -> visit 사이즈 = n - 1, visit 인덱스로의 접근 = i의 배수 이므로