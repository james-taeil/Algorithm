function solution(n) {
    let nbi = Number(n).toString(2);
    let nbiCount = nbi.match(/1/g).length;
    while(true){
        n+=1;
        let nextbi = Number(n).toString(2);
        let nextbiCount = nextbi.match(/1/g).length;
        if(nbiCount == nextbiCount){
            break;
        }
    }
    return n;
}
