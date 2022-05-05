const Node = function(idx, prev, next){
    this.idx = idx;
    this.prev = prev;
    this.next = next;
}

function solution(n, k, cmd) {
    let answer = new Array(n).fill('O');
    let front = null, end = null;
    let head = new Node();

    // double linked list 초기화
    for(let i=0; i<n; i++){
        if(!front){
            front = new Node(i);
            end = front;
        }
        else{
            newNode = new Node(i);
            end.next = newNode;
            newNode.prev = end;
            end = newNode;
        }
        if(i === k){
            head = end;
        }
    }

    // 명령을 순차적으로 실행
    let history = [];
    cmd.map(op => {
        if(op === "C"){
            answer[head.idx] = 'X';
            prv = head.prev;
            nxt = head.next;
            history.push([head, prv, nxt]);

            if (prv) {
                prv.next = nxt;
            }

            if (nxt) {
                nxt.prev = prv;
            }

            if (!nxt) {
                head = prv;
            } else {
                head = nxt;
            }

        } else if (op === "Z") {
            [cur, prv, nxt] = history.pop();
            answer[cur.idx] = 'O';

            if (prv) {
                prv.next = cur;
            }

            if (nxt) {
                nxt.prev = cur;
            }

        } else {
            [d, num] = op.split(" ");
            if (d === "U") {
                for(let i=0; i<Number(num); i++){
                    head = head.prev;
                }
            } else {
                for(let i=0; i<Number(num); i++){
                    head = head.next;
                }
            }
        }
    });

    return answer.join('');
}

/*
* double linked list 문제를 javascript 로 구현해 보았다.
*/