function solution(arr) {
    let answer = [];
    const minIdx = arr.indexOf(Math.min(...arr));
    arr.splice(minIdx, 1);
    answer = arr.length === 0 ? [-1] : arr;
    return answer;
}