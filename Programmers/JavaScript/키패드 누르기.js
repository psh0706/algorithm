function solution(numbers, hand) {
    const delta = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    let answer = '';
    let distInfo = {};
    let arr = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"],["*", "0", "#"]];
    let distCheckList = [[0, 1], [1, 1], [2, 1], [3, 1]];
    let handInfo = {'left': "*", "right": "#"};

    // check distance
    distCheckList.map(item =>{
        let [x, y] = item.map(x => Number(x));
        let num = arr[item[0]][item[1]];
        let q = [[...item, 0]];
        let visit = Array.from(Array(4), () => Array(3).fill(false));
        visit[x][y] = true;
        distInfo[num] = {};

        while(q.length != 0){
            const node = q.shift(0);
            distInfo[num][arr[node[0]][node[1]]] = node[2];

            delta.map(d => {
                let dx = d[0] + node[0];
                let dy = d[1] + node[1];

                if(0 <= dx && dx < 4 && 0 <= dy && dy < 3 && !visit[dx][dy]){
                    visit[dx][dy] = true;
                    q.push([dx, dy, node[2] + 1]);
                }
            })
        }
    })


    // check L or R
    numbers.map(num => {
        num += "";
        if (num === '1' || num === '4' || num === '7'){
            answer += "L";
            handInfo["left"] = num;
        } else if (num === '3' || num === '6' || num === '9'){
            answer += "R";
            handInfo["right"] = num;
        } else {
            let L = distInfo[num][handInfo["left"]];
            let R = distInfo[num][handInfo["right"]];

            if(L < R){
                answer += "L";
                handInfo["left"] = num;
            } else if (R < L){
                answer += "R";
                handInfo["right"] = num;
            } else {
                answer += hand[0].toUpperCase();
                handInfo[hand] = num;

            }
        }
    })

    return answer;
}

/*
* 키패드 누르기 알고리즘
* 1, 4, 7 은 왼쪽 엄지 3, 6, 9 는 오른쪽 엄지로 항상 정해진 손가락이 있다.
* 2, 5, 8, 0 은 번호를 누를 때 마다 가장 가까이 있는 손가락을 선택해야 하므로 손가락 까지의 거리를 비교해야한다.
* 손가락이 있는 위치까지의 거리를 빠르게 알아내기 위해 먼저 2, 5, 8, 0을 각각 bfs 하여 각 키패드 까지의 거리를 미리 측정한다.
* 측정된 거리를 이용해 주어진 번호를 누를때 어느 손가락을 사용해야하는지 판단한다.
*/