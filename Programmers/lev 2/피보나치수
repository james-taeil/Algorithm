function solution(n) {
    let div = 1234567;
    const dp = [0, 1];
    for(let i = 2; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % div
    }
    return dp[n];
}
