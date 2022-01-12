function solution(n) {
    let answer = 0;
    let arr = String(n).split('').map(Number);
    arr.sort((a, b) =>{
        return b - a;
    });
    answer = parseInt(arr.map(String).join(''));
    return answer;
}