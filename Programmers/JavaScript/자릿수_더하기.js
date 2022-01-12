function solution(n) {
    return String(n).split('').map(Number).reduce((sum, item) => (sum += item));
}