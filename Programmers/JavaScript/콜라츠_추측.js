function solution(num) {
    let answer = 0;
    console.log(num);
    while(true){
        if(num === 1){
            break;
        }

        if(answer === 500){
            answer = -1;
            break;
        }


        answer += 1
        num = (num%2 === 0)? num/2 : num*3+1;
    }
    return answer;
}