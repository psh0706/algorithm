function solution(x) {
    let answer = true;
    const arr = String(x).split('').map(Number);
    const sum = arr.reduce((acc, item)=>{
        return acc+=item;
    },0)

    answer = (x % sum === 0);
    return answer;
}