function solution(board, moves) {
    let answer = 0;
    const len = board.length;
    const stack = [];
    const newBoard = Array.from(new Array(len), () => new Array(len).fill(0));

    // setting newBoard = 전치
    board.map((item, i) => {
        item.map((x, j)=> {
            newBoard[j][i] = x;
        })
    });

    // stack을 관리하는 함수
    const addStack = (x) => {
        if (stack[stack.length-1] === x) {
            answer += 2;
            stack.pop();
        } else {
            stack.push(x);
        }
    }


    // move
    moves.map(move => {
        move--;
        for (let i=0; i<len; i++){
            if (newBoard[move][i] !== 0) {
                addStack(newBoard[move][i]);
                newBoard[move][i] = 0;
                break;
            }
        }
    });

    return answer;
}

// stack을 사용하는 간단한 문제