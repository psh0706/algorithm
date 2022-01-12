function solution(n, m) {
    let answer = [];
    let getGCD = (num1, num2) => {
        while(num2 > 0){
            let r = num1 % num2;
            num1 = num2;
            num2 = r;
        }
        return num1;
    };

    let getLCM = (num1, num2) => {
        return (num1*num2) / getGCD(num1, num2);
    }

    answer = [getGCD(n,m), getLCM(n, m)]

    return answer;
}