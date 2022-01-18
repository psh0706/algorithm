function solution(s){
    let p = 0;
    let y = 0;

    s.split("").map(item => {
        let ch = item.toLowerCase();
        if(ch === 'p'){
            p += 1;
        }
        if(ch === 'y'){
            y += 1;
        }
    })

    return p === y;
}