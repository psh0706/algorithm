function solution(s) {
    return s.split(' ').map(item => {
        return item.split('').map((x, idx) => (idx % 2 === 0 ? x.toUpperCase() : x.toLowerCase())).join('');
    }).join(' ');
}