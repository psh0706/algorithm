function solution(s, n) {
    return s.split('').map(item => {
        const ascii = item.charCodeAt(0);

        if (item === " "){
            return item;
        }

        if (65 <= ascii && 90 >= ascii){
            return ascii+n > 90? String.fromCharCode(64+ascii+n-90) : String.fromCharCode(ascii+n);
        }else{
            return ascii+n > 122? String.fromCharCode(96+ascii+n-122) : String.fromCharCode(ascii+n);
        }
    }).join('');
}

// ASCII 코드를 계산하는 문제.
// ascii -> char : String.fromCharCode(아스키 코드);
// char -> ascii : 문자열.charCodeAt(문자열 인덱스);