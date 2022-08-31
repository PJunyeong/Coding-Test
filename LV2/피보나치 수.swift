//
//  피보나치 수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/31.
//

func solution(_ n:Int) -> Int {
    var dp = Array(repeating: 0, count: n+1)
    dp[1] = 1
    for i in 2..<n+1 {
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    }
    return dp[n]
}
