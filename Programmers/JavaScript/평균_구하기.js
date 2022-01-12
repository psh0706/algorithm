function solution(arr) {
    return arr.reduce((sum, item) => {
        return sum += item;
    }, 0) / arr.length;
}