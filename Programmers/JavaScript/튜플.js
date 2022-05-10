function solution(s) {
    let answer = [];
    let sList = [];
    let arr = [];
    const visit = {};

    // 숫자만 남겨서 중복을 없애고, 방문처리를 위한 배열 만들기
    sList = s.replace(/,/gi,' ').replace(/} {/gi, ' ').replace(/[{{}}]/gi, '').split(" ");
    sList = [...new Set(s)].map(x => visit[x] = false);

    // 집합의 길이 순으로 배열로 만들기
    arr = s.slice(2, -2).replace(/},{/gi,' ').split(" ").map(s => s.split(",")).sort((x,y) => x.length - y.length);

    // 집합 길이가 작은 순으로 배열을 순회하며 방문하지 않은 숫자 발견시 answer push
    arr.map(set =>{
        set.map(item => {
            if (!sList[item]){
                answer.push(Number(item));
                sList[item] = true;
            }
        })
    })

    return answer;
}

/*
처음엔 단순히 정규표현식으로 괄호와 컴마를 지운 후 중복제거를 하면 되는줄 알아서 잘못 풀었던 문제
튜플에는 순서가 있지만 튜플로써 만들어지는 집합 내부적으로는 순서가 없었다.
집합이 튜플의 순서(a1, a2, a3, ...)에 맞춰 "{a1},{a1, a2},{a1, a2, a3}..." 순으로 만들어진다는 점을 이용해 문제를 풀었다.
(이때 집합 내부의 순서는 변할 수 있다. "{a1},{a2, a1},{a3, a1, a2}..." 등)
가장 먼저 원본 문자열을 파싱해 모든 중복을 제거한 숫자 리스트를 만들어 방문처리를 위한 배열 visit 을 만들어주었고 (visit[숫자] = true/false)
원본 문자열을 다시 파싱해 집합의 길이가 작은 순으로 배열을 만들었다. -> [[a1], [a2, a1], [a3, a1, a2], ...]
배열을 순회하며 방문처리 되지 않은 숫자만을 찾아내 answer 에 push 했다.
*/