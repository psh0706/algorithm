function solution(s) {
    return s.split(' ').map(x => {
        return x.substr(0, 1).toUpperCase() + x.substr(1, x.length).toLowerCase();
    }).join(' ');
}